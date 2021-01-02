#!/bin/sh

#bash -i -c "sudo su eab -l -c /home/eab/git/auto/sshcyclos.sh & "
bash -i -c "syncthing &"
# bash -i -c "sudo noip2 &"
# bash -i -c "cd ~/data/gitno/github/boykov.github.io/ && jekyll -w serve &"
# bash -i -c "~/bin/cloud &"
bash -i -c "export USER=eab && sudo dovecot &"
bash -i -c "export USER=eab && /home/eab/.dropbox-dist/dropboxd &"
# bash -i -c "/home/eab/tmp/ann/git-annex.linux/git-annex assistant --autostart &"
# bash -i -c "export USER=eab && sudo docker start jenkins &"
# # bash -i -c "python /home/eab/git/python/watch_share.py &"
# # bash -i -c "sudo mount -t cifs -o user=eab,password=,dir_mode=0777,file_mode=0777 //192.168.0.4/share ~/jonesbook &"
# bash -i -c "mono ~/KeePass/KeePass.exe &"
sudo mount --bind "/home/eab/data/papers" "/home/eab/share/papers"
sudo mount --bind "/home/eab/data/papers" "/home/eab/share/tor/papers"
sudo mount --bind "/home/eab/git/cc/" "/home/eab/share/cc/"
sudo mount --bind "/home/eab/git/cc/boykov.github.io/org-html-themes/styles" "/home/eab/pub/org/css/styles"
sudo service samba restart 
sudo service transmission-daemon start
