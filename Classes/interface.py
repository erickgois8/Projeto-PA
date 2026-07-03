from figura import Figura
from linha import Linha
from retangulo import Retangulo
from quadrado import Quadrado
from oval import Oval
from circulo import Circulo
from lapis import Lapis
from borracha import Borracha

from tkinter import *
from tkinter import ttk


class Interface(): #podemos dar um nome melhor dps
    cinza_escuro = "#808080"
    cinza_medio = "#C0C0C0"
    branco = "#FFFFFF"
    preto = "#000000"

    ferramenta = None
    cor = None
    figuras = []
    figura_nova = None

# ----- ATRIBUTO ROOT DA CLASSE INTERFACE ----- #
    def __init__(self):
        self.root = Tk()

# ----- MÉTODO PARA CONFIGURAR NOME, FORMATO E ÍCONE DA JANELA ----- #
    def config(self):
        self.root.title("Meu paint")
        self.root.geometry("1920x1080")

        # Adaptação do ícone da janela para que seja possível rodar o programa em linux também já que ele não reconhece o ícone .ico
        self.icone = PhotoImage(file="/home/erick/Downloads/icone.png")
        self.root.iconphoto(False, self.icone)

        self.root.configure(bg=self.cinza_escuro)

# ----- MÉTODO PARA CONFIGURAÇÃO DO FRAME LATERAL (EM CINZA) ----- #
    def frames(self):
        self.frame_lateral = Frame(self.root, bg=self.cinza_medio, width=120, height=1080)
        self.frame_lateral.pack(side=LEFT, fill=Y)

# ----- CONFIGURAÇÃO DO CANVAS ----- #
    def canvas(self):
        self.canvas = Canvas(self.root, bg=self.branco, width=1770, height=1080)

        #Essa parte me garante que o canva estará possicionado corretamente na tela, e que ele se adaptará ao tamanho da janela caso o usuário a redimensione.
        self.canvas.pack(side=RIGHT, fill=BOTH, expand=True)

# ----- CONFIGURAÇÃO DOS WIDGETS ----- #
    def widgets(self):
        # Lápis
        self.img_btn_lapis = PhotoImage(file="/home/erick/Downloads/lapis.png") #Para esse tamanho de botão, a imagem precisa ter 24px
        self.botao_lapis = Button(
            self.frame_lateral,
            image=self.img_btn_lapis,
            bg=self.cinza_medio,
            relief=RAISED,
            activebackground=self.cinza_escuro,
            border=1,
            text="lapis",
            command=selecionaLapis)
        self.botao_lapis.place(x=10, y=10, width=32, height=32)
        
        # Borracha
        self.img_btn_borracha = PhotoImage(file="/home/erick/Downloads/borracha.png")
        self.botao_borracha = Button(
            self.frame_lateral,
            image=self.img_btn_borracha,
            bg=self.cinza_medio,
            relief=RAISED,
            activebackground=self.cinza_escuro,
            border=1)
        self.botao_borracha.place(x=45, y=10, width=32, height=32)

        # Balde de tinta
        self.img_btn_balde_tinta = PhotoImage(file="/home/erick/Downloads/balde_tinta.png")
        self.botao_balde_tinta = Button(
            self.frame_lateral,
            image=self.img_btn_balde_tinta,
            bg=self.cinza_medio,
            relief=RAISED,
            activebackground=self.cinza_escuro,
            border=1)
        self.botao_balde_tinta.place(x=80, y=10, width=32, height=32)

        
# ----- CONFIGURAÇÃO DAS FERRAMENTAS ----- #
        def selecionaLapis(self):
            self.ferramenta = "lapis"


# ----- FUNÇÕES DE DESENHO ----- #
    def iniciar_figura_nova(event): 