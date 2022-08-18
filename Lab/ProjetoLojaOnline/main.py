from modelos.produtos.item import Item
from modelos.carrinho.carrinho import Carrinho

item1 = Item("Carregador",
             "Carrega celulares",
             200.0)

item2 = Item(valor=350.0,
             nome="Stray",
             descricao= "Gato")

item3 = Item(valor=350.0,
             nome="Stray",
             descricao= "Gato")


carrinho = Carrinho()

carrinho.adicionar(item1)
carrinho.adicionar(item2)


print("Tamanho %i" % carrinho.get_quantidade_itens())
print("Valor %.2f" % carrinho.get_valor_total())


carrinho.remover(item1)
print("Tamanho %i" % carrinho.get_quantidade_itens())
print("Valor %.2f" % carrinho.get_valor_total())



