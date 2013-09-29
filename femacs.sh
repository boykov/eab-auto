#!/bin/sh

if (emacsclient --eval "$*")
then
    return 0
else
    gnome-terminal
fi
