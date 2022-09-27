
import streamlit as st
from src.controllers.product_controller import ProductController

from src.models import product
from src.controllers.user_controller import UserController
from src.controllers.cart_controller import CartController
from src.models import cart


P_Controller = ProductController()
# Cart_Controller = CartController()
User_Controller = UserController()

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html= True)

if 'Login' not in st.session_state:
    st.session_state['Login'] = 'negado'
    st.session_state['Usuario'] = ''
    st.session_state['Email'] = ''
    st.session_state['Cart'] = CartController()

with st.sidebar:
    st.text("")
    st.text("")

    st.title("Login")

    st.markdown("***")

    usuario = st.text_input(
        label="Usuário",
        )

    senha = st.text_input(
        label="Senha",
        type = "password")

    st.text("")
    col1,col2 = st.columns(2)
    

    with col1:
        st.button(label= "Entrar", on_click= User_Controller.checkLogin, args = (usuario,senha))

    with col2:
        st.button(label= "Sair", on_click= User_Controller.exit_login)

    if "Login" in st.session_state:
        st.markdown("#### Login " + st.session_state["Login"])

if st.session_state['Login'] == 'aprovado':
    tab1, tab2, tab3 = st.tabs(["Profile", "Home", "Carrinho"])
    with tab1:
        st.title("Profile")

        st.markdown("***")

        col1,col2 = st.columns(2)

        with col1:
            st.markdown("#")
            st.image("https://i.scdn.co/image/ab6761610000e5eb9319d939accc1f1e22155955")
        
        with col2:
            st.markdown("***")
            st.markdown("### Nome:")
            st.markdown("#### %s" % st.session_state["Usuario"])
            st.markdown("***")
            st.markdown("### Email:")
            st.markdown("#### %s" % st.session_state["Email"])
            st.markdown("***")

    with tab2:

        st.title("Home")

        st.markdown("***")

        col1,col2 = st.columns(2,gap="large")
        
        with col1:
            c = st.container()
            prdct = P_Controller.get_product(index = 0)
            c.markdown("## %s" % prdct._name)
            c.image("%s" % prdct._url)
            c.markdown("#### R$ %.2f" % prdct._price)
            quantity = c.number_input(label = "", format = "%i", step = 1, min_value = 1)
            c.button(label = "Adicionar",on_click = st.session_state['Cart'].add_product, args=(prdct,quantity))
            
        with col2:
            c = st.container()
            prdct = P_Controller.get_product(index = 1)
            c.markdown("## %s" % prdct._name)
            c.image("%s" % prdct._url)
            c.markdown("#### R$ %.2f" % prdct._price)
            quantity = c.number_input(label = "", format = "%i", step = 1,min_value =1,key=3)
            c.button(label = "Adicionar",on_click = st.session_state['Cart'].add_product, args=(prdct,quantity),key = 3)
        
        with col1:
            c = st.container()
            prdct = P_Controller.get_product(index = 2)
            c.markdown("## %s" % prdct._name)
            c.image("%s" % prdct._url)
            c.markdown("#### R$ %.2f" % prdct._price)
            quantity = c.number_input(label = "", format = "%i", step = 1,min_value = 1,key = 4)
            c.button(label = "Adicionar",on_click = st.session_state['Cart'].add_product, args=(prdct,quantity),key = 4)

        with col2:
            c = st.container()
            prdct = P_Controller.get_product(index = 3)
            c.markdown("## %s" % prdct._name)
            c.image("%s" % prdct._url)
            c.markdown("#### R$ %.2f" % prdct._price)
            quantity = c.number_input(label = "", format = "%i", step = 1,min_value = 1,key=5)
            c.button(label = "Adicionar",on_click = st.session_state['Cart'].add_product, args=(prdct,quantity),key = 5)
    with tab3:
        if 'Cart' in st.session_state:
            c = st.container()
            with c :
                col1,col2,col3,col4 = st.columns(4)
            
                for i in st.session_state['Cart'].get_products():
                    with col4:
                        c.markdown("%s R\$ %s  %s R\$ %s" % (i[0].get_name(), i[0].get_price(),i[1],(i[0].get_price()*i[1])))
   
