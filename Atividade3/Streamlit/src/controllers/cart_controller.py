from src.models.cart import Cart
class CartController():
    def __init__(self):
        self._cart = Cart()

    def add_product(self,product,quantity):
        
        for i in range(len(self._cart._products)):
            if self._cart._products[i][0].get_name() == product.get_name():
                self._cart._products[i][1] += quantity
                print(self._cart._products)
                return

        self._cart._products.append([product,quantity])
        print(self._cart._products)

    def get_products(self):
        return self._cart.get_products()
    
    def calculate_price(self,product,quantity):
        return (product.get_price()*quantity)