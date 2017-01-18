def assignment():
  # Use the file name mbox-short.txt as the file name
  fname = raw_input("Enter file name: ")
  fh = open(fname)
  # look for lines of the form
  for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    print line
  print "Done"
  # count the lines
  for line in fn:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = 0
    count = count + 1
  print "Line count: ", count
