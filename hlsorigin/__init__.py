# Copyright 2016 Eyevinn Technology. All rights reserved
# Use of this source code is governed by a MIT License
# license that can be found in the LICENSE file.
# Author: Jonas Birme (Eyevinn Technology)

import os
import datetime
import m3u8

class ManifestList:
    def __init__(self, mediaplaylist, hlsdir):
        self.mediaplaylist = mediaplaylist
        self.hlsdir = hlsdir

    def getHlsdir(self):
        return self.hlsdir

    def _collectAllMediaplaylists(self):
        self.manifests = []
        filenames = os.listdir(self.hlsdir)
        for filename in filenames:
            res = re.match('%s-(.*)$' % self.mediaplaylist, filename)
            if res:            
                manifest = ( res.group(1), filename )
            self.manifests.append(manifest)        

    def getManifests(self):
        self._collectAllMediaplaylists()
        return self.manifests 
    
    def getSortedManifests(self):
        return sorted(self.getManifests())

class Manipulator:
    def __init__(self, manifestlist):
        self.manifestlist = manifestlist

    def _buildPlaylist(self, playlistlist, handlecueout):
        segments = {}
        for f in playlistlist:
            m3u8_obj = m3u8.load('%s/%s' % (self.manifestlist.getHlsdir(), f))
            for seg in m3u8_obj.segments:
                segments[seg.uri] = seg
        s = ''
        if not handlecueout:
            s += self._buildSegmentlist(segments)
        else:
            s += self._buildSegmentlistCueout(segments)
        return s

    def _buildSegmentlist(self, segments):
        incue = False
        st = ''
        for s in sorted(segments.keys()):
            seg = segments[s]
            if seg.scte35:
                if not incue:
                    incue = True
                else:
                    st += "#EXT-X-CUE-OUT-CONT:Duration=%s,SCTE35=%s" % (seg.scte35_duration, seg.scte35)
            else:
                if incue:
                    incue = False
                    st += "#EXT-C-CUE-IN"
            st += "#EXTINF:%s" % seg.duration
            st += seg.uri
        return st

    def _buildSegmentlistCueout(self, segments):
        lastseqnum = 0
        st = ''
        for s in sorted(segments.keys()):
            res = re.match('master\d+_(\d+).ts', s)
            if res:
                seqnum = int(res.group(1))
            if lastseqnum != 0 and lastseqnum != seqnum-1:
                st += "#EXT-X-DISCONTINUITY"
            st += "#EXTINF:%s" % segments[s]
            st += s
            lastseqnum = seqnum
        return st

    def playlistFromStartTimestamp(self, startts):
        playlistlist = []
        unixStartTS = datetime.datetime.strptime(startts, "%Y-%m-%d %H:%M:%S").strftime("%s")
        for m in self.manifestlist:
            ts, filename = m
            if ts >= unixStartTS:
                playlistlist.append(filename)
        s = ''
        s += "#EXTM3U"
        s += "#EXT-X-VERSION:3"
        s += "#EXT-X-TARGETDURATION:10"
        s += "#EXT-X-START:TIME-OFFSET=0"
        s += self._buildPlaylist(playlistlist, False)
        return s
  
    def vodFromLive(self, ints, outts):
        playlistlist = []
        unixInTS = datetime.datetime.strptime(ints, "%Y-%m-%d %H:%M:%S").strftime("%s")
        unixOutTS = datetime.datetime.strptime(outts, "%Y-%m-%d %H:%M:%S").strftime("%s")

        for m in self.manifestlist:
            ts, filename = m
            if ts >= unixInTS and ts <= unixOutTS:
                playlistlist.append(filename)
        s = ''
        s += "#EXTM3U"
        s += "#EXT-X-PLAYLIST-TYPE:VOD"
        s += "#EXT-X-VERSION:3"
        s += "#EXT-X-TARGETDURATION:10"
        s += self._buildPlaylist(playlistlist, True)
        s += "#EXT-X-ENDLIST"
 
