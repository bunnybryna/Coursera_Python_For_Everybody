--comment here: 
/*1.Do not replicate data
2. use integers for keys and add key(id) to each table



where to start: think about what is the most essential to this application?
 what are real things? what are attibutes of things?
 Track: most essential, Rating, Len, Count, are all attributes
 Track belongs to Album: 
 Album belongs to Artist:  
 Track belongs to Genre
 primary key: generally an integer auto-increment field, ending point of the arrow
 foreign key: generally an integer key pointing to a row in another table, starting point of the arrow
 logical key: unique thing that we use to look up this row from outside world
 (WHERE clause)
 first create the end then the start
 work from outward in: Artist => Genre => Album => Track
 */
CREATE TABLE Genre(
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT
)        
-- artist_id is a foreign key
-- title is the logical key
CREATE TABLE Album(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT
)
-- album_id and genre_id are foreign keys
-- title is the logical key
CREATE TABLE Track(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
)

-- now insert data to the table, not specify the id field
insert into Artist(name) values('Led Zepplin');
insert into Artist(name) values('AC/DC')

insert into Genre(name) values('Rock');
insert into Genre(name) values('Metal')

insert into Album(title, artist_id) values('Who Made Who',2);
insert into Album(title, artist_id) values('IV',1)

-- it's OK to have replication as long as they are numbers
insert into Track(title, rating, len, count, album_id, genre_id)
    values('Black Dog', 5, 297, 0, 2, 1)
insert into Track(title, rating, len, count, album_id, genre_id)
    values('Stairway', 5, 482, 0, 2, 1)
insert into Track(title, rating, len, count, album_id, genre_id)
    values('About to Rock', 5, 313, 0, 1, 2)
insert into Track(title, rating, len, count, album_id, genre_id)
    values('Who Made Who', 5, 207, 0, 1, 2)
    
-- JOIN: select data from more than 1 table
-- Table_name.field_name
-- on clause states how the tables are linked starting_point = ending_point
-- select logical keys
select Album.title, Artist.name from Album join Artist on Album.artist_id = Artist.id
-- now look at all data that's participating in the connection between two rows
select Album.title, Album.artist_id, Artist.id, Artist.name from Album join Artist on Album.artist_id = Artist.id
-- without on clause, it means all combinations
-- indentations or lines don't affect the code
select Track.title, Album.title from Track join Album on Track.album_id = Album.id
select Track.title, Genre.name from Track join Genre on Track.genre_id = Genre.id

select Track.title, Artist.name, Album.title, Genre.name from 
Track join Genre join Album join Artist on Track.genre_id = Genre.id and
Track.album_id = Album.id and Album.artist_id = Artist.id