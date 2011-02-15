#!/bin/sh

is=`ping -c 3 192.168.0.107 | grep -c "64 bytes"`
   # Проверяем прошли ли пинги на мой ip адрес внутри СС, дома точно такого нет 
if !(test $is -gt "0") # если пинги не проходят
then
    echo "CC server is down"
    return 1
else
    return 0
    echo "we are in CC"
fi
