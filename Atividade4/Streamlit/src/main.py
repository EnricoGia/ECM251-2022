# Enrico Giannobile 19.00610-0

import streamlit as st

from src.controllers.product_controller import ProductController
from src.controllers.user_controller import UserController
from src.controllers.cart_controller import CartController


# Atualizam constantemente
P_Controller = ProductController()
User_Controller = UserController()
#

# Atualizam apenas uma vez
if 'Login' not in st.session_state:
    st.session_state['Login'] = 'negado'
    st.session_state['Usuario'] = ''
    st.session_state['Email'] = ''
    st.session_state['Profile'] = "info"
    st.session_state['Cart'] = CartController()
#

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
            st.button(label = "Novo registro", on_click = User_Controller.register_screen)

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
            label= "Senha",
            type = "password")
        cpf = st.text_input(
            label = "CPF"
        )

        col1,col2 = st.columns(2)
        with col1:
            st.button(label = "Voltar", on_click = User_Controller.exit_login)
        with col2:
            st.button(label = "Registrar", on_click = User_Controller.register_login, args = (name, email, password, cpf))

if st.session_state['Login'] == 'errado':

    st.markdown("***")
    st.markdown("# Email ou senha incorreto!")
        
if st.session_state['Login'] == 'aprovado':
    tab1, tab2, tab3 = st.tabs(["Perfil", "Home", "Carrinho"])
    with tab1:
        if st.session_state['Profile'] == "info":
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
                st.button(label = "Mudar informações de login", on_click = User_Controller.change_profile_screen)
        
        if st.session_state["Profile"] == "changes":
            st.title("Novas informações de login")

            st.markdown("***")
            email = st.text_input(
            label = "Novo email"
        )
            password = st.text_input(
                label= "Nova senha",
                type = "password")

            col1,col2 = st.columns(2)
            with col1:
                st.button(label = "Voltar", on_click = User_Controller.change_profile_screen_back)
            with col2:
                st.button(label = "Mudar", on_click = User_Controller.change_profile, args = (email,password,st.session_state["Email"]))   
    with tab2:

        st.title("Home")

        st.button(label = "Adicionar novo produto", on_click = User_Controller.add_new_product_screen)

        st.markdown("***")

        col1,col2 = st.columns(2,gap="large")
        
        for (i,product) in enumerate(P_Controller.get_products()):
            try:
                if(i%2 == 0):
                    with col1:
                        c = st.container()
                        c.image("%s" % product.get_url())
                        c.markdown("## %s" % product.get_name())  
                        c.markdown("#### R$ %.2f" % product.get_price())
                        quantity = c.number_input(label = "", format = "%i", step = 1, min_value = 1, key = i)
                        c.button(label = "Adicionar",on_click = st.session_state['Cart'].add_product, args=(product, quantity), key = i)

                else:
                    with col2:
                        c = st.container()
                        c.image("%s" % product.get_url())
                        c.markdown("## %s" % product.get_name())
                        c.markdown("#### R$ %.2f" % product.get_price())
                        quantity = c.number_input(label = "", format = "%i", step = 1, min_value = 1, key = i)
                        c.button(label = "Adicionar",on_click = st.session_state['Cart'].add_product, args=(product,quantity), key = i)
            except Exception: #URL não encontrada
                pass
        
    with tab3:
        if 'Cart' in st.session_state:
            st.title("Carrinho")
            st.markdown("***")

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
            st.markdown("***")
            st.button(label = "Finalizar pedido", on_click=st.session_state["Cart"].empty_cart)
    
if st.session_state["Login"] == "new_product":
    
    
    st.title("Novo produto")
    st.markdown("***")

    name = st.text_input(
        label="Nome"
        )
    price = st.text_input(
        label = "Preço"
    )
    url = st.text_input(
        label= "URL")

    col1,col2 = st.columns(2)
    with col1:
        st.button(label = "Voltar", on_click = User_Controller.default_screen)
    with col2:
        st.button(label = "Adicionar novo produto", on_click = P_Controller.register_product, args = (name, price, url))
            
   
