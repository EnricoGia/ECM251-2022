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
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Product(name = resultado[1], price = resultado[2], url = resultado[3]))
        self.cursor.close()
        return resultados
    
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
    
    def pegar_item(self,id):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Itens
            WHERE id = '{id}';
        """)
        item = None
        resultado =  self.cursor.fetchone()
        if resultado:
            item = Product(id=resultado[0], nome=resultado[1], preco=resultado[2])
        self.cursor.close()
        return item

    def atualizar_item(self,item):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Itens SET 
                nome = '{item.nome}',
                preco = {item.preco}
                WHERE id = '{item.id}' 
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True

    def deletar_item(self,id):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE FROM Itens
                Where id = '{id}'  
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True

    def search_all_for_name(self,nome):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Itens
            WHERE nome LIKE '{nome}%'; 
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Product(id=resultado[0], nome=resultado[1], preco=resultado[2]))
        self.cursor.close()
        return resultados