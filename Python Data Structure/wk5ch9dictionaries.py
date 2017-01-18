# diffrence between list and dictionary
# list, a linear collection of values that stay in order
# dictionary, a bag of values, each with its own labels
purse = dict()
purse['money']=12
purse['candy']=3
# candy is the key,3 is the value
purse['tissue']=75
print purse
print purse['candy']
# can do calculation
purse['candy'] = purse['candy'] + 2
print purse

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
# dict doesn't keep order
print ddd
ddd['age'] = 23
print ddd

# solve the counting problem
ccc = dict()
ccc['csev']=1
ccc['cwen']=1
print ccc
ccc['cwen']=ccc['cwen']+1
print ccc
# see if a key is in the dict
print 'csev' in ccc

counts = dict()
# name is a list
names = ['csev','cwen','csev','zqian','cwen']
# in for loop,name = 'csev','cwen','cwen'...they are the keys
for name in names:
    if name not in counts:
	    counts[name]=1
    else:
	    counts[name]=counts[name]+1
# {'csev':2,'zqian':1,'cwen':2}
print counts

# to check if a key is already in a dict
if name in counts:
    print counts[name]
else:
    print 0
# or, use get method that takes 2 parameters
# name is the name of the key
# 0 is the a value to give back if this doesn't exist,default  
print counts.get(name,0)

# simplified counting with get()
counts = dict()
names = ['csev','cwen','csev','zqian','cwen']
for name in names:
    counts[name]=counts.get(name,0)+1
print counts

# counting pattern
counts = dict()
print 'Enter a line of text:'
line = raw_input

words = line.split()
print 'Words:',words
print 'Counting...'
for word in words:
    counts[word]=counts.get(word,0)+1
print 'Counts',counts

# definite loops to go through all the values
counts = {'chuck':1,'fred':42,'jan':100}
for key in counts:
    print key,counts[key]

# you can get a list of keys, values or items(both)
jjj = {'chuck':1,'fred':42,'jan':100}
print list(jjj)
# same thing as list(jjj)
print jjj.keys()
# notice that these two orders correspond
print jjj.values()
# python calls the list tuples
print jjj.items()

# Python has two iteration variables
jjj = {'chuck':1,'fred':42,'jan':100}
# aaa,bbb are moving in pairs
# aaa takes on the value of the key
# bbb takes on the value of the value
for aaa,bbb in jjj.items():
   print aaa,bbb
 
name = raw_input('Enter file:')
handle = open(name,'r')
text = handle.read()
# create a list of words in that file
words = text.split()

counts = dict()
# have a full dict with the word:count
for word in words:
    counts[word]=counts.get(word,0)+1
#  None is frequently used to represent the absence of a value
bigcount = None
bigword = None
# go through the key/value pairs
for word,count in counts.items():
    if bigcount is None or count > bigcount:
	    bigword = word
		bigcount = count
	print bigword,bigcount
