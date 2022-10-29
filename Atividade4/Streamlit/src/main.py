# Enrico Giannobile 19.00610-0

import streamlit as st

from src.controllers.product_controller import ProductController
from src.controllers.user_controller import UserController
from src.controllers.cart_controller import CartController



P_Controller = ProductController()
User_Controller = UserController()

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html= True)

if 'Login' not in st.session_state:
    for user in User_Controller.get_all_info():
        print(user)
    st.session_state['Login'] = 'negado'
    st.session_state['Usuario'] = ''
    st.session_state['Email'] = ''
    st.session_state['Cart'] = CartController()

with st.sidebar:
    if st.session_state['Login'] == 'errado' or st.session_state['Login'] == 'negado':
        st.text("")
        st.text("")

        st.title("Login")

        st.markdown("***")

        email = st.text_input(
            label="Email",
            )

        password = st.text_input(
            label="Senha",
            type = "password")

        st.text("")
        col1, col2 = st.columns(2)
        with col1:
            st.button(label= "Entrar", on_click= User_Controller.check_login, args = (email,password))
        with col2:
            st.button(label = "Novo registro", on_click = User_Controller.tela_registro)

    if st.session_state['Login'] =='aprovado':
        st.markdown("Bem vindo, %s" % st.session_state['Usuario'])
        st.button(label= "Sair", on_click= User_Controller.exit_login)
    
    if st.session_state['Login'] =='registro':
        st.text("")
        st.text("")

        st.title("Novo login")

        st.markdown("***")

        name = st.text_input(
            label="Usuário"
            )
        email = st.text_input(
            label = "Email"
        )
        password = st.text_input(
            label="Senha",
            type = "password")
        cpf = st.text_input(
            label = "CPF"
        )

        col1,col2 = st.columns(2)
        with col1:
            st.button(label = "Voltar", on_click = User_Controller.exit_login)
        with col2:
            st.button(label = "Registrar", on_click = User_Controller.registrar_login, args = (name, email, password, cpf))

if st.session_state['Login'] == 'errado':

    st.markdown("***")
    st.markdown("# Email ou senha incorreto!")
        
if st.session_state['Login'] == 'aprovado':
    tab1, tab2, tab3 = st.tabs(["Perfil", "Home", "Carrinho"])
    with tab1:
        st.title("Perfil")

        st.markdown("***")

        col1,col2 = st.columns(2)

        with col1:
            st.markdown("#")
            st.image("https://cdn-icons-png.flaticon.com/512/17/17004.png")
        
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
            c.markdown("## %s" % prdct.get_name())
            c.image("%s" % prdct.get_url())
            c.markdown("#### R$ %.2f" % prdct.get_price())
            quantity = c.number_input(label = "", format = "%i", step = 1, min_value = 1)
            c.button(label = "Adicionar",on_click = st.session_state['Cart'].add_product, args=(prdct,quantity))
            
        with col2:
            c = st.container()
            prdct = P_Controller.get_product(index = 1)
            c.markdown("## %s" % prdct.get_name())
            c.image("%s" % prdct.get_url())
            c.markdown("#### R$ %.2f" % prdct.get_price())
            quantity = c.number_input(label = "", format = "%i", step = 1,min_value =1,key=3)
            c.button(label = "Adicionar",on_click = st.session_state['Cart'].add_product, args=(prdct,quantity),key = 3)
        
        with col1:
            c = st.container()
            prdct = P_Controller.get_product(index = 2)
            c.markdown("## %s" % prdct.get_name())
            c.image("%s" % prdct.get_url())
            c.markdown("#### R$ %.2f" % prdct.get_price())
            quantity = c.number_input(label = "", format = "%i", step = 1,min_value = 1,key = 4)
            c.button(label = "Adicionar",on_click = st.session_state['Cart'].add_product, args=(prdct,quantity),key = 4)

        with col2:
            c = st.container()
            prdct = P_Controller.get_product(index = 3)
            c.markdown("## %s" % prdct.get_name())
            c.image("%s" % prdct.get_url())
            c.markdown("#### R$ %.2f" % prdct.get_price())
            quantity = c.number_input(label = "", format = "%i", step = 1,min_value = 1,key=5)
            c.button(label = "Adicionar",on_click = st.session_state['Cart'].add_product, args=(prdct,quantity),key = 5)
    with tab3:
        if 'Cart' in st.session_state:

            row = st.container()
            col1,col2,col3,col4 = st.columns(4)
            col1.markdown("##### Produto")
            col2.markdown("##### Preço unitário")
            col3.markdown("##### Quantidade")
            col4.markdown("##### Preço conjunto")
            with row :
                for i in st.session_state['Cart'].get_cart().get_products():
                        col1.markdown("#### %s" % i[0].get_name())
                        col2.markdown("#### R\$ %.2f" %  i[0].get_price())
                        col3.markdown("#### %s" % i[1])
                        col4.markdown("#### R\$ %.2f" % (i[0].get_price()*i[1]))

            st.markdown("***")
            col1,col2 = st.columns(2)

             
            col1.markdown("# Preço Total:")
            col2.markdown("# R\$ %.2f" % st.session_state['Cart'].total_price())
            
            
   
