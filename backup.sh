#!/bin/sh

sudo mount -t smbfs -o password=,uid=eab,gid=eab //192.168.0.112/eab /home/eab/117/

rsync --delete -avzL ~/rsync/cc/ ~/117/rsync/cc
rsync --delete -avzL ~/rsync/share/ ~/117/rsync/share

sudo umount /home/eab/117/
