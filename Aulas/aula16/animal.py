class Animal():
    def __init__(self, nome):
        self._nome = nome

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super(self,nome)
        self._raca = raca