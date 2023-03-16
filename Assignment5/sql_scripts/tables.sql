CREATE DATABASE SandwichMaker4;
CREATE TABLE IF NOT EXISTS resources (
id int NOT NULL AUTO_INCREMENT,
item varchar(50) NOT NULL,
amount int NOT NULL,
PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS sandwich (
id int NOT NULL AUTO_INCREMENT,
sandwich_size varchar(50) NOT NULL,
price decimal(5,2) NOT NULL,
PRIMARY KEY (id)
);