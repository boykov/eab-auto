#!/bin/bash
# Add org file changes to the repository
# [[file:/etc/crontab][crontab]]

cd ~/data/tor
wget http://rescuedisk.kaspersky-labs.com/rescuedisk/updatable/kav_rescue_10.iso
wget http://rescuedisk.kaspersky-labs.com/rescuedisk/updatable/kav_rescue_10.md5.txt
md5sum kav_rescue_10.iso
cat kav_rescue_10.md5.txt
