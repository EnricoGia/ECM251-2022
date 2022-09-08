from string import hexdigits
from tkinter.simpledialog import SimpleDialog
from tkinter.tix import COLUMN
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import *
import tkinter as tk

class GUI():
    def __init__(self):
        self.janela = ttk.Window(
            size = [300,300],
            )
    
    def tela_Home(self):

        nav_bar = ttk.Frame(style='primary', master = self.janela,height=70)
        nav_bar.pack(fill=X, pady=1, side=TOP)

        cart_button = ttk.Button(style = 'danger', master = nav_bar)
        cart_button.pack(side = RIGHT)

        
