"""


CREATE TABLE Users(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      email TEXT NOT NULL UNIQUE,
      password TEXT NOT NULL,
      cpf TEXT NOT NULL UNIQUE
);

INSERT INTO Users (name, email, password, cpf)
VALUES("Edx","Edx@gmail.com","12345","23412341");

SELECT * FROM Users;





"""

