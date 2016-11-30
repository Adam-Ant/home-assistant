import mpd

client = mpd.MPDClient()
client.connect("192.168.1.62",6600)
client.stop()
client.clear()
client.random(0)
client.consume(0)
client.close()
client.disconnect()
