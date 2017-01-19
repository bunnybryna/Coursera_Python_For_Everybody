# json1.py
import json
# JSON represents data as nested lists and dictionaries
# first key is a string
# second key is an object, a two key value pair
# third key is an object, a one key value pair
data = '''{
"name" : "Chuck",
"phone" : {
  "type":"intl",
  "number":" +1 734 303 4456"
  },
  "email":{
    "hide":"yes"
	}
}'''
# no attributes, you create type

# start here, we deserialize it
# load from string data
info = json.loads(data)
# what you get back is a dictionary
print 'Name:', info["name"]
# sub twice 
print 'Hide:', info["email"]["hide"]
# Name: Chuck
# Hide: yes




# json2.py
# a list of dictionaries
import json
input = '''[
  {"id" : "001",
   "x" : "2",
   "name" : "Chuck"
   },
   {"id" : "009",
    "x" : "7",
	"name" : "Chuck"
	}
]'''

# get back a list
info = json.loads(input)
print 'User count:', len(info)
# loop through the list
for item in info: 
    print 'Name', item['name']
	print 'Id', item['id']
	print 'Attribute', item['x']




#geojson.py	
import urllib
import json
serviceurl = 'http://maps.googleapis.com/maps/apigeocode/json?'

while True:
    address = raw_input('Enter location:')
	if len(address) < 1: break
    
	# encode this address value that the user typed in a way
	# that's legal to be put on to a URL
	url = serviceurl + urllib.urlencode({'sensor':'false',
	    'address': address})
	print 'Retrieving',url
	uh = urllib.urlopen(url)
	data = uh.read()
	print 'Retrieved',len(data),'characters'
	
	try: js = json.loads(str(data))
	except: js = None
	# check the status
	if 'status' not in js or js['status'] ! = 'OK':
	    print '====Failure To Retrieve===='
		print data
		continue
	# dump as a string
	# pretty priting
	print json.dumps(js,indent = 4)
	
	# dictionary-list-dictionary-dictionary
	lat = js["results"][0]["geometry"]["location"]["lat"]
	lng = js["results"][0][geometry]["location"]["lng"]
	print 'lat',lat,'lng',lng
	location = js["result"][0]['formated_address']
	print location
	
	
	
# API Security and Rate Limiting
# twitter1.py
import urllib
from twurl import augment

print '*Calling Twitter...'
url = augment('http://api.twitter.com/1.1/statuses/user_timeline.json',
	    {'screen_name':'drchuck','count':'2'})
print url
connection = urllib.urlopen(url)
# get the headers of the http request and body
data = connection.read()
print data
# get a dictionary of the headers
# x-rate-limit-reset,x-rate-limit-remaining
headers = connection.info().dict
print headers



# twitter2.py
import urllib
import twurl
import json
TWITTER_URL = 'http://api.twitter.com/1.1/friends/list.json'
while True:
    print ''
	acct = raw_input('Enter Twitter Account:')
	if (len(acct) < 1) : break
	url = twurl.augment(TWITTER_URL,
	      {'screen_name':acct,'ccount':'5'})
    # print the augmented url
	print 'Retrieving',url
	conneciton = urllib.urlopen(url)
	data = connection.read()
	headers = connection.info().dict
	print 'Remaining',headers['x-rate-limit-remaining']
	# deserialize the body in JSON, give back an array of entries in friend list
	js = json.loads(data)
	print json.dumps(js,indent = 4)
	for u in js['users']:
	    print u['screen_name']
		s = u['status']['text']
		print ' ',s[.50]