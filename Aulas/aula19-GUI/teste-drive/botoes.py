import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage

base = ttk.Window(
    title = "Minha GUI",
    size = (1024,400),
    position=(100,100),
    minsize = (600,300),
    maxsize=(1800,900),
    alpha = 0.75
)

base.iconphoto(False,PhotoImage(file='calculator.png'))
# Criando um botão

def acao_botao():
    print("Click!")

ttk.Button(
    base,
    text= "Ola Mundo!",
    bootstyle="default",
    command = acao_botao
).pack(side=LEFT, padx = 10, pady=5)

# Ponto de entrada da interface
base.mainloop()