CREATE TABLE entries(
  id INT(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
  username VARCHAR(100) NOT NULL,
  author VARCHAR(100) NOT NULL,
  title VARCHAR(100) NOT NULL,
  journal_entry VARCHAR(500) NOT NULL
);


CREATE TABLE users(
  id INT(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
  username VARCHAR(100) NOT NULL,
  email VARCHAR(320) NOT NULL,
  password VARCHAR(100) NOT NULL,
  register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE (USERNAME)
);
