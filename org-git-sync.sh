#!/bin/sh
# Add org file changes to the repository
# [[file:/etc/crontab][crontab]]
REPOS="org cc mpl hron home emacs auto python timekeeper difwave/uu difwave/upr_upr difwave/forgen difwave/gmres difwave/namelib" 

for REPO in $REPOS
do
    echo "Repository: $REPO"
    cd ~/git/$REPO
# Remove deleted files
    git ls-files --deleted -z | xargs -0 git rm >/dev/null 2>&1
# Add new files
    git add . >/dev/null 2>&1
    git commit -m "$(date)"
done
