from tkinter import *

class BotoesFormas:
    def __init__(self, root):
        self.img_btn_linha = PhotoImage(file="images/linha.png")
        self.img_btn_circulo = PhotoImage(file="images/circulo.png")
        self.img_btn_oval = PhotoImage(file="images/oval.png")
        self.img_btn_quadrado = PhotoImage(file="images/quadrado.png")
        self.img_btn_retangulo = PhotoImage(file="images/retangulo.png")

        # Botão de Linha
        self.botao_linha = Button(
            master=root,
            image=self.img_btn_linha,
            bg="#1B1919",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.botao_linha.grid(row=0, column=0)
        
        # Botão de Círculo
        self.botao_circulo = Button(
            master=root,
            image=self.img_btn_circulo,
            bg="#C0C0C0",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.botao_circulo.grid(row=0, column=1)

        # Botão de Oval
        self.botao_oval = Button(
            master=root,
            image=self.img_btn_oval,
            bg="#C0C0C0",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.botao_oval.grid(row=0, column=2)

        # Botão de Quadrado
        self.botao_quadrado = Button(
            master=root,
            image=self.img_btn_quadrado,
            bg="#C0C0C0",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.botao_quadrado.grid(row=1, column=0)

        # Botão de Retângulo
        self.botao_retangulo = Button(
            master=root,
            image=self.img_btn_retangulo,
            bg="#C0C0C0",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.botao_retangulo.grid(row=1, column=1)