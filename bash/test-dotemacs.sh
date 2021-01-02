#!/bin/sh
# Test dotemacs config

export EMACS_SERVER_NAME=serverM
# export DISPLAY=:0.0

emacs25 --daemon=$EMACS_SERVER_NAME

sleep 1

emacsclient -s $EMACS_SERVER_NAME --eval "(eab/test-dotemacs)"
