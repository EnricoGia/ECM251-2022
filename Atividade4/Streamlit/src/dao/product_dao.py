# Enrico Giannobile 19.00610-0

import sqlite3
from src.models.product import Product
class ProductDAO:
    
    _instance = None

    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = ProductDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db', check_same_thread = False)

    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Products;
        """)
        results = []
        for result in self.cursor.fetchall():
            results.append(Product(name = result[1], price = result[2], url = result[3]))
        self.cursor.close()
        return results
    
    def register_product(self, name, price, url):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
                INSERT INTO Products (name, price, url)
                VALUES(?,?,?);
            """, (name, price, url))
            self.conn.commit()
            self.cursor.close()
        except Exception:
            pass