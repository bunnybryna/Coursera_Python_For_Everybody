CREATE TABLE Ages(
    name VARCHAR(128),
    age INTEGER
)
DELETE FROM Ages;
INSERT INTO Ages(name, age) VALUES('Blaise',31);
INSERT INTO Ages(name, age) VALUES('Evangeline',39);
INSERT INTO Ages(name, age) VALUES('Rianna', 28);
INSERT INTO Ages(name, age) VALUES('Lukmaan',34);
INSERT INTO Ages(name, age) VALUES('Darrell',23);

SELECT hex(name || age) AS X FROM Ages ORDER BY X
