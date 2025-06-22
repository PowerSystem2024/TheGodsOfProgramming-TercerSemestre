-- Create the database if it does not already exist
CREATE DATABASE IF NOT EXISTS estudiantes;

-- Use the newly created or existing database
USE estudiantes;

-- Create the estudiantes2022 table
CREATE TABLE IF NOT EXISTS estudiantes2022 (
    idestudiantes2022 INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(45) NULL,
    apellido VARCHAR(45) NULL,
    telefono VARCHAR(45) NULL,
    email VARCHAR(45) NULL,
    PRIMARY KEY (idestudiantes2022)
) ENGINE=InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;