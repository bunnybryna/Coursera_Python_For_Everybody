import urllib
import xml.etree.ElementTree as ET

address = raw_input('Enter location: ')
print 'Retrieving', address
# for urllib.urlopen(),go back to review wk3ch12assignment
uh = urllib.urlopen(address)
data = uh.read()
print 'Retrieved',len(data),'characters'
# like deserializing,get back an object'tree'
tree = ET.fromstring(data)
# comments/comment in the path, returns a list
lst = tree.findall('comments/comment')
pile = 0
count = 0
for item in lst:
	num = int(item.find('count').text)
	count = count + 1
	pile = pile + num
print "count:", count
print "sum:", pile
 
