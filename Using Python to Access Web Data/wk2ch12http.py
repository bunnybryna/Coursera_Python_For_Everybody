import socket
# socket is the library,.socket() is a function within the library
# create a socket (an end point)
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# connect extends the end point, push it across the Internet and lock in on the other side
# establish a connection between me and the host www.py4inf.com, go to port 80 on that
# if there is no web server, this line will blow up
# mysocket.connect is like the open() call to read a file
mysock .connect(('www'py4inf.com',80))

# http://www.dr-chunk.com/page1.html
# protocol+host+document,URL, uniform resource locator
# request-response cycle
mysock.send('GET http://py4inf.com/code/romeo.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
	if (len(data)<1):
	    break
	print data
mysock.close()

# using urllib in Python
import urllib
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

for line in fhand:
    print line.strip()
	
counts = dict()
for line in fhand:
    words = line.split()
	for word in words:
	    counts[word] = counts.get(word,0) + 1
print counts

