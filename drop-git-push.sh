#!/bin/sh
if find /home/$USER/Dropbox/git/ -type d -name '*.git' | sed 's@^/home/'$USER'/Dropbox/git/@@; s/.git$//' | while read repo; do
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
    # TODO put here alert message!
fi
