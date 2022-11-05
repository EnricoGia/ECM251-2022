class Conta():
    def __init__(self,usuario,senha):
        self._usuario = usuario
        self._senha = senha

    def get_usuario(self):
        return self._usuario
    
    