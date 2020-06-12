#!/bin/sh

docker run --rm --user $UID:$GID -v /home/eab/share/tube:/data vimagick/youtube-dl --extract-audio --audio-format mp3 $* > /dev/null &
