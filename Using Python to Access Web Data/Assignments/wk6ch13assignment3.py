import urllib
import json

# for display purpose, remove the while True and try and except part
address = raw_input('Enter location: ')
serviceurl = 'https://maps.googleapis.com/maps/api/elevation/json?'
# encode this address value that the user typed in a way
# that's legal to be put on to a URL
# If you visit the URL with no parameters
# you get a list of all of the address values
url = serviceurl + urllib.urlencode({'sensor':'false', 'address':address})
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

js = json.loads(str(data))
# pretty priting
print json.dumps(js, indent=4)

#lat = js["results"][0]["geometry"]["location"]["lat"]
#lng = js["results"][0]["geometry"]["location"]["lng"]
ele = js["results"][0]["elevation"]
# find the place id
print "elevation", ele
