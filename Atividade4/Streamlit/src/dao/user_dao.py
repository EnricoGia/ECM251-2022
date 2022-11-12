# Enrico Giannobile 19.00610-0

import sqlite3
import streamlit as st
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
        self.conn = sqlite3.connect('databases/sqlite.db', check_same_thread = False)

    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Users;
        """)
        results = []
        for result in self.cursor.fetchall():
            results.append(User(name=result[1], email=result[2], password=result[3]))
        self.cursor.close()
        return results

    def register_login(self, name, email, password, cpf):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
                INSERT INTO Users (name, email, password, cpf)
                VALUES(?,?,?,?);
            """, (name, email, password, cpf))
            self.conn.commit()
            self.cursor.close()
            st.success("# Login registrado")

        except Exception:
            st.warning("# CPF ou Email já registrado!")


    
    def get_all_info(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Users;
        """)
        results = []
        for result in self.cursor.fetchall():
            results.append(str(result[0]) + " " + result[1] + " " + result[2] + " " + result[3] + " " + result[4] + " ")
        self.cursor.close()
        return results
    
    def change_profile(self, email, password, email_now):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Users SET 
                email = '{email}',
                password = '{password}'
                WHERE email = '{email_now}' 
            """)
            self.cursor.close()
            st.markdown("Informações atualizadas")
            return True
        except Exception:
            st.markdown("Email já utilizado")
            return False
        


    
    