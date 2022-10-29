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

    def checkLogin(self, email, password):
        try:
            user_test = User(name = None, password = password, email = email)
            for user in self.users:
                if user.get_email() == user_test.get_email() and user.get_password() == user_test.get_password():
                    st.session_state["Login"] = "aprovado"
                    st.session_state['Usuario'] = user.get_name()
                    st.session_state['Email'] = user.get_email()
                    return True
            st.session_state["Login"] = "negado"
            return False
        except:
            st.session_state["Login"] = "negado"

    def exit_login(self):
        st.session_state["Login"] = "negado"
        st.session_state['Cart'] = CartController()
