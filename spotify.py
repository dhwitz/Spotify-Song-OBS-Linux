"""

GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

@author David E. Horowitz

"""

#[Imports]
import dbus
import time

#[Globals]
_application = "org.mpris.MediaPlayer2.spotify"
_path = "/org/mpris/MediaPlayer2"
_prop = "org.freedesktop.DBus.Properties"

session_bus = dbus.SessionBus()
spotify_bus = session_bus.get_object(_application, _path)
spotify_prop = dbus.Interface(spotify_bus, _prop)

def create_values():
    global session_bus, spotify_bus, spotify_prop
    session_bus = dbus.SessionBus()
    spotify_bus = session_bus.get_object(_application, _path)
    spotify_prop = dbus.Interface(spotify_bus, _prop)

def current_song():
    if not session_bus or not spotify_bus or not spotify_prop:
        create_values()
    metadata = spotify_prop.Get("org.mpris.MediaPlayer2.Player", "Metadata")
    return metadata.get("xesam:title", "Spotify Not Found!")

def main():
    # single threaded application
    while True:
        print(current_song())
        time.sleep(5)

if __name__ == "__main__":
    main()
