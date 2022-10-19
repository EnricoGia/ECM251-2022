
from src.controllers.item_controller import ItemController
from src.models.item import Item

controller = ItemController()
itens = controller.pegar_todos_itens()
for item in itens:
    print(item)

novo_item = Item("OLA", "Cooler REDRAGON Vermelho", 19.90)
print(controller.inserir_item(novo_item))

itens = controller.pegar_todos_itens()
for item in itens:
    print(item)

item = controller.pegar_item("CAF")
print(item)