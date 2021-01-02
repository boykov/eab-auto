sudo docker run -d \
    --name=firefox \
    -p 5800:5800 \
    -v /home/vagrant/tmp/firefox:/config:rw \
    -p 5900:5900 \
    --shm-size 2g \
    --privileged \
    jlesage/firefox