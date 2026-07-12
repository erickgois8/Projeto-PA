from tkinter import *

class BotoesSalvar:
    def __init__(self, frame_superior):
        # Imagens dos Botões
        self.img_botao_salvar = PhotoImage(file="images/salvar.png")
        self.img_botao_abrir = PhotoImage(file="images/abrir.png")

        # Botão de salvar arquivo
        self.botao_salvar = Button(
            master=frame_superior,
            image=self.img_botao_salvar,
            bg="#C0C0C0",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.botao_salvar.grid(padx=10, pady = 0)
    
        # Botão de abrir arquivos
        self.botao_abrir = Button(
            master=frame_superior,
            image=self.img_botao_abrir,
            bg="#C0C0C0",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.botao_abrir.grid(row=0, column=7)

    