#!/bin/sh

docker run --rm --user $UID:$GID -v /home/eab/share/tube:/data eab/youtube-dl --extract-audio --audio-format mp3 $* > /dev/null &


# docker run --rm --user $UID:$GID -v /home/eab/share/tube:/data vimagick/youtube-dl --extract-audio --audio-format mp3 $* > /dev/null &

# cd /home/eab/share/tube
# /home/eab/bin/youtube-dl --extract-audio --audio-format mp3 $* > /dev/null &
