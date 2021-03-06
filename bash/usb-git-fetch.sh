#!/bin/sh
# Download objects and refs from repositories on /media/disk
find /media/disk -type d -name '*.git' | sed 's@^/media/disk/@@; s/.git$//' | while read repo; do 
 if test -d ~/git/$repo/.git
 then
	echo REPO: $repo
	cd ~/git/$repo
	git fetch usb
 fi
done
