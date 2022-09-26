import streamlit as st
from src.models.user import User

class UserController():
    def __init__(self):
        # Carrega os dados dos usuários
        self.users = [
        User(name="João", password = "arroz", email = "joao@gmail.com"),
        User(name="João2", password = "arroz2", email = "joao2@gmail.com"),
        User(name ="tais", password="petacular", email = "tais@perando.com"),
        User(name="usuario", password ="senha", email = "padrao@gmail.com")

        ]
    
    def checkUser(self,user):
        return user in self.users

    def checkLogin(self, name, password):
        user_test = User(name = name, password = password, email=None)
        for user in self.users:
            if user.get_name() == user_test.get_name() and user.get_password() == user_test.get_password():
                st.session_state["Login"] = "aprovado"
                st.session_state['Usuario'] = user.get_name()
                st.session_state['Email'] = user.get_email()
                return True
        st.session_state["Login"] = "negado"
        return False

    def exit_login(self):
        st.session_state["Login"] = "negado"
