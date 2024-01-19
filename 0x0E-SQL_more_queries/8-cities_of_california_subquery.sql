-- list all the cities of California in the database hbtn_0d_usa
SELECT id, name FROM citites WHERE state_id = (SELECT id FROM states WHERE name = "Clifornia") ORDER BY id;
