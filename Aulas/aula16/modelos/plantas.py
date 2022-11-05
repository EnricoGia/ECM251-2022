class Plantas:

    def __init__(self, nome):
        self._nome = nome

    def get_nome(self):
        return self._nome


class Arvore(Plantas):
    def __str__(self):
        return (f"Uma árvore chamada {self.get_nome()}")


class Alface(Plantas):
    def __str__(self):
        return (f"Um alface chamado {self.get_nome()}")
