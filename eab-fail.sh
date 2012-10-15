#!/bin/sh

cd /var/mail
grepmail failed eab >> ~/data/mail/inbox
grepmail -v failed eab > ~/data/mail/eab.bak

