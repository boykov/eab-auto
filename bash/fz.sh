#!/bin/sh

sudo openvpn --config /etc/openvpn/fz.conf --route-noexec --dev tun5 --auth-user-pass /etc/openvpn/fzauth.conf &
sleep 10
GATEWAY=$(route | grep -h tun5 | awk '{print $1}')
sudo route add 193.142.56.242 gw $GATEWAY tun5
sudo route add 217.23.158.114 gw $GATEWAY tun5

