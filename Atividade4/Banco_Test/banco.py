"""

DROP TABLE Usuarios;

CREATE TABLE Usuarios(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nome TEXT NOT NULL,
      email TEXT NOT NULL UNIQUE,
      senha TEXT NOT NULL,
      cpf INTEGER NOT NULL UNIQUE
);

INSERT INTO Usuarios (nome, email, senha, cpf)
VALUES("Edx","Edx@gmail.com","12345","23412341");

SELECT * FROM Usuarios;

"""

