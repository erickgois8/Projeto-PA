from tkinter import *
from tkinter import ttk


class Menu(): #podemos dar um nome melhor dps
    
    def __init__(self):
        self.root = Tk()
        self.config()
    
        self.root.mainloop()
    
    def config(self):
        self.root.title("Meu paint")
        self.root.geometry("800x680")


Menu()