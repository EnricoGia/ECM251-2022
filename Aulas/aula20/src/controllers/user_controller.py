from models.user import User

class UserController():
    def __init__(self):
        # Carrega os dados dos usuários
        self.users = [
        User(name="João",password = "arroz", email = "joao@gmail.com"),
        User(name="João2",password = "arroz2", email = "joao2@gmail.com"),
        User(name ="tais", password="petacular", email = "tais@perando.com")

        ]
    
    def checkUser(self,user):
        return user in self.users

    def checkLogin(self, name, password):
        user_test = User(name = name,password = password,email=None)
        for user in self.users:
            if user.name == user_test.name and user.password == user_test.password:
                return True
        return False