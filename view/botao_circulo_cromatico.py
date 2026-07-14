from tkinter import *
from tkinter.colorchooser import askcolor

class BotaoCromatico:
    def __init__(self, frame_cores):
        self.img_botao_cromatico = PhotoImage(file="images/circulo_cromatico.png")
        self.botao_cromatico = Button(
            master=frame_cores,
            image=self.img_botao_cromatico,
            bg="#C0C0C0",
            relief=RAISED,
            activebackground="#808080",
            borde=1)
        self.botao_cromatico.grid(row=4, column=1)