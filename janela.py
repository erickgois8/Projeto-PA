from tkinter import *
from tkinter import ttk


class Menu(): #podemos dar um nome melhor dps
    cinza_escuro = "#808080"
    cinza_medio = "#C0C0C0"
    branco = "#FFFFFF"
    preto = "#000000"
    verde = "#007f4e"
    verde_claro = "#72b043"
    amarelo = "#f8cc1b"
    laranja = "#f37324"
    vermelho = "#e12729"
    ciano = "#52a675"
    azul = "#1982c4"
    roxo = '#6a4c93'
    rosa = '#f49ac2'
    


    def __init__(self, controller=None):
        # controller: instancia de Interface que possui selecionaCor
        self.controller = controller
        if self.controller is None:
            self.root = Tk()
            self._own_root = True
        else:
            self.root = self.controller.root
            self._own_root = False

        self.config()
        self.frames()
        self.canvas()
        self.widgets()
        self.widgets_cores()

        if self._own_root:
            self.root.mainloop()
    
    def config(self):
        self.root.title("Meu paint")
        self.root.geometry("1920x1080")

        #Adaptação do ícone da janela para que seja possível rodar o programa em linux também já que ele não reconhece o ícone .ico
        self.icone = PhotoImage(file="images/icone.png")
        self.root.iconphoto(False, self.icone)

        self.root.configure(bg=self.cinza_escuro)

    def frames(self):
        self.frame_lateral = Frame(self.root, bg=self.cinza_medio, width=120, height=1080)
        self.frame_lateral.pack(side=LEFT, fill=Y)

    def canvas(self):
        self.canvas = Canvas(self.root, bg=self.branco, width=1770, height=1080)

        #Essa parte me garante que o canva estará possicionado corretamente na tela, e que ele se adaptará ao tamanho da janela caso o usuário a redimensione.
        self.canvas.pack(side=RIGHT, fill=BOTH, expand=True)

    def widgets(self):
        self.img_btn_lapis = PhotoImage(file="images/lapis.png") #Para esse tamanho de botão, a imagem precisa ter 24px
        self.botao_lapis = Button(
            self.frame_lateral,
            image=self.img_btn_lapis,
            bg=self.cinza_medio,
            relief=RAISED,
            activebackground=self.cinza_escuro,
            border=1)
        self.botao_lapis.place(x=10, y=25, width=32, height=32)
    
        self.img_btn_borracha = PhotoImage(file="images/borracha.png")
        self.botao_borracha = Button(
            self.frame_lateral,
            image=self.img_btn_borracha,
            bg=self.cinza_medio,
            relief=RAISED,
            activebackground=self.cinza_escuro,
            border=1)
        self.botao_borracha.place(x=45, y=25, width=32, height=32)

        self.img_btn_balde_tinta = PhotoImage(file="images/balde_tinta.png")
        self.botao_balde_tinta = Button(
            self.frame_lateral,
            image=self.img_btn_balde_tinta,
            bg=self.cinza_medio,
            relief=RAISED,
            activebackground=self.cinza_escuro,
            border=1)
        self.botao_balde_tinta.place(x=80, y=25, width=32, height=32)

        self.img_btn_linha = PhotoImage(file="images/linha.png")
        self.botao_linha = Button(
            self.frame_lateral,
            image=self.img_btn_linha,
            bg=self.cinza_medio,
            relief=RAISED,
            activebackground=self.cinza_escuro,
            border=1)
        self.botao_linha.place(x=10, y=90, width=32, height=32)

        self.img_btn_circulo = PhotoImage(file="images/circulo.png")
        self.botao_circulo = Button(
            self.frame_lateral,
            image=self.img_btn_circulo,
            bg=self.cinza_medio,
            relief=RAISED,
            activebackground=self.cinza_escuro,
            border=1)
        self.botao_circulo.place(x=45, y=90, width=32, height=32)

        self.img_btn_oval = PhotoImage(file="images/oval.png")
        self.botao_oval = Button(
            self.frame_lateral,
            image=self.img_btn_oval,
            bg=self.cinza_medio,
            relief=RAISED,
            activebackground=self.cinza_escuro,
            border=1)
        self.botao_oval.place(x=80, y=90, width=32, height=32)

        self.img_btn_quadrado = PhotoImage(file="images/quadrado.png")
        self.botao_quadrado = Button(
            self.frame_lateral,
            image=self.img_btn_quadrado,
            bg=self.cinza_medio,
            relief=RAISED,
            activebackground=self.cinza_escuro,
            border=1)
        self.botao_quadrado.place(x=10, y=125, width=32, height=32)

        self.img_btn_retangulo = PhotoImage(file="images/retangulo.png")
        self.botao_retangulo = Button(
            self.frame_lateral,
            image=self.img_btn_retangulo,
            bg=self.cinza_medio,
            relief=RAISED,
            activebackground=self.cinza_escuro,
            border=1)
        self.botao_retangulo.place(x=45, y=125, width=32, height=32)

    def widgets_cores(self):
        self.botao_preto = Button(
            self.frame_lateral,
            bg=self.preto,
            relief=RIDGE,
            activebackground=self.cinza_escuro,
            border=1)
        self.botao_preto.config(command=lambda c=self.preto: (self.controller.selecionaCor(c) if self.controller else self.selecionaCor(c)))
        self.botao_preto.place(x=80, y=600, width=32, height=32)

        self.botao_branco = Button(
            self.frame_lateral,
            bg=self.branco,
            relief=RIDGE,
            activebackground=self.cinza_escuro,
            border=1)
        self.botao_branco.config(command=lambda c=self.branco: (self.controller.selecionaCor(c) if self.controller else self.selecionaCor(c)))
        self.botao_branco.place(x=10, y=600, width=32, height=32)

        self.botao_cinza_escuro = Button(
            self.frame_lateral,
            bg=self.cinza_escuro,
            relief=RIDGE,
            activebackground=self.cinza_escuro,
            border=1)
        self.botao_cinza_escuro.config(command=lambda c=self.cinza_escuro: (self.controller.selecionaCor(c) if self.controller else self.selecionaCor(c)))
        self.botao_cinza_escuro.place(x=45, y=600, width=32, height=32)

        self.botao_vermelho = Button(
            self.frame_lateral,
            bg=self.vermelho,
            relief=RIDGE,
            activebackground=self.cinza_escuro,
            border=1)
        self.botao_vermelho.config(command=lambda c=self.vermelho: (self.controller.selecionaCor(c) if self.controller else self.selecionaCor(c)))
        self.botao_vermelho.place(x=10, y=635, width=32, height=32)

        self.botao_laranja = Button(
            self.frame_lateral,
            bg=self.laranja,
            relief=RIDGE,
            activebackground=self.cinza_escuro,
            border=1)
        self.botao_laranja.config(command=lambda c=self.laranja: (self.controller.selecionaCor(c) if self.controller else self.selecionaCor(c)))
        self.botao_laranja.place(x=45, y=635, width=32, height=32)

        self.botao_amarelo = Button(
            self.frame_lateral,
            bg=self.amarelo,
            relief=RIDGE,
            activebackground=self.cinza_escuro,
            border=1)
        self.botao_amarelo.config(command=lambda c=self.amarelo: (self.controller.selecionaCor(c) if self.controller else self.selecionaCor(c)))
        self.botao_amarelo.place(x=80, y=635, width=32, height=32)

        self.botao_verde = Button(
            self.frame_lateral,
            bg=self.verde,
            relief=RIDGE,
            activebackground=self.cinza_escuro,
            border=1)
        self.botao_verde.config(command=lambda c=self.verde: (self.controller.selecionaCor(c) if self.controller else self.selecionaCor(c)))
        self.botao_verde.place(x=10, y=670, width=32, height=32)

        self.botao_verde_claro = Button(
            self.frame_lateral,
            bg=self.verde_claro,
            relief=RIDGE,
            activebackground=self.cinza_escuro,
            border=1)
        self.botao_verde_claro.config(command=lambda c=self.verde_claro: (self.controller.selecionaCor(c) if self.controller else self.selecionaCor(c)))
        self.botao_verde_claro.place(x=45, y=670, width=32, height=32)

        self.botao_ciano = Button(
            self.frame_lateral,
            bg=self.ciano,
            relief=RIDGE,
            activebackground=self.cinza_escuro,
            border=1)
        self.botao_ciano.config(command=lambda c=self.ciano: (self.controller.selecionaCor(c) if self.controller else self.selecionaCor(c)))
        self.botao_ciano.place(x=80, y=670, width=32, height=32)

        self.botao_azul = Button(
            self.frame_lateral,
            bg=self.azul,
            relief=RIDGE,
            activebackground=self.cinza_escuro,
            border=1)
        self.botao_azul.config(command=lambda c=self.azul: (self.controller.selecionaCor(c) if self.controller else self.selecionaCor(c)))
        self.botao_azul.place(x=10, y=705, width=32, height=32)

        self.botao_roxo = Button(
            self.frame_lateral,
            bg=self.roxo,
            relief=RIDGE,
            activebackground=self.cinza_escuro,
            border=1)
        self.botao_roxo.config(command=lambda c=self.roxo: (self.controller.selecionaCor(c) if self.controller else self.selecionaCor(c)))
        self.botao_roxo.place(x=45, y=705, width=32, height=32)

        self.botao_rosa = Button(
            self.frame_lateral,
            bg=self.rosa,
            relief=RIDGE,
            activebackground=self.cinza_escuro,
            border=1)
        self.botao_rosa.config(command=lambda c=self.rosa: (self.controller.selecionaCor(c) if self.controller else self.selecionaCor(c)))
        self.botao_rosa.place(x=80, y=705, width=32, height=32)

    def selecionaCor(self, cor):
        # Se não houver controller, a própria classe guarda a cor
        self.cor = cor






janela = Menu()