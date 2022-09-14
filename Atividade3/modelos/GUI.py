from pathlib import Path
from tkinter import font
from turtle import bgcolor
from webbrowser import BackgroundBrowser
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import *
from PIL import *


p = Path(__file__).parent

class GUI():
    def __init__(self):
        self.janela = ttk.Window(
            size = [1920,1080],
            )
        ##self.janela.config(bg = "light gray")
        self.usuario = ttk.StringVar(value="")
        self.senha = ttk.StringVar(value="")
        self.tela_login(self.usuario,self.senha)
        #self.tela_produto()
        self.janela.place_window_center()
    
    def tela_home(self):

        nav_bar = ttk.Frame(style='primary', master = self.janela,height=70)
        nav_bar.pack(fill=X, pady=1, side=TOP)

        cart_button = ttk.Button(style = 'danger', master = nav_bar)
        cart_button.pack(side = RIGHT)



    def tela_login(self, usuario, senha):
        primary_color = "#F4A261"
        font_type = "Bahnschrift SemiLight SemiConde"
        # Configures
        self.janela.configure(background="#1E1E1E")
        self.style = ttk.Style()
        self.style.configure("Login.TLabel",foreground = "white", background = primary_color,font=(font_type,20))
        self.style.configure("Login.TFrame",background = primary_color)
        self.style.configure("Login.TEntry")
        self.style.configure("Login.TButton",font=(font_type,20),background = '#003566')
        # Widgets
        frame1 = ttk.Frame(style = "Login.TFrame",master = self.janela,border=300) 
        frame1.place(rely=0.45,relx=0.5,anchor="c")

        texto1 = ttk.Label(style = "Login.TLabel" ,text="Usuário",master = frame1)
        texto1.grid(row=1,pady=[15,0])

        campo1 = ttk.Entry(style = "Login.TEntry",master = frame1,width=50,textvariable=usuario)
        campo1.grid(row=2)

        texto2 = ttk.Label(style = "Login.TLabel",text="Senha",master = frame1)
        texto2.grid(row=3,pady=[15,0])

        campo2 = ttk.Entry(style="Login.TEntry", master = frame1, width=50, textvariable = senha)
        campo2.grid(row=4)

        botao1 = ttk.Button(style = "Login.TButton",text="Entrar", master = frame1, width=16, command=self.verifica_login)
        botao1.grid(row=5,pady=[40,0])

    def tela_produto(self):

        # Widgets

        nav_bar = ttk.Frame(style='primary', master = self.janela)
        nav_bar.pack(fill=X,ipady=10, side=TOP)

        nav_bar_under = ttk.Frame(style = 'danger', master = self.janela)
        nav_bar_under.pack(fill=X, ipady=18, side=TOP)

        frame_inferior = ttk.Frame(style = 'dark', master = self.janela)
        frame_inferior.pack(fill=BOTH, expand=TRUE, side=RIGHT,ipadx = 10)
        
        #self.seta_esquerda = ttk.PhotoImage(file = p/"imagens/seta.png")
        cart_button = ttk.Button(style = 'danger', master = frame_inferior,text = "voltar",compound=LEFT)
        cart_button.grid(row=1,column=1)

        cart_button = ttk.Button(style = 'danger', master = nav_bar,text = "voltar",compound=LEFT)
        cart_button.pack(side = LEFT,ipady=8,ipadx=8)

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







        
