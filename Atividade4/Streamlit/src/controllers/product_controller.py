# Enrico Giannobile 19.00610-0

from src.models.product import Product
from src.dao.product_dao import ProductDAO
import streamlit as st

class ProductController():
    def __init__(self):
        self._products = ProductDAO.get_instance().get_all()

        for product in self._products: ### RETIRAR
            print(product)

    def get_product(self,index):
        return self._products[index]
    
    def get_products(self):
        return self._products
    
    def register_product(self, name, price, url):
        if(name and price and url):
            ProductDAO.get_instance().register_product(name, price, url)
        else:
            pass
        

