friends = ['Joseph','Glenn','Sally']
for friend in friends:
    print 'Happy New Year:', friend
print 'Done!'
# construct an index loop using for and an integer iterator
for i in range(len(friends)):
    friend = friends[i]
	print 'Happy New Year:', friend

# lists are mutable,use the index to change the element
# cannot do this to a string
# once a string is made, it's unchangable or immutable
lotto = [2,14,26,41,63]
print lotto
lotto[2] = 28
print lotto

# len() tells the number of elements of a sequence
x = [1,2,'joe',99]
print len(x)

# create a new list by adding two existing lists together
a = [1,2,3]
b = [4,5,6]
c = a + b
print c
# slice lists
t = [9,41,12,3,74,15]
# up to but not include
t[1:3]
t[:4]
t[3:]
t[:]

# use append method to add elements 
# start with an empty list, new elements are added at the end
stuff = list()
stuff.append('book')
stuff.append(99)
print stuff
stuff.append('cookie')
print stuff

# can reponse with True or False
some = [1,9,21,10,16]
9 in some
12 in some
20 not in some

# sort() in alphabetical order
friends = ['Joseph','Glenn','Sally']
friends.sort()
print friends
print friends[1]

# built-in functions 
nums = [3,41,12,9,74,15]
print len(nums)
print max(nums)
print min(nums)
print sum(nums)
print sum(nums)/len(nums)

# this one is more like calculator
total = 0
count = 0
while True:
    inp = raw_input("Enter a number:")
	if inp == 'done': break
	value = float(inp)
	total = total + value
	count = count + 1

average = total/ count
print 'Average:', average

# the other way,but this one stores the numbers
# if there're a lot of number, it might take more memory
# other than that, this one is more powerful pattern for you to do sth. with the list
numlist = list()
while True:
    inp = raw_input('Enter a number:')
	if inp == 'done': break
	value = float(inp)
	numlist.append(value)
	
average = sum(numlist)/len(numlist)
print 'Average:',average

# split breaks a string into parts produces a list 
abc = 'With three words'
stuff = abc.split()
print stuff
print len(stuff)
print stuff[0]
for w in stuff:
    print w

line = 'A lot                   of spaces'
etc = line.split()
# will not print spaces
print etc
line = 'first;second;third'
thing = line.split()
print thing
print len(thing)
# split on a charater, eg, we pass semicolon as a parameter
# it will split based on semicolons
thing = line.split(';')
print thing
print len(thing)

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
	if not line.startswith('From'): continue
	words = line.split()
	print words[2]
	
# double split patten
words = line.split()
email = words[1]
pieces = email.split('@')
print pieces[1]

