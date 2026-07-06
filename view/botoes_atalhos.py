from tkinter import *

class BotoesAtalhos:
    def __init__(self, frame_atalhos):
        self.frame_atalhos = frame_atalhos

        # Botão de rabisco
        self.Img_lapis = PhotoImage(file="images/lapis.png")
        self.botao_lapis = Button(self.frame_atalhos,
                                  image=self.Img_lapis,
                                  bg = "#C0C0C0",
                                  relief=RAISED,
                                  activebackground="#A9A9A9",
                                  border=1,
                                  width=32,
                                  height=32) 
        self.botao_lapis.grid(row=10, column=25)

        # Botão de borrancha
        self.Imag_borracha