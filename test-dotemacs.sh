#!/bin/sh
# Test dotemacs config

export EMACS_SERVER_NAME=serverM
# export DISPLAY=:0.0

/home/eab/data/gitno/emacs24.4/emacs-24.5/src/emacs-24.5.1 --daemon=$EMACS_SERVER_NAME

sleep 1

emacsclient -s $EMACS_SERVER_NAME --eval "(eab/test-dotemacs)"
