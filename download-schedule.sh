#!/bin/bash
# Add org file changes to the repository
# [[file:/etc/crontab][crontab]]

cd ~/data/admin
test -s kav_rescue_10.iso && mv kav_rescue_10.iso kav_rescue_10.iso.bak
rm -f kav_rescue_10.md5.txt
wget http://rescuedisk.kaspersky-labs.com/rescuedisk/updatable/kav_rescue_10.iso
wget http://rescuedisk.kaspersky-labs.com/rescuedisk/updatable/kav_rescue_10.md5.txt
md5sum kav_rescue_10.iso
cat kav_rescue_10.md5.txt

test -s drweb-livedisk-900-cd.iso && mv drweb-livedisk-900-cd.iso drweb-livedisk-900-cd.iso.bak
wget https://download.geo.drweb.com/pub/drweb/livedisk/drweb-livedisk-900-cd.iso
