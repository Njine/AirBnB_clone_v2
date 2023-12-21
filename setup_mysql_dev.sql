-- Creating hbnb_dev_db database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Creating or updating hbnb_dev user and setting password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Using the hbnb_dev_db database
USE hbnb_dev_db;

-- Granting privileges to hbnb_dev user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flushing privileges
FLUSH PRIVILEGES;
