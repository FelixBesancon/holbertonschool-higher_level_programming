-- Tasks 16. Say my name
-- Script that lists all records of the table second_table
-- of the database hbtn_0c_0 in the MySQL server
SELECT name, score
FROM second_table
WHERE name IS NOT NULL AND name <> ''
ORDER BY score DESC;
