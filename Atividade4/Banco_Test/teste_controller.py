

from user_controller import UserController


controller = UserController()

resultado = controller.get_all()

print(resultado)

for user in resultado:
    print(user)