#!/bin/sh
if find /home/john/Dropbox/git/ -type d -name '*.git' | sed 's@^/media/disk/@@; s/.git$//' | while read repo; do
	if test -d ~/git/$repo/.git
	then
	    echo REPO: $repo
	    cd ~/git/$repo
	    if ! git push drop
	    then
		exit 1;
	    fi
	fi
    done
then
    # echo Unmounting USB stick...
    # umount /media/disk
    echo All done.;
else
    echo Fix and redo.;
fi
