-- Creating hbnb_test_db database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Creating or updating hbnb_test user and setting password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Using the hbnb_test_db database
USE hbnb_test_db;

-- Granting privileges to hbnb_test user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flushing privileges
FLUSH PRIVILEGES;
