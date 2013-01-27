#!/bin/sh

cd /var/mail
sudo cp eab ~/data/mail/eab.bak
grepmail failed eab >> ~/data/mail/inbox
grepmail -v failed eab > ~/data/mail/eab.bak
sudo rm eab # DONE если нет grepmail, то можно удалить всю почту
sudo cp ~/data/mail/eab.bak eab
sudo chown eab:mail /var/mail/eab
sudo chmod o-r /var/mail/eab
sudo chmod g+rw /var/mail/eab
