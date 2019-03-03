import dbus
import time

# The property Metadata behaves like a python dict
while(True):
    session_bus = dbus.SessionBus()
    spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify",
                                     "/org/mpris/MediaPlayer2")
    spotify_properties = dbus.Interface(spotify_bus,
                                    "org.freedesktop.DBus.Properties")
    metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")
    for key, value in metadata.items():
        print(key, value)

    # To just print the title
    print(metadata['xesam:title'])

    time.sleep(5)