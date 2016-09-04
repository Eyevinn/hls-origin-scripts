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
    parser = argparse.ArgumentParser(description="Generate a VOD HLS playlist between two timestamps in a LIVE HLS playlist")
    parser.add_argument('hlsdir', metavar='HLSDIR', default=None, help="path to directory where HLS files are being archived")
    parser.add_argument('--in', dest='ints', default=None, help="YYYY-mm-dd HH:MM:SS")
    parser.add_argument('--out', dest='outts', default=None, help="YYYY-mm-dd HH:MM:SS")
    parser.add_argument('--mediaplaylist', dest='mediaplaylist', default=None, help="name of media playlist, e.g: master800.m3u8")
    parser.add_argument('--noremovecueout', dest='noremovecueout', action='store_true', default=False, help="do not remove segments in cue out periods")
    parser.add_argument('--debug', dest='debug', action='store_true', default=False, help='Write debug info to stderr')
    args = parser.parse_args()
    debug.doDebug = args.debug

    debug.log("Generating media playlist for %s%s-* from %s to %s" % (args.hlsdir, args.mediaplaylist, args.ints, args.outts))    
    if not util.isValidTimestamp(args.ints):
        raise Exception("Invalid in timestamp") 
    if not util.isValidTimestamp(args.outts):
        raise Exception("Invalid out timestamp") 
    manifests = ManifestList(args.mediaplaylist, args.hlsdir)
    manipulator = Manipulator(manifests)
    print manipulator.vodFromLive(args.ints, args.outts, not args.noremovecueout)
    
if __name__ == '__main__':
    try:
        main()
    except Exception, err:
        raise

