import mpd

client = mpd.MPDClient()
client.connect("192.168.1.62",6600)
client.clear()
client.load("morning")
client.random(1)
client.consume(1)
client.play()
client.close()
client.disconnect()
