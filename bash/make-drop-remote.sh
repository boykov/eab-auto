#!/bin/sh
# Add org file changes to the repository
# [[file:/etc/crontab][crontab]]
REPOS="org cc mpl hron home emacs timekeeper difwave/uu difwave/upr_upr"

for REPO in $REPOS
do
    echo "Repository: $REPO"
    cd ~/git/$REPO
    git remote add drop /home/$USER/Dropbox/git/$REPO.git
done
