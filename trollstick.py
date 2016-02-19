import os, urllib2

image = urllib2.urlopen('http://tekromancr.github.io/trollstick/lol.jpg')
with open("/tmp/lol.jpg", "wb") as f:
    f.write(image.read())

