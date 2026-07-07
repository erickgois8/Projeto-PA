from tkinter import *

class BotoesCores:
    def __init__(self, root):
        # Botão Branco
        self.botao_branco = Button(
            master=root,
            bg="#FFFFFF",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.botao_branco.grid(row=0, column=0)

        # Botão Cinza
        self.botao_cinza = Button(
            master=root,
            bg="#8F8E8E",
            relief=RAISED,
            activebackground="#808080",
            borde=1)
        self.botao_cinza.grid(row=0, column=1)

        #Botão Preto
        self.botao_preto = Button(
            master=root,
            bg="#000000",
            relief=RAISED,
            activebackground="#808080",
            borde=1)
        self.botao_preto.grid(row=0, column=2)

        # Botão Vermelho
        self.botao_vermelho = Button(
            master=root,
            bg="#e12729",
            relief=RAISED,
            activebackground="#808080",
            borde=1)
        self.botao_vermelho.grid(row=1, column=0)

        # Botão Laranja
        self.botao_laranja = Button(
            master=root,
            bg="#f37324",
            relief=RAISED,
            activebackground="#808080",
            borde=1)
        self.botao_laranja.grid(row=1, column=1)

        # Botão Amarelo
        self.botao_amarelo = Button(
            master=root,
            bg="#f8cc1b",
            relief=RAISED,
            activebackground="#808080",
            borde=1)
        self.botao_amarelo.grid(row=1, column=2)

        # Botão Verde
        self.botao_verde = Button(
            master=root,
            bg="#007f4e",
            relief=RAISED,
            activebackground="#808080",
            borde=1)
        self.botao_verde.grid(row=2, column=0)

        # Botão Verde Claro
        self.botao_verde_claro = Button(
            master=root,
            bg="#72b043",
            relief=RAISED,
            activebackground="#808080",
            borde=1)
        self.botao_verde_claro.grid(row=2, column=1)

        # Botão Ciano
        self.botao_ciano = Button(
            master=root,
            bg="#53d0b5",
            relief=RAISED,
            activebackground="#808080",
            borde=1)
        self.botao_ciano.grid(row=2, column=2)

        # Botão Azul
        self.botao_azul = Button(
            master=root,
            bg="#1982c4",
            relief=RAISED,
            activebackground="#808080",
            borde=1)
        self.botao_azul.grid(row=3, column=0)

        # Botão Roxo
        self.botao_roxo = Button(
            master=root,
            bg="#6a4c93",
            relief=RAISED,
            activebackground="#808080",
            borde=1)
        self.botao_roxo.grid(row=3, column=1)

        # Botão Rosa
        self.botao_rosa = Button(
            master=root,
            bg="#f49ac2",
            relief=RAISED,
            activebackground="#808080",
            borde=1)
        self.botao_rosa.grid(row=3, column=2)