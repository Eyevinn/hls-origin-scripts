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

# Usage

These scripts are executed by the request handler at the origin webserver.

## hls-capture

## hls-live-from-vod

## hls-startover