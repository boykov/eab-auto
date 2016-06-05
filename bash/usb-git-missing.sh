#!/bin/sh
find /usb -type d -name '*.git' | sed 's@^/usb/@@; s/.git$//' | while read repo; do 
    if ! test -d ~/$repo/.git
    then
	echo REPO: $repo
    fi
done
