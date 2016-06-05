#!/bin/bash
echo "Content-type: text/html"
echo ''
echo 'NMAP to HTML'

nmap localhost | grep open | awk '{print $1}'
