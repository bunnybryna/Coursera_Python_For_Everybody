-- add a junction table between
-- junction table has two foreign keys but not primary keys
CREATE TABLE User(
    id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name        TEXT,
    email       TEXT
)

CREATE TABLE Course(
    id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title       TEXT
)
-- Primary key is a combination, unique 
CREATE TABLE Member(
    user_id     INTEGER,
    course_id   INTEGER,
        role    INTEGER,
    PRIMARY KEY (user_id, course_id)
)

INSERT INTO User (name, email) VALUES ('Jane','jane@tsugi.org');
INSERT INTO User (name, email) values ('Sue', 'sue@tsugi.org');
INSERT INTO User (name, email) VALUES ('Ed', 'ed@tsugi.org');
INSERT INTO Course (title) VALUES ('Python');
INSERT INTO Course (title) VALUES ('SQL');
INSERT INTO Course (title) VALUES ('PHP');

-- Insert membership, role 1 is instructor, 0 means student
INSERT INTO Member (user_id, course_id, role) VALUES (1,1,1);
INSERT INTO Member (user_id, course_id, role) VALUES (2,1,0);
INSERT INTO Member (user_id, course_id, role) VALUES (3,1,0);

INSERT INTO Member (user_id, course_id, role) VALUES (1,2,0);
INSERT INTO Member (user_id, course_id, role) VALUES (2,2,1);

INSERT INTO Member (user_id, course_id, role) VALUES (2,3,1);
INSERT INTO Member (user_id, course_id, role) VALUES (3,3,0);

-- ORDER BY, title is the most important thing, then role (descending)and name last
SELECT User.name, Member.role, Course.title From User JOIN Member JOIN Course
ON Member.user_id = User.id AND MEMBER.course_id = Course.id
ORDER BY Course.title, Member.role DESC, User.name