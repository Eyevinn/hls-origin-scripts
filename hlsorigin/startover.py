# Copyright 2016 Eyevinn Technology. All rights reserved
# Use of this source code is governed by a MIT License
# license that can be found in the LICENSE file.
# Author: Jonas Birme (Eyevinn Technology)

import argparse
from hlsorigin import debug
from hlsorigin import util
from hlsorigin import ManifestList
from hlsorigin import Manipulator

def main():
    parser = argparse.ArgumentParser(description="Generate an HLS media playlist from a start-over position")
    parser.add_argument('hlsdir', metavar='HLSDIR', default=None, help="path to directory where HLS files are being archived")
    parser.add_argument('--startover', dest='startover', default=None, help="YYYY-mm-dd HH:MM:SS")
    parser.add_argument('--mediaplaylist', dest='mediaplaylist', default=None, help="name of media playlist, e.g: master800.m3u8")
    parser.add_argument('--lstfile', dest='lstfile', default=None, help="Use LST file to collect all media playlists")
    parser.add_argument('--debug', dest='debug', action='store_true', default=False, help='Write debug info to stderr')
    args = parser.parse_args()
    debug.doDebug = args.debug

    debug.log("Generating media playlist for %s%s-* from start-over position %s" % (args.hlsdir, args.mediaplaylist, args.startover))    
    if not util.isValidTimestamp(args.startover):
        raise Exception("Invalid timestamp") 
    if not args.mediaplaylist: 
        raise Exception("Media playlist not specified")
    manifests = ManifestList(args.mediaplaylist, args.hlsdir, args.lstfile)
    manipulator = Manipulator(manifests)
    print manipulator.playlistFromStartTimestamp(args.startover)

if __name__ == '__main__':
    try:
        main()
    except Exception, err:
        raise

