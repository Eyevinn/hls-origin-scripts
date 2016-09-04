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

    def playlistFromStartTimestamp(self, startts):
        return ""
  
