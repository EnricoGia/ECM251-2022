from pathlib import Path
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import *
from PIL import *


janela = ttk.Window(
            size = [800,800],
            )


nav_bar = ttk.Frame(style='primary', master = janela)
nav_bar.grid(row = 1,column=1,ipadx=800,ipady=30)

nav_bar_under = ttk.Frame(style = 'danger', master = janela)
nav_bar_under.grid(row = 2,column=1,ipadx=800,ipady=30)

"""
frame_inferior = ttk.Frame(style = 'dark', master = janela)
frame_inferior.pack(fill=Y, expand=TRUE, side=RIGHT,ipadx = 10)


#self.seta_esquerda = ttk.PhotoImage(file = p/"imagens/seta.png")
cart_button = ttk.Button(style = 'danger', master = nav_bar, text = "voltar",compound=LEFT)
cart_button.pack(side = LEFT,ipady=8,ipadx=8)
"""
janela.mainloop()