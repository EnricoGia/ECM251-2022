# Enrico Giannobile 19.00610-0

class Cart():
    def __init__(self):
        self._products=[]


    def get_product(self,name):
        for i in self._products:
            if i.get_name() == name:
                return i
    
    def __str__(self):
        return self._products
    
    def get_products(self):
        return self._products