-- Creates the database hbnb_dev_db if it does not already exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creates the user 'hbnb_dev'@'localhost' with the specified password if it does not already exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grants all privileges on the hbnb_dev_db database to the user 'hbnb_dev'
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grants SELECT privilege on the performance_schema database to 'hbnb_dev'
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Applies the changes immediately
FLUSH PRIVILEGES;

