# xml1.py
import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>'''

# take the string and parse into the element tree library
# like deserializing
# .fromstring() method get back an obejct, name it "tree"
tree = ET.fromstring(data)
# call the find method on the tree object, find the name tags
# .text we like text of that thing
print 'Name:',tree.find('name').text
# find the email tags, get attribute hide = "yes"
print 'Attr:',tree.find('email').get('hide')

import xml.etree.ElementTree as ET

# xml2.py
# plural name for the tage, singular name for the each of thing 
# users and user
input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
            </user>
        </users>
</stuff>'''


stuff = ET.fromstring(input)
# users/user is the path, returns a list of users
lst = stuff.findall('users/user')
print 'User count:', len(lst)

# find attributes and texts
for item in lst:
    print 'Name', item.find('name').text
    print 'Id', item.find('id').text
    print 'Attribute', item.get("x")
