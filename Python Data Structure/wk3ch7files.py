

stuff = "Hello\nWorld"
print stuff
print len(stuff)

xfile = open("test.txt")
for cheese in xfile:
	print cheese

# read the file as a sequence of strings(lines)
fhand = open("test.txt")
# you cann't print len(fhand), fhand is not a string
# count is a mnemonic variable
count = 0
for line in fhand:
	count = count + 1
print "Line Count:", count

# we can read the whole ile into a single string
fhand = open("test.txt")
inp = fhand.read()
print len(inp)
# we need the first 20 characters but not including 20
print inp[:20]

fhand = open("test.txt")
for line in fhand:
	if line.startswith("From:"):
		# print statement adds a newline to each line
		print line
		
fhand = open("test.txt")
for line in fhand:
	line = line.rstrip()
	# wipe out the blank lines
	if line.startswith("From:"):
		print line

# another way to achieve the same result
fhand = open("test.txt")
for line in fhand:
	line = line.rstrip()
	# skip uninteresting lines
	if not line.startswith("From:"):
		continue
	# process intersteing line
	print line

fhand = open("test.txt")
for line in fhand:
	line = line.rstrip()
	# look for a string in a line
	if not "@uct.ac.za" in line:
		continue
	print line

fname = raw_input("Enter the file name:")
try:
	fhand = open(fname)
except:
	print "File cannot be opened:", fname
	exit()
count = 0
for line in fhand:
	if line.startswith("Subject:"):
		count = count + 1
print "There were", count, "subject lines in",fname

