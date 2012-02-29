#!/bin/sh
# Add org file changes to the repository
# [[file:/etc/crontab][crontab]]

DOTPATH=/home/eab/git/emacs/init.el
export EMACS_SERVER_NAME=serverN

# /usr/local/bin/emacs -Q --batch -l $DOTPATH --eval "(org-publish-project \"html\" t)"
# /usr/local/bin/emacs -Q --batch -l $DOTPATH --eval "(eab/send-csum)"

emacsclient -s $EMACS_SERVER_NAME --eval "(org-publish-project \"html\" t)"
emacsclient -s $EMACS_SERVER_NAME --eval "(eab/send-csum)"
