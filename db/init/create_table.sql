use test;

CREATE [TEMPORARY] TABLE [IF NOT EXISTS] users (
    name VARCHAR(10),
    age int
)DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

CREATE TABLE board (
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	title VARCHAR(30),
    name VARCHAR(10),
    description VARCHAR(1000),
    created_time datetime
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;
 
