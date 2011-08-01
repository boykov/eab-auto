export AP_PORT=$(netstat -napt|sed -n 's/^tcp.*127.0.0.1:\([0-9]*\).*LISTEN.*ase$/\1/gp')
python