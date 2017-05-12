docker run -ti --rm -v $('pwd'):/mnt/workspace \
-v /home/eab/.emacs.d:/home/emacs/.emacs.d \
-v /etc/localtime:/etc/localtime:ro \
-v /var/run/dbus/system_bus_socket:/var/run/dbus/system_bus_socket \
-v /tmp/.X11-unix:/tmp/.X11-unix \
-e DISPLAY=$DISPLAY \
-e TERM=xterm-256color \
-e TZ=UA \
 --name spacemacs jare/emacs
