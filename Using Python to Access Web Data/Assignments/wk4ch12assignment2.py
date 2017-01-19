import urllib
from BeautifulSoup import *

for count in range(0,7):
	# at the 1st time, url = raw input
	if count == 0:
		url = raw_input('Enter:')
		html = urllib.urlopen(url).read()
		soup = BeautifulSoup(html)
		tags = soup('a')
		tag18 = tags[17]
		urlnew = tag18.get('href',None)
		name = tag18.contents[0]
		count = count + 1
	# from the 2nd time, url is the link from last page
	elif count > 0 and count < 7: 
		url = urlnew
		html = urllib.urlopen(url).read()
		soup = BeautifulSoup(html)
		tags = soup('a')
		# tags is a list of tags, find the link at position 18
		tag18 = tags[17]
		# get the new url to generate the next list
		urlnew = tag18.get('href',None)
		# pull out the name from the tag
		name = tag18.contents[0]
		# automatically increment 
		count = count + 1
	# at the 8th times, stop the loop	
	else:
		break
print name