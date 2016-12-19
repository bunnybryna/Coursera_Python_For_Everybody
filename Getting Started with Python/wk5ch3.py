# conditional execution (flow diagrams)
x = 5
if x < 10:
    print 'Smaller'
# comparison operations
if x > 20:
    print 'Bigger'
# same as if x > 20: print 'Bigger'
print 'Finis'

x = 5
print 'Before 5'
# one way decision
# Python uses indentation as syntactically significant
# think indentation, two lines lining up run sequetially
if x == 5:
    print 'Is 5'
	print 'Is still 5'
	print 'Third 5'
# pull out means the block of conditional executed code is finished
print 'Afterwards 5'

for i in range(5):
    print i 
	if i > 2:
	    print 'Bigger than 2'
	print 'Done with i',i
	
# two way decision
x = 4
if x > 2:
    print 'Bigger'
else:
    print 'Smaller'
print 'All done'

# multi-way decision
# only one runs, order does matter
if x < 2:
    print 'Small'
elif x < 10:
    print 'Medium'
else:
    print 'Large'
print 'All done'

#  No else
x = 15
if x < 2:
    print 'Small'
elif x < 10:
    print 'Medium'
# you can skip them both
print 'All done'

# you can have many elifs as you want
if x < 2:
    print 'Small'
elif x < 10:
    print 'Medium'
elif x < 20:
    print 'Big'
elif x < 40:
    print 'Large'
elif x < 100:
    print 'Huge'
else:
    print 'Ginormous'

if x < 2:
    print 'Below 2'
elif x >= 2:
    print 'Two or more'
# this line will never print
else:
    print 'Something else'

if x < 2:
    print 'Below 2'
elif x < 20:
    print 'Below 20'
# this line will never print 
elif x < 10:
    print 'Below 10'
else:
    print 'Something else'

# try and except
astr = 'Hello Bob'
try:
    istr = int(astr)
# if it fails,we will have the alternate substitue code 
except:
    istr = -1
print 'First',istr

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print 'Second',istr

# multiple lines under try:
# it runs until one dies
astr = 'Bob'
try:
    # this runs
    print 'Hello'
	istr = int(astr)
	# this will never run
	print 'There'
except:
    istr = -1

# errors are anticipated
rawstr = raw_input('Enter a number')
try:
    ival = int(rawstr)
except:
    ival = -1
if ival > 10:
    print 'Nice work'
else:
    print 'Not a number'