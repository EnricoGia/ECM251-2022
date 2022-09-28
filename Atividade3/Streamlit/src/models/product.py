class Product():
    def __init__(self, name, price, url):
        self._name = name
        self._price = price
        self._url = url

    def __str__(self)->str:
        return f'Product(name:{self._name}, price:{self._price}, url:{self._url}'
    
    def get_name(self):
        return self._name
    
    def get_price(self):
        return self._price
    
    def get_url(self):
        return self._url