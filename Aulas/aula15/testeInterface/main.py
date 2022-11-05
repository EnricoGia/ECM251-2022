from item import Item
from carrinho import Carrinho

def mostrar_itens():
    print("\n- Itens Disponíveis -")
    num = 0
    for i in itens:
        print("%i - %s"% (num,i))
        num +=1

def adicionar_item():
    mostrar_itens()
    novo_item = input("Escoha um item para adicionar: ")
    carrinho.adicionar(novo_item)

item1 = Item("Carregador",
             "Carrega celulares",
             200.0)

item2 = Item(valor=350.0,
             nome="Stray",
             descricao= "Gato")

item3 = Item(valor=350.0,
             nome="Stray",
             descricao= "Gato")

itens = [item1,item2]

carrinho = Carrinho()
opcoes = {1:adicionar_item}
op = 20

while (op != 0):

    print("\n--- Carrinho de compras --- ")
    print("0 - Sair")
    print("1 - Adicionar item")

    op = int(input("Selecione uma opção: "))

    if(op != 0):
        opcoes[op]()

    
print("Encerrando...")
# carrinho.adicionar(item1)
# carrinho.adicionar(item2)


# print("Tamanho %i" % carrinho.get_quantidade_itens())
# print("Valor %.2f" % carrinho.get_valor_total())


# carrinho.remover(item1)
# print("Tamanho %i" % carrinho.get_quantidade_itens())
# print("Valor %.2f" % carrinho.get_valor_total())



