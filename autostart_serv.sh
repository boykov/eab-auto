#!/bin/sh

# bash -i -c "sudo noip2 &"
# bash -i -c "cd ~/data/gitno/github/boykov.github.io/ && jekyll -w serve &"
# bash -i -c "~/bin/cloud &"
bash -i -c "export USER=eab && sudo dovecot &"
bash -i -c "export USER=eab && /home/eab/.dropbox-dist/dropboxd &"
# bash -i -c "/home/eab/tmp/ann/git-annex.linux/git-annex assistant --autostart &"
# bash -i -c "export DISPLAY=:0 && gnome-screensaver-command -l"
# bash -i -c "psensor &"
bash -i -c "export USER=eab && sudo docker start jenkins &"
# eval `ssh-agent -s`
# # bash -i -c "/opt/TakeBreak/TakeBreak &"
# # bash -i -c "python /home/eab/git/python/watch_share.py &"
# bash -i -c "indicator-multiload &"
# bash -i -c "skype &"
# # bash -i -c "transmission-gtk &"
# # bash -i -c "sudo mount -t cifs -o user=eab,password=,dir_mode=0777,file_mode=0777 //192.168.0.4/share ~/jonesbook &"
# bash -i -c "mono ~/KeePass/KeePass.exe &"
bash -i -c "export USER=eab && mediatomb -e eth0 &"
sudo mount --bind "/home/eab/downloads/pub/papers" "/home/eab/share/papers"
sudo mount --bind "/home/eab/git/cc/boykov-2014-cmmf/boykov-2016" "/home/eab/share/boykov-2016/"
sudo mount --bind "/home/eab/newdata/Cloud@Mail.Ru/read/" "/home/eab/share/read/"

