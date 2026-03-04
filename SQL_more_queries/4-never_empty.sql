-- Tasks 4. ID can't be null
-- Script that creates the table id_not_null on the MySQL server
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
