#!/bin/sh
# Test dotemacs config

export EMACS_SERVER_NAME=serverM
export DISPLAY=:0.0

dbus-launch `which emacs` --daemon=$EMACS_SERVER_NAME

emacsclient -s $EMACS_SERVER_NAME -c --eval "(eab/test-dotemacs)"
