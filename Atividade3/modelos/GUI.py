
from tkinter.tix import COLUMN
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import *


class GUI():
    def __init__(self):
        self.janela = ttk.Window(
            size = [800,800]
            )

        self.usuario = ttk.StringVar(value="")
        self.senha = ttk.StringVar(value="")
        ##self.tela_login(self.usuario,self.senha)
        self.tela_produto()
        self.janela.place_window_center()
    
    def tela_home(self):

        nav_bar = ttk.Frame(style='primary', master = self.janela,height=70)
        nav_bar.pack(fill=X, pady=1, side=TOP)

        cart_button = ttk.Button(style = 'danger', master = nav_bar)
        cart_button.pack(side = RIGHT)



    def tela_login(self, usuario, senha):
        frame1 = ttk.Frame()
        frame1.place(rely=0.4,relx=0.5,anchor="c")

        texto1 = ttk.Label(text="Usuário",master = frame1)
        texto1.grid(row=1,pady=[15,0])

        campo1 = ttk.Entry(style="warning",master = frame1,width=30, textvariable=usuario)
        campo1.grid(row=2)

        texto2 = ttk.Label(text="Senha",master = frame1)
        texto2.grid(row=3,pady=[15,0])

        campo2 = ttk.Entry(style="warning", master = frame1, width=30, textvariable = senha)
        campo2.grid(row=4)

        botao1 = ttk.Button(text="Entrar", master = frame1, width=16, command=self.verifica_login)
        botao1.grid(row=5,pady=[20,0])

    def tela_produto(self):
        nav_bar = ttk.Frame(style='primary', master = self.janela)
        nav_bar.pack(fill=X, pady=1,ipady=10, side=TOP)

        cart_button = ttk.Button(style = 'danger', master = nav_bar,image='seta.png')
        cart_button.pack(side = RIGHT,ipady=8,ipadx=8)

    def verifica_login(self):
        print("verificando")
        print(self.usuario.get(),self.senha.get())

        usuario = self.usuario.get()
        senha = self.senha.get()

        arquivo = open("modelos/logs.txt", "r")
        login = (usuario + ":" + senha + "\n")

        linhas = arquivo.readlines()

        aprovado = False

        for linha in linhas:
            if (linha == login):
                aprovado = True
                break

        arquivo.close()
        print("Aprovado!" if aprovado else "Negado!")
        print("\n")
        






        
