from src.models.cart import Cart
class CartController():
    def __init__(self):
        self._cart = Cart()

    def add_product(self,product,quantity):
        
        for i in range(len(self._cart._products)-1):
            if self._cart._products[i][0] == product:
                self._cart._products[i][1] += quantity
                return
        self._cart._products.append([product,quantity])
        print(self._cart._products)
