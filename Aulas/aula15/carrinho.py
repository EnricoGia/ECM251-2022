class Carrinho():
    # Construtor
    def __init__(self):
        self._itens = []

    # Demais métodos
    def get_valor_total(self)->float:
        total = 0
        for item in self._itens:
            total += item.get_valor()
        return total

    def get_quantidade_itens(self):
        return len(self._itens)

    def adicionar(self, item):
        self._itens.append(item)

    def remover(self, item):
        if item in self._itens:
            self._itens.remove(item)
            