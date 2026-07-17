from tkinter import *

class BotoesFormas:
    def __init__(self, frame_formas):

        # Imagens dos Botões
        self.img_botao_linha = PhotoImage(file="images/linha.png")
        self.img_botao_circulo = PhotoImage(file="images/circulo.png")
        self.img_botao_oval = PhotoImage(file="images/oval.png")
        self.img_botao_quadrado = PhotoImage(file="images/quadrado.png")
        self.img_botao_retangulo = PhotoImage(file="images/retangulo.png")
        self.img_botao_triangulo= PhotoImage(file="images/triangulo.png")
        self.img_botao_poligono = PhotoImage(file="images/poligono.png")

        # Botão de Linha
        self.botao_linha = Button(
            master=frame_formas,
            image=self.img_botao_linha,
            bg="#C0C0C0",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.botao_linha.grid(row=0, column=0)
        
        # Botão de Círculo
        self.botao_circulo = Button(
            master=frame_formas,
            image=self.img_botao_circulo,
            bg="#C0C0C0",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.botao_circulo.grid(row=0, column=1)

        # Botão de Oval
        self.botao_oval = Button(
            master=frame_formas,
            image=self.img_botao_oval,
            bg="#C0C0C0",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.botao_oval.grid(row=0, column=2)

        # Botão de Quadrado
        self.botao_quadrado = Button(
            master=frame_formas,
            image=self.img_botao_quadrado,
            bg="#C0C0C0",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.botao_quadrado.grid(row=1, column=0)

        # Botão de Retângulo
        self.botao_retangulo = Button(
            master=frame_formas,
            image=self.img_botao_retangulo,
            bg="#C0C0C0",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.botao_retangulo.grid(row=1, column=1)

        # Botão de Triângulo
        self.botao_triangulo = Button(
            master=frame_formas,
            image=self.img_botao_triangulo,
            bg= "#C0C0C0",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.botao_triangulo.grid(row=1, column=2)

        # Botão de Polígono
        self.botao_poligono = Button(
            master=frame_formas,
            image= self.img_botao_poligono,
            bg="#C0C0C0",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.botao_poligono.grid(row=2, column=0)
