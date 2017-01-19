import urllib
import json

address = raw_input('Enter location: ')

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
key = "AIzaSyAYGzs1AQ8njOxaZLvz15t1wa1KmvEBeL4"
# encode this address value that the user typed in a way
# that's legal to be put on to a URL
# If you visit the URL with no parameters
# you get a list of all of the address values
url = serviceurl + urllib.urlencode({'sensor':'false', 'address':address,'key':key})
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

js = json.loads(str(data))
# pretty priting
print json.dumps(js, indent=4)

lat = js["results"][0]["geometry"]["location"]["lat"]
lng = js["results"][0]["geometry"]["location"]["lng"]
# find the place id
id = js["results"][0]["place_id"]
print 'lat',lat,'lng',lng,'id',id
location = js['results'][0]['formatted_address']
print location

location = str(lat)+','+str(lng)
#39.7391536,-104.9847034'

serviceurl = 'https://maps.googleapis.com/maps/api/elevation/json?'
key = "AIzaSyAYGzs1AQ8njOxaZLvz15t1wa1KmvEBeL4"

url = serviceurl + urllib.urlencode({'sensor':'false', 'locations':location,'key':key})
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

js = json.loads(str(data))
# pretty priting
print json.dumps(js, indent=4)

#lat = js["results"][0]["geometry"]["location"]["lat"]
#lng = js["results"][0]["geometry"]["location"]["lng"]
# find the place id
ele = js["results"][0]["elevation"]
print 'ele',ele