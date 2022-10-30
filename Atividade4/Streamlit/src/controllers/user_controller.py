# Enrico Giannobile 19.00610-0

import streamlit as st
from src.models.user import User
from src.controllers.cart_controller import CartController
from src.dao.user_dao import UserDAO

class UserController():
    def __init__(self):
        # Carrega os dados dos usuários
        self.users = UserDAO.get_instance().get_all()
        
    
    def checkUser(self,user):
        return user in self.users

    def check_login(self, email, password):
        try:
            user_test = User(name = None, password = password, email = email)
            for user in self.users:
                if user.get_email() == user_test.get_email() and user.get_password() == user_test.get_password():
                    st.session_state["Login"] = "aprovado"
                    st.session_state['Usuario'] = user.get_name()
                    st.session_state['Email'] = user.get_email()
                    return True
            st.session_state["Login"] = "errado"
            return False
        except:
            st.session_state["Login"] = "errado"

    def exit_login(self):
        st.session_state["Login"] = "negado"
        st.session_state["Profile"] = "info"
        st.session_state['Cart'] = CartController()

    def register_screen(self):
        st.session_state["Login"] = "registro"

    def register_login(self, name, email, password, cpf):
        UserDAO.get_instance().register_login(name, email, password, cpf)

    def get_all_info(self):
        return UserDAO.get_instance().get_all_info()
    
    def change_profile_screen(self):
        st.session_state["Profile"] = "changes"
    
    def change_profile_screen_back(self):
        st.session_state["Profile"] = "info"
    
    def change_profile(self, email, password, email_now):
        if(UserDAO.get_instance().change_profile(email, password, email_now)):
            st.session_state["Email"] = email