from tkinter import *

class BotoesAtalhos:
    def __init__(self, frame_atalhos):
        # Imagens dos Botões
        self.img_botao_desfazer = PhotoImage(file="images/desfazer.png")
        self.img_botao_refazer = PhotoImage(file="images/refazer.png")
        self.img_botao_sem_preenchimento_ativo = PhotoImage(file="images/sem_preenchimento_ativo.png")
        self.img_botao_sem_preenchimento = PhotoImage(file="images/sem_preenchimento.png")

        # Seletor modo cor da borda
        """self.lbl_borda = Label(
            master=root,
            text="COR DE BORDA",
            bg="#C0C0C0",
            fg="#000000",
            font=("Arial", 7, "bold"))
        self.lbl_borda.grid(row=0, column=0, columnspan=3)"""

        self.botao_cor_borda = Button(
            text="Borda",
            font=("Arial", 8),
            master=frame_atalhos,
            bg="#000000",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.botao_cor_borda.grid(row=0, column=0, columnspan=3, sticky="nsew", pady=(0, 10))

        # Seletor modo preenchimento
        """self.lbl_preenchimento = Label(
            master=root,
            text="PREENCHIMENTO",
            bg="#C0C0C0",
            fg="#000000",
            font=("Arial", 7, "bold"))
        self.lbl_preenchimento.grid(row=3, column=0, columnspan=3)"""

        self.botao_cor_preenchimento = Button(
            text="Preenchimento",
            font=("Arial", 6),
            master=frame_atalhos,
            bg="#C0C0C0",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.botao_cor_preenchimento.grid(row=1, column=0, columnspan=2, sticky="nsew", pady=(0, 132))
        
        # Seletor de preenchimento vazio
        self.botao_sem_preenchimento = Button(
            master=frame_atalhos,
            bg="#C0C0C0",
            relief=RAISED,
            activebackground="#808080",
            image=self.img_botao_sem_preenchimento_ativo,
            border=1)
        self.botao_sem_preenchimento.grid(row=1, column=2, sticky="nsew", pady=(0, 132))

        # Botão desfazer
        self.botao_desfazer = Button(
            master=frame_atalhos,
            image=self.img_botao_desfazer,
            bg="#C0C0C0",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.botao_desfazer.grid(row=2, column=0, sticky="nsew", padx=(0, 33))

        # Botão refazer
        self.botao_refazer = Button(
            master=frame_atalhos,
            image=self.img_botao_refazer,
            bg="#C0C0C0",
            relief=RAISED,
            activebackground="#808080",
            border=1)
        self.botao_refazer.grid(row=2, column=2, sticky="nsew")