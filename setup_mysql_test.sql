-- Creates the test database hbnb_test_db if it does not already exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Creates the user 'hbnb_test'@'localhost' with the specified password if it does not already exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grants all privileges on the hbnb_test_db database to the user 'hbnb_test'
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grants SELECT privilege on the performance_schema database to 'hbnb_test'
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Applies the changes immediately
FLUSH PRIVILEGES;

