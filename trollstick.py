import os, urllib2

image = urllib2.urlopen('https://raw.githubusercontent.com/tekromancr/trollstick/gh-pages/lol.jpg')
with open("/tmp/lol.jpg", "wb") as f:
    f.write(image.read())
command = '''osascript -e 'tell application "Finder" to set desktop picture to POSIX file "/tmp/lol.jpg"'''
os.system(command)
