#!/bin/sh

cd /var/mail
# sudo cp eab ~/data/mail/eab.bak
grepmail -i "(failed|error)" eab >> ~/data/mail/inbox
grepmail -i -v "(failed|error|1353298727)" eab >> ~/data/mail/eab.bak
grepmail 1353298727 eab > eab.tmp
cp -f eab.tmp eab  # DONE если нет grepmail, то можно удалить всю почту
# sudo chown eab:mail /var/mail/eab
# sudo chmod o-r /var/mail/eab
# sudo chmod g+rw /var/mail/eab
