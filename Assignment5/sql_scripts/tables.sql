CREATE DATABASE SandwichMaker4;
CREATE TABLE IF NOT EXISTS resources (
id int NOT NULL AUTO_INCREMENT,
item varchar(50) NOT NULL,
amount int NOT NULL,
PRIMARY KEY (id)
);