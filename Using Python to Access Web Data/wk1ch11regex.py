hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
	if line.find('From:')>=0
	    print line


# same thing in the regular expression
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
	if re.search('From:' line):
	    print line
		
# use re.search()like startswith()
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
	if line.startswith('From:'):
	# if re.search('^From:',line)
	    print line
# ^ means beginning of the line
# . means means any character		
# * means any number of time
#means any lines that starts with x
# it will find you x and :
^x.*:
# fine-tuning the match, we want x- and no space
# \S match any non-whitespace character
# + means one or more times
^x-\S+:
# at least one digit
[0-9]+

import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print y
# it will print ['2','19','42'],a Python list

# look for any uppercase vowels, + means one or more
y = re.findall('[AEIOU]+',x)
print y
# it will return an empty list

# greedy matching
import re
x = 'From: Using the : character'
# first character in the match is F
# last character in the match is :
y = re.findall('^F.+:',x)
print y
# it will return ['From: Using the :'] instead of ['From:']
# it will give you the largest possible string

# non-greedy matching
import re
x = 'From: Using the : character'
# ? means prefer the shorted string
y = re.findall('^F.+?:',x)
print y

# to find From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
y = re.findall('\S+@\S+',X)
print y		
# () is the start and end of what to extract
# () says after From and a blank, start the match
# even though From is part of the matching, () helps to extract the part we want
y = re.findall('From (\S+@\S+)',x)
print y

# the regex version of double split
import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# [^] means not, matches non-blank character
# From, space, any character, @ with non blank character
y = re.findall('@([^ ]*)',lin)
print y
# even cooler regex version
y = re.findall('^From .*@([^ ]*)',lin)

# spam confidence
import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand：
    line = line.rstrip()
	# select and extract all in one line
	# [0-9.] digit or period
	stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
	if len(stuff) ! = 1: continue
	num = float(stuff[0])
	numlist.append(num)

print 'Maximum:',max(numlist)

x = 'We just received $10.00 for cookies.'
# \$ means real $
y = re.findall('\$[0-9.]+',x)
print y
