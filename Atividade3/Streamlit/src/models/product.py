class Product():
    def __init__(self, name, price, url):
        self._name = name
        self._price = price
        self._url = url

    def __str__(self)->str:
        return f'Product(name:{self._name}, price:{self._price}, url:{self._url}'