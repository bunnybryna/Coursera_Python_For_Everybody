x = 2
x = x + 2
# the right-hand side of "=", x + 2 run first
print x
# variable is a memory location used to store a value
# "=" right side is an expression
x = 3.9 * x * (1-x)

x = 1 + 2 ** 3 / 4 * 5
# x = 1 + 8 / 4 * 5 = 1 + 2 * 5 = 1 + 10 = 11

eee = hello
type(eee)

# integer is implicitly converted to a float
print float(99/100)
print 1 + 2 * 3 float(3) / 4 - 5

# raw input function issues a prompt, waits and then takes whatever you enter and returns it
nam = raw_input("Who are you?")
print "Welcome", nam

inp = raw_input("Europe floor?")
usf = int(inp) + 1
print "US floor", usf