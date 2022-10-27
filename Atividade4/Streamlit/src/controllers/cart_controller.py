# Enrico Giannobile 19.00610-0

from src.models.cart import Cart
class CartController():
    def __init__(self):
        self._cart = Cart()

    def add_product(self,product,quantity):
        
        for i in range(len(self.get_cart().get_products())):
            if self.get_cart().get_products()[i][0].get_name() == product.get_name():
                self.get_cart().get_products()[i][1] += quantity
                return

        self.get_cart().get_products().append([product,quantity])
       

    
    def calculate_price(self,product,quantity):
        return (product.get_price()*quantity)

    def get_cart(self):
        return self._cart

    def total_price(self):
        products = self.get_cart().get_products()
        total = 0
        for i in products:
           total += (i[0].get_price()*i[1])
        return total
