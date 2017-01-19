import re
file = raw_input("Enter file name:")
hand = open(file)
pile = 0
for line in hand:
    line = line.rstrip()
    num = re.findall('[0-9]+',line)
    integer = int(num)
    pile = pile + integer
print pile
