# use beautifulsoup to find all the links on a web page
import urllib
from BeautifulSoup import  *

url = raw_input("Enter - ")

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# retrieve a list of the anchor tags
# each tag is like a dictrionary of HTML attributes
# soup is collection of parsed HTML data

tags = soup('a')
# an anchor tag is like <a xxx> xxx</a>, no<p>,no<b>
for tag in tags:
    # TAG: <a href="http://www.dr-chuck.com/page2.htm">Second Page</a>
    print 'TAG:',tag
	# URL: http://www.dr-chuck.com/page2.htm
    print 'URL:',tag.get('href', None)
	# Contents:Second Page
    print 'Contents:',tag.contents[0]
	# Attrs: [(u'href', u'http://www.dr-chuck.com/page2.htm')]
    print 'Attrs:',tag.attrs