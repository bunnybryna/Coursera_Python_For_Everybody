import json
import sqlite3

conn = sqlite3.connect('rosterdb2.sqlite')
cur = conn.cursor()


cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')
#  PRIMARY KEY is a combination (user_id, course_id)
fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'roster_data.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:

    names = entry[0];
    titles = entry[1];
    roles = entry[2];

    print names, titles, roles

    cur.execute('''INSERT OR IGNORE INTO User (name) 
        VALUES ( ? )''', ( names, ) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (names, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title) 
        VALUES ( ? )''', ( titles, ) )
    cur.execute('SELECT id FROM Course WHERE title = ? ', (titles, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''', 
        ( user_id, course_id, roles ) )

conn.commit()