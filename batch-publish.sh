#!/bin/sh
# Add org file changes to the repository
# [[file:/etc/crontab][crontab]]

DOTPATH=/home/eab/git/emacs/init.el

/usr/local/bin/emacs -Q --batch -l $DOTPATH --eval "(org-publish-project \"html\" t)"
# -l /home/eab/git/emacs/eab-auto-exec.el
