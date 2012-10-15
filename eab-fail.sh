#!/bin/sh

cd /var/mail
grepmail failed eab >> ~/data/mail/inbox
grepmail -v failed eab > ~/data/mail/eab.bak
sudo rm eab
sudo cp ~/data/mail/eab.bak eab
sudo chown eab:mail /var/mail/eab
sudo chmod o-r /var/mail/eab
sudo chmod g+rw /var/mail/eab
