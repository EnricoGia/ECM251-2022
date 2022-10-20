from src.dao.item_dao import ItemDAO

itens = ItemDAO.get_instance().get_all()

for item in itens:
    print(item)

item = ItemDAO.get_instance().pegar_item("OLA")
item.nome = "NVIDIA RTX4090"   
item.preco = 135000

print(ItemDAO.get_instance().atualizar_item(item))
