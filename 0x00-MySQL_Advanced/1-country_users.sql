-- SQL script that creates users table with specific constraints
-- Creates a table named users with id, email, name, and country fields
-- The country field is an ENUM with values 'US', 'CO', and 'TN'

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
