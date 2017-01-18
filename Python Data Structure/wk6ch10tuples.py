x = ('Glenn','Sally','Joseph')
print x[2]
y = (1,9,2)
print y
print max(y)

for iter in y:
    print iter
# immutable 
# no sort,append,reverse functions

l = list()
dir(l)
t = tuple()
dir(t)

# we can put a tuple on the left hand side
(x,y)=(4,'fred')
print y
# we can omit the parenthesis
(a,b)=(99,98)
print a
a,b = (99,98)
print a

# tuples and dictionaries
# the .items() method in dic returns a list of (key,value) tuples
d = dict()
d['csev']=2
d['cwen']=4
for (k,v) in d.items():
    print k,v
# k=csev,v=2;k=cwen,v=4
tups = d.items()
print tups

# tuples are comparable
# if the first items are equal, goes on to the next
# till it finds elements that differ
(0,1,2)<(5,1,2)
(0,1,2000)<(0,3,4)
('Jones','Sally')<('Jones','Fred')
('Jones','Sally')>('Adams','Sam')

# sorting lists of tuples
# get a sorted version of dictionary by sorting keys
d = {'a':10,'b':1,'c':22}
t = d.items()
t.sort()
# or use sorted()d = {'a':10,'b':1,'c':22}
d = {'a':10,'b':1,'c':22}
t = d.items()
t = sorted(d.items())
t
for k,v in sorted(d.items())
print k,v

# sort by values instead of key
c = {'a':10,'b':1,'c':22}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))
# [(10,'a'),(22,'c'),(1,'b')]
# temporary data, value first, key second
print tmp
# sort in a reversed order
tmp.sort(reverse=True)
print tmp
# [(2,'c'),(10,'a'),(1,'b')]

# top 10 most common words
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
	# get the word-count pairs
	for word in words:
	    counts[word]=counts.get(word,0)+1
	
	lst = list()
	for key,val in counts.items():
	    lst.append((val,key))
	
	lst.sort(reverse=True)
	
	for val,key in lst[:10]
	    print key,val

#even shorter version
c = {'a':10,'b':1,'c':22}
# create the reverse list
print sorted([(v,k) for k,v in c.items()])