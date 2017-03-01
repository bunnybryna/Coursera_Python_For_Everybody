# import the library to talk to sql database
import sqlite3
# store that databse in the file emaildb.sqlite
conn = sqlite3.connect('emaildb.sqlite')
# cur variable now has the cursor object, just like socket
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    emails = pieces[1]
    print emails
    # (emails,) is a tuple, the first thing in the tupe is what will replace the question mark(note that email is the name of the column, emails is the actual email sliced from fh)  
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (emails, ))
    # fetchone() brings back one row available, think of fin.get(next) in c
    # second way to do it line 26-32
    ''' try:
            count = cur.fetchone()[0]
            cur.execute('UPDATE Counts SET count=count+1 WHERE email=?',(emails,))
        execpt:
            cur.execute('INSERT INTO Counts (email,count) VALUES (?,1)',(emails,))'''
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (email, count) VALUES ( ?, 1 )', ( emails, ) )
    else : 
        cur.execute('UPDATE Counts SET count=count+1 WHERE email = ?', 
            (emails, ))
    # This statement commits outstanding changes to disk each 
    # time through the loop - the program can be made faster 
    # by moving the commit so it runs only after the loop completes
conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

print
print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()

