from src.controllers.pedido_controller import PedidoController

controller = PedidoController()

resultado = controller.pegar_pedido("001")

for elemento in resultado:
    print(elemento)