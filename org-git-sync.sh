#!/bin/sh
# Add org file changes to the repository
# [[file:/etc/crontab][crontab]]
REPOS="home cc difwave/mpl difwave/gmres difwave/upr_upr difwave/namelib org lit emacs auto python patches" 

for REPO in $REPOS
do
    echo "Repository: $REPO"
    cd ~/git/$REPO
# Remove deleted files
    git ls-files --deleted -z | xargs -0 git rm >/dev/null 2>&1
# Add new files
    git add . >/dev/null 2>&1
    # git config --global user.name "Evgeny Boykov"
    # git config --global user.email artscan@list.ru
    git commit -m "$(date)"
    git status | grep -qF 'working directory clean'
done
