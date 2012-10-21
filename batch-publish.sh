#!/bin/sh
# Add org file changes to the repository
# [[file:/etc/crontab][crontab]]

DOTPATH=/home/eab/git/emacs/init.el
export EMACS_SERVER_NAME=serverN
export DISPLAY=:0.0

# /usr/local/bin/emacs -Q --batch -l $DOTPATH --eval "(org-publish-project \"html\" t)"
# /usr/local/bin/emacs -Q --batch -l $DOTPATH --eval "(eab/send-csum)"

emacsclient -s $EMACS_SERVER_NAME -c --eval "(progn (eab/update-reports-nightly) (org-publish-project \"html\" t) (org-publish-project \"pdf\" t) (eab/send-csum) (org-mobile-push) (org-agenda nil \"H\") (delete-frame nil 'force))"
