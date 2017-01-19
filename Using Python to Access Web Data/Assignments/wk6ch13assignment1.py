import json
import urllib
url = raw_input('Enter url...')
print 'Retrieving', url

uh = urllib.urlopen(url)
data = uh.read()
# deserializing from json and get back a dictionrary
info = json.loads(data)
print'Retrieved', len(info), 'characters'

pile = 0
count = 0

# two elements of dictionary
# 2nd key "comments", value is another dictionary
# loop through the value dictionary
for item in info['comments']:
    # item is a dictionary
	num = item['count']
	count = count + 1
	pile = pile + num
print "count:", count
print "sum:", pile