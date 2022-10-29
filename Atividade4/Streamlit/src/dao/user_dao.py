import sqlite3
from src.models.user import User
class UserDAO:
    
    _instance = None

    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = UserDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('databases/sqlite_users.db', check_same_thread = False)

    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Users;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(User(name=resultado[1], email=resultado[2], password=resultado[3]))
        self.cursor.close()
        return resultados

    def registrar_login(self, name, email, password, cpf):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Users (name, email, password, cpf)
            VALUES(?,?,?,?);
        """, (name, email, password, cpf))
        self.conn.commit()
        self.cursor.close()
    
    def get_all_info(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Users;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(str(resultado[0]) + " " + resultado[1] + " " + resultado[2] + " " + resultado[3] + " " + resultado[4] + " ")
        self.cursor.close()
        return resultados

    
    