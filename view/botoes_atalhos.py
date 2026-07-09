from tkinter import *

class BotoesAtalhos:
    def __init__(self, root):
        # Imagens dos Botões
        self.img_btn_desfazer = PhotoImage(file="images/desfazer.png")
        self.img_btn_refazer = PhotoImage(file="images/refazer.png")

        # Seletor modo cor da borda
        """self.lbl_borda = Label(
            master=root,
            text="COR DE BORDA",
            bg="#C0C0C0",
            fg="#000000",
            font=("Arial", 7, "bold"))
        self.lbl_borda.grid(row=0, column=0, columnspan=3)"""

        self.btn_cor_borda = Button(
            master=root,
            bg="#C0C0C0",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.btn_cor_borda.grid(row=0, column=0, columnspan=3, sticky="nsew", pady=(0, 10))

        # Seletor modo preenchimento
        """self.lbl_preenchimento = Label(
            master=root,
            text="PREENCHIMENTO",
            bg="#C0C0C0",
            fg="#000000",
            font=("Arial", 7, "bold"))
        self.lbl_preenchimento.grid(row=3, column=0, columnspan=3)"""

        self.btn_fig_preenchida = Button(
            master=root,
            bg="#C0C0C0",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.btn_fig_preenchida.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=(0, 132))
        
        self.btn_figura_vazia = Button(
            master=root,
            bg="#C0C0C0",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.btn_figura_vazia.grid(row=1, column=2, sticky="nsew", pady=(0, 132))

        # Botão desfazer
        self.btn_desfazer = Button(
            master=root,
            image=self.img_btn_desfazer,
            bg="#C0C0C0",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.btn_desfazer.grid(row=2, column=0, sticky="nsew", padx=(0, 33))

        # Botão refazer
        self.btn_refazer = Button(
            master=root,
            image=self.img_btn_refazer,
            bg="#C0C0C0",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.btn_refazer.grid(row=2, column=2, sticky="nsew")