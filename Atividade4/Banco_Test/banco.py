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



CREATE TABLE Products(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      price FLOAT NOT NULL,
      url TEXT NOT NULL
);

INSERT INTO Products (name, price, url)
VALUES("Elden Ring",199.90, "https://image.api.playstation.com/vulcan/ap/rnd/202110/2000/aGhopp3MHppi7kooGE2Dtt8C.png"),
("Dark Souls (PC)", 99.90 ,"https://upload.wikimedia.org/wikipedia/pt/7/7c/Dark_Souls_1_capa.png");

SELECT * FROM Products;

"""

