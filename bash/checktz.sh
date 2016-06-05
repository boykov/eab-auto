#!/bin/sh
T1=$(LC_ALL=C TZ=Europe/Moscow date -d @1409067890)
if [ "$T1" != 'Tue Aug 26 19:44:50 MSK 2014' ] ; then
    echo FAIL! Wrong TZ BEFORE 26 Oct 2014!
    exit 1
fi
T2=$(LC_ALL=C TZ=Europe/Moscow date -d @1416667890)
if [ "$T2" != 'Sat Nov 22 17:51:30 MSK 2014' ] ; then
    echo FAIL! Wrong TZ AFTER 26 Oct 2014!
    exit 2
fi
echo OK