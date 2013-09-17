#!/bin/sh

if (emacsclient --eval "(eab/show-minibuffer-frame)")
then
    return 0
else
    gnome-terminal
fi
