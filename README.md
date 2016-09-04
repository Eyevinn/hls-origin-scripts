# Description
This package contains useful scripts to manipulate HLS manifests at origin or edge server.

| Script         | Description         |
| -------------- | ------------------- |
| hls-capture    | Create a VOD playlist between two timestamps in a LIVE playlist |
| hls-live-from-vod  | Create a LIVE playlist from a set of VOD playlists |
| hls-startover  | Create a LIVE playlist from a specific starttime in another LIVE playlist |

## Preconditions
These scripts are based on the assumption that all HLS manifest files and segments are archived at the origin server where these scripts are executed. The archive for a specific live stream contains the history for all HLS manifest updates. For example:

Live HLS stream called 'foo' is archived in the directory /archive/foo on the server. It contains all updated HLS manifest files with a unix timestamp when it was last updated.

	master800.m3u8-1472977456
	master800.m3u8-1472977465
	master800.m3u8-1472977475
	
All video segments are also stored in the same directory.

# Installation
From source

	git clone https://github.com/Eyevinn/hls-origin-scripts.git
	cd hls-origin-scripts
	python setup.py install
	
# Usage

These scripts are executed by the request handler at the origin webserver. The scripts output the generated manifest file to stdout

## hls-capture
Generate a VOD playlist from a LIVE HLS where segments and manifest files are archived at /hlsarchive/stream/. A 20 minutes VOD manifest from 11:45 to 12:05 is created in this case.

	hls-capture /hlsarchive/stream/ --mediaplaylist master800.m3u8 --in "2016-09-04 11:45:00" --out "2016-09-04 12:05:00"
	
By default any cueout periods (e.g. ads) are removed and a discontinuity tag is added in the generated manifest. Available options:

	--help					show help message and exit
	--in TS				YYYY-mm-dd HH:MM:SS
	--out TS				YYYY-mm-dd HH:MM:SS
	--mediaplaylist PL	name of media playlist
	--noremovecueout		do not remove segments in cue out periods

## hls-startover
Generate a new LIVE HLS playlist with a new start position. This is useful when needing a startover functionality but the user should not be able to watch before the startover position.

	hls-startover /hlsarchive/stream/ --mediaplaylist master800.m3u8 --startover "2016-09-04 16:25:00"
	
Available options:

	--help					show help message and exit
	--mediaplaylist PL	name of media playlist
	--startover TS		YYYY-mm-dd HH:MM:SS
	
## hls-live-from-vod

TBD