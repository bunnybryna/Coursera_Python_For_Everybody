#infinite loop and zero trip loop
n = 0 
while n > 0:
    print 'Lather'
	print 'Rinse'
print 'Dry off!'

# use break to control the execution
while True:
    line = raw_input('>')
	if line = 'done':
	# break means stop the loop
	    break
    print line
print 'Done'

# use continue to stop this iteration and advance to next one
while True:
    line = raw_input('>')
	if line[0] == '#':
	    continue
	# continue ignores the next two lines
	if line == 'done':
	    break
    print line
print 'Done'

friends = ['Joseph','Glenn','Sally']
for friend in friends:
    print 'Happy New Year:', friend
print 'Done!'

largest_so_far = -1
print 'Before',largest_so_far
for num in [9,41,12,3,74,15]:
    # num < smallest_so_far
	# remember to change the starting point -1
    if num > largest_so_far:
	    largest_so_far = num
	print largest_so_far,num
print 'After',largest_so_far

smallest = None
print 'Before'
for value in [9,41,12,3,74,15]:
    # None is like a placeholder
	# remember "is None" not "== None"
	# is can be used in logical expressions
	# is stronger than ==
    # this gonna happen at the first time
    if smallest is None:
	    smallest = value
	elif value < smallest:
	    smallest = value 
	print smallest, value

# counting in a loop:
count = 0
print 'Before',count
for thing in [9,41,12,3,74,15]:
    count = count + 1
	print count,thing
print 'After',count

# summing in a loop:
sum = 0
print 'Before',sum
for thing in [9,41,12,3,74,15]:
    sum = sum + thing
	print sum, thing
print 'After',sum

# finding the average in a loop
count = 0
sum = 0
print 'Before', count, sum
for value in [9,41,12,3,74,15]:
    count = count + 1
	sum = sum + value
	print count, sum, value
print 'After',count,sum,sum/count

# filtering in a loop
print 'Before'
for value in [9,41,12,3,74,15]:
    if value > 20:
	    print 'Large number,value
print 'After'

# using a Boolean variable
found = False
print 'Before',found
for value in [9,41,12,3,74,15]:
    if value == 3:
	    found = True
		break
	print found,value
print 'After',found

	