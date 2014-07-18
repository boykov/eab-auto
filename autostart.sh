#!/bin/sh

bash -i -c "sudo noip2 &"
bash -i -c "cd ~/data/gitno/github/boykov.github.io/ && jekyll -w serve &"
bash -i -c "~/bin/cloud &"
bash -i -c "sudo dovecot &"
bash -i -c "~/.dropbox-dist/dropboxd &"
bash -i -c "/home/eab/tmp/ann/git-annex.linux/git-annex assistant --autostart &"
bash -i -c "export DISPLAY=:0 && gnome-screensaver-command -l"
bash -i -c "psensor &"
# bash -i -c "/opt/TakeBreak/TakeBreak &"
# bash -i -c "python /home/eab/git/python/watch_share.py &"
bash -i -c "indicator-multiload &"
