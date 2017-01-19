import urllib
from BeautifulSoup import *

url = raw_input('Enter-')
# read the HTML from data and parse the data using urllib and BeautifulSoup
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
# find all the <span> tags
tags = soup('span')
count = 0
pile = 0
for tag in tags:
# pull out the number from the tag
	num=tag.contents[0]
	pile = pile + int(num)  
	count = count + 1
print "count", count
print "total", pile
	