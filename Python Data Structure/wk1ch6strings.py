# indefinite loop using while 
fruit = "banana"
index = 0
while index < len(fruit):
	letter = fruit[index]
	print index, letter
	index = index + 1

# definte loop using for
# for loop is doing looking up and advancing the index
fruit = "banana"
for letter in fruit:
    print letter

word = "banana"
count = 0
for letter in word:
	if letter == "a":
		count = count + 1
print count

# slicing strings
# [x:y],y means up to but not including
# if y beyond the end of the string, it stops at the end
s = "Monty Python"
print s[0:4]
print s[6:7]
print s[6:20]
# Mont,P,Python
# if we leave off x, beginning;y,end
print s[:2]
print s[8:]
print s[:]
# Mo,thon,Monty Python

# using in as an operator
# returns True or Flase, can be used in if
fruit = "banana"
"n" in fruit
"m" in fruit
"nan" in fruit
if "a" in fruit:
	print "Found it!"

# string comparison
if word == "banana":
	print "All right, banana."

if word < "banana":
	print "Your word," + word + " ,comes before banana."
# else word > "banana":
	#print "Your word," + word + " ,comes after banana."
else:
	print "All right, bananas."

# type()is asking the type of data, string, integer...

# built-in functions
# find funtion
fruit = "banana"
pos = fruit.find("na")
print pos
# replace function
greet = "Hello Bob"
nstr = greet.replace("Bob","Jane")
print nstr
# stripping whitespace
# left,right,left and right
greet = " Hello Bob "
print greet.lstrip()
print greet.rstrip()
print greet.strip()
# prefixes,returns True or False
line = "Please have a nice day"
line.startswith("Please")
line.startswith("p")

# parsing text
data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
atpos = data.find("@")
print atpos 
# .find(start,end)
sppos = data.find(" ",atpos)
print sppos
host = data[atpos+1:sppos]
print host