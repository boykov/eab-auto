#!/usr/bin/env python

def my_func(account, sender, message, conversation, flags):
    print sender, "said:", message

import dbus, gobject
from dbus.mainloop.glib import DBusGMainLoop

dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

bus = dbus.SessionBus()

bus.add_signal_receiver(my_func,
                        dbus_interface="im.pidgin.purple.PurpleInterface",
                        signal_name="ReceivedImMsg")

loop = gobject.MainLoop()
loop.run()


# obj = bus.get_object("im.pidgin.purple.PurpleService", "/im/pidgin/purple/PurpleObject")
# purple = dbus.Interface(obj, "im.pidgin.purple.PurpleInterface")
# purple.PurpleConvImSend(purple.PurpleConvIm(purple.PurpleGetIms()[0]),"hi!")

