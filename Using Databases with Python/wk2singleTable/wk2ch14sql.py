''' SQL depends on the data being pretty
Python on the other hand can handle unstructured rought data
Therefore, Python + SQL is a powerful combination
Python cleans up the data and SQL stores and retrieves data
CRUD: Create, Read(Retrieve), Upate, Delete
database administrator
application developer
Common Database Systems:
1. Oracle
2. MySql: purchased by Oracle, open source, for online web sites
3. SqlServer, Microsoft
SQLite, Postgress
''' 
#emaildb.py
import sqlite3
conn = sqlite3.connect('emaildb.sqlite')
# cursor object
cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS Counts''')
# create a table called counts
cur.execute('''CREATE TABLE Counts(email TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if (len(fname) < 1): 
    fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    emails = pieces[1]
    print emails
    # we do parameter substitution here to avoid SQL injection
    # ? is a place holder,(email,) is a tuple
    cur.execute('SELECT count FROM Counts WHERE email=?', (emails,))
    # just like .get()
    try: 
        count = cur.fetchone()[0]
        cur.execute('UPDATE Counts SET count=count+1 WHERE email=?',(emails,))
    except:
        cur.execute('''INSERT INTO Counts (email,count) VALUES (?, 1)''', (emails,))
    conn.commit()
#desceding and top 10
sqlstr= 'SELECT email,count FROM Counts ORDER BY count DESC LIMIT 10'

print 
print "Count:" 
for row in cur.execute(sqlstr):
    print str(row[0]),str(row[1])
   
cur.close()
    
