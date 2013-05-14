#!/bin/sh
# Add org file changes to the repository
# [[file:/etc/crontab][crontab]]

DOTPATH=/home/eab/git/emacs/init.el
export EMACS_SERVER_NAME=serverN
export DISPLAY=:0.0

# /usr/local/bin/emacs -Q --batch -l $DOTPATH --eval "(org-publish-project \"html\" t)"
# /usr/local/bin/emacs -Q --batch -l $DOTPATH --eval "(eab/send-csum)"

emacsclient -s $EMACS_SERVER_NAME -c --eval "(progn (eab/update-reports-nightly) (org-publish-project \"html\" t) (eab/send-csum) (eab/send-csum-all) (org-mobile-push) (delete-frame nil 'force))"
# emacsclient -c --eval "(progn (org-agenda nil \"H\") (delete-frame nil 'force))"
# (org-publish-project \"pdf\" t)
