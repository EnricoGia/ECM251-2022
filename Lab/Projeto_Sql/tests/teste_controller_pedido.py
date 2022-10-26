from src.controllers.pedido_controller import PedidoController

controller = PedidoController()

resultado = controller.pegar_pedido("001")

for elemento in resultado:
    print(elemento)

item_pedido = resultado[0]
item_pedido.quantidade = 10
controller.atualizar_pedido(item_pedido)

print("$$###$$##")
resultado = controller.pegar_pedido("001")
for elemento in resultado:
    print(elemento)