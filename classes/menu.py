from classes.lapis import Lapis
from classes.linha import Linha
from classes.retangulo import Retangulo
from classes.quadrado import Quadrado
from classes.oval import Oval
from classes.circulo import Circulo

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
    roxo = "#6a4c93"
    rosa = "#f49ac2"
    
    ferramenta = "lapis"
    modo_cor = "borda"
    cor_borda = preto
    cor_preenchimento = None
    figura_nova = None
    figuras = []

# ----- Criação do root ----- #
    def __init__(self):
        self.root = Tk()
        self.config()
        self.frames()
        self.canvas()
        self.widgets()
        self.widgets_cores()
    
# ----- CONFIGURAR NOME, FORMATO E ÍCONE DA JANELA ----- #
    def config(self):
        self.root.title("Meu paint")
        self.root.geometry("1920x1080")

        # Adaptação do ícone da janela para que seja possível rodar o programa em linux também já que ele não reconhece o ícone .ico
        self.icone = PhotoImage(file="images/icone.png")
        self.root.iconphoto(False, self.icone)

        self.root.configure(bg=self.cinza_escuro)

# ----- CONFIGURAÇÃO DO FRAME LATERAL (EM CINZA) ----- #
    def frames(self):
        self.frame_lateral = Frame(self.root, bg=self.cinza_medio, width=120, height=1080)
        self.frame_lateral.pack(side=LEFT, fill=Y)

# ----- CONFIGURAÇÃO DO CANVAS ----- #
    def canvas(self):
        self.canva = Canvas(self.root, bg=self.branco, width=1770, height=1080)

        # Posicionando o canvas corretamente e assegurando redimensinamento
        self.canva.pack(side=RIGHT, fill=BOTH, expand=True)

# ----- CONFIGURAÇÃO DOS WIDGETS ----- #
    def widgets(self):
        # Lápis
        self.img_btn_lapis = PhotoImage(file="images/lapis.png") # Para esse tamanho de botão, a imagem precisa ter 24px
        self.botao_lapis = Button(
            self.frame_lateral,
            image=self.img_btn_lapis,
            bg=self.cinza_medio,
            relief=RAISED,
            activebackground=self.cinza_escuro,
            border=1,
            command=lambda: self.selecionaFerramenta("lapis"))
        self.botao_lapis.place(x=10, y=25, width=32, height=32)
    
        # Borracha
        self.img_btn_borracha = PhotoImage(file="images/borracha.png")
        self.botao_borracha = Button(
            self.frame_lateral,
            image=self.img_btn_borracha,
            bg=self.cinza_medio,
            relief=RAISED,
            activebackground=self.cinza_escuro,
            border=1,
            command=lambda: self.selecionaFerramenta("borracha"))
        self.botao_borracha.place(x=45, y=25, width=32, height=32)

        # Balde de tinta
        self.img_btn_balde_tinta = PhotoImage(file="images/balde_tinta.png")
        self.botao_balde_tinta = Button(
            self.frame_lateral,
            image=self.img_btn_balde_tinta,
            bg=self.cinza_medio,
            relief=RAISED,
            activebackground=self.cinza_escuro,
            border=1,
            command=lambda: self.selecionaFerramenta("balde_tinta"))
        self.botao_balde_tinta.place(x=80, y=25, width=32, height=32)

        # Linha
        self.img_btn_linha = PhotoImage(file="images/linha.png")
        self.botao_linha = Button(
            self.frame_lateral,
            image=self.img_btn_linha,
            bg=self.cinza_medio,
            relief=RAISED,
            activebackground=self.cinza_escuro,
            border=1,
            command=lambda: self.selecionaFerramenta("linha"))
        self.botao_linha.place(x=10, y=90, width=32, height=32)

        # Círculo
        self.img_btn_circulo = PhotoImage(file="images/circulo.png")
        self.botao_circulo = Button(
            self.frame_lateral,
            image=self.img_btn_circulo,
            bg=self.cinza_medio,
            relief=RAISED,
            activebackground=self.cinza_escuro,
            border=1,
            command=lambda: self.selecionaFerramenta("circulo"))
        self.botao_circulo.place(x=45, y=90, width=32, height=32)

        # Oval
        self.img_btn_oval = PhotoImage(file="images/oval.png")
        self.botao_oval = Button(
            self.frame_lateral,
            image=self.img_btn_oval,
            bg=self.cinza_medio,
            relief=RAISED,
            activebackground=self.cinza_escuro,
            border=1,
            command=lambda: self.selecionaFerramenta("oval"))
        self.botao_oval.place(x=80, y=90, width=32, height=32)

        # Quadrado
        self.img_btn_quadrado = PhotoImage(file="images/quadrado.png")
        self.botao_quadrado = Button(
            self.frame_lateral,
            image=self.img_btn_quadrado,
            bg=self.cinza_medio,
            relief=RAISED,
            activebackground=self.cinza_escuro,
            border=1,
            command=lambda: self.selecionaFerramenta("quadrado"))
        self.botao_quadrado.place(x=10, y=125, width=32, height=32)

        # Retângulo
        self.img_btn_retangulo = PhotoImage(file="images/retangulo.png")
        self.botao_retangulo = Button(
            self.frame_lateral,
            image=self.img_btn_retangulo,
            bg=self.cinza_medio,
            relief=RAISED,
            activebackground=self.cinza_escuro,
            border=1,
            command=lambda: self.selecionaFerramenta("retangulo"))
        self.botao_retangulo.place(x=45, y=125, width=32, height=32)

        # Figuras com borda colorida
        self.lbl_figuras_borda = Label(
            self.frame_lateral,
            text="Cor da borda",
            bg=self.cinza_medio,
            fg=self.preto,
            font=("Arial", 7, "bold"))
        self.lbl_figuras_borda.place(x=28, y=754)
        self.btn_fig_borda = Button(
            self.frame_lateral,
            bg=self.cinza_medio,
            relief=RAISED,
            activebackground=self.cinza_escuro,
            border=1,
            command=lambda: self.selecionaModoCor("borda"))
        self.btn_fig_borda.place(x=20, y=770, width=80, height=32)

        # Figuras preenchidas com cores
        self.lbl_figuras = Label(
            self.frame_lateral,
            text="Cor do preenchimento",
            bg=self.cinza_medio,
            fg=self.preto,
            font=("Arial", 7, "bold"))
        self.lbl_figuras.place(x=8, y=814)
        self.btn_fig_preenchida = Button(
            self.frame_lateral,
            bg=self.cinza_medio,
            relief=RAISED,
            activebackground=self.cinza_escuro,
            border=1,
            command=lambda: self.selecionaModoCor("preenchimento"))
        self.btn_fig_preenchida.place(x=10, y=830, width=80, height=32)

        # Botão de sem preenchimento
        self.img_btn_sem_preenchimento = PhotoImage(file="images/sem_preenchimento.png")
        self.btn_sem_preenchimento = Button(
            self.frame_lateral,
            image=self.img_btn_sem_preenchimento,
            bg=self.cinza_medio,
            relief=RAISED,
            activebackground=self.cinza_escuro,
            border=1,
            command=lambda: self.selecionaCor(None, self.modo_cor))
        self.btn_sem_preenchimento.place(x=90, y=835, width=24, height=24)

        # Botão desfazer
        self.img_btn_desfazer = PhotoImage(file="images/desfazer.png")
        self.btn_desfazer = Button(
            self.frame_lateral,
            image=self.img_btn_desfazer,
            bg=self.cinza_medio,
            relief=RAISED,
            activebackground=self.cinza_escuro,
            border=1,
            command=lambda: self.desfazer())
        self.btn_desfazer.place(x=15, y=950, width=32, height=32)

        # Botão refazer
        self.img_btn_refazer = PhotoImage(file="images/refazer.png")
        self.btn_refazer = Button(
            self.frame_lateral,
            image=self.img_btn_refazer,
            bg=self.cinza_medio,
            relief=RAISED,
            activebackground=self.cinza_escuro,
            border=1,
            command=lambda: self.refazer())
        self.btn_refazer.place(x=70, y=950, width=32, height=32)

# ----- Botões de cores ----- #
    def widgets_cores(self):
        # Preto
        self.botao_preto = Button(
            self.frame_lateral,
            bg=self.preto,
            relief=RIDGE,
            activebackground=self.cinza_escuro,
            border=1,
            command=lambda: self.selecionaCor(self.preto, self.modo_cor))
        self.botao_preto.place(x=80, y=600, width=32, height=32)

        # Branco
        self.botao_branco = Button(
            self.frame_lateral,
            bg=self.branco,
            relief=RIDGE,
            activebackground=self.cinza_escuro,
            border=1,
            command=lambda: self.selecionaCor(self.branco, self.modo_cor))
        self.botao_branco.place(x=10, y=600, width=32, height=32)

        # Cinza escuro
        self.botao_cinza_escuro = Button(
            self.frame_lateral,
            bg=self.cinza_escuro,
            relief=RIDGE,
            activebackground=self.cinza_escuro,
            border=1,
            command=lambda: self.selecionaCor(self.cinza_escuro, self.modo_cor))
        self.botao_cinza_escuro.place(x=45, y=600, width=32, height=32)

        # Vermelho
        self.botao_vermelho = Button(
            self.frame_lateral,
            bg=self.vermelho,
            relief=RIDGE,
            activebackground=self.cinza_escuro,
            border=1,
            command=lambda: self.selecionaCor(self.vermelho, self.modo_cor))
        self.botao_vermelho.place(x=10, y=635, width=32, height=32)

        # Laranja
        self.botao_laranja = Button(
            self.frame_lateral,
            bg=self.laranja,
            relief=RIDGE,
            activebackground=self.cinza_escuro,
            border=1,
            command=lambda: self.selecionaCor(self.laranja, self.modo_cor))
        self.botao_laranja.place(x=45, y=635, width=32, height=32)

        # Amarelo
        self.botao_amarelo = Button(
            self.frame_lateral,
            bg=self.amarelo,
            relief=RIDGE,
            activebackground=self.cinza_escuro,
            border=1,
            command=lambda: self.selecionaCor(self.amarelo, self.modo_cor))
        self.botao_amarelo.place(x=80, y=635, width=32, height=32)

        # Verde
        self.botao_verde = Button(
            self.frame_lateral,
            bg=self.verde,
            relief=RIDGE,
            activebackground=self.cinza_escuro,
            border=1,
            command=lambda: self.selecionaCor(self.verde, self.modo_cor))
        self.botao_verde.place(x=10, y=670, width=32, height=32)

        # Verde claro
        self.botao_verde_claro = Button(
            self.frame_lateral,
            bg=self.verde_claro,
            relief=RIDGE,
            activebackground=self.cinza_escuro,
            border=1,
            command=lambda: self.selecionaCor(self.verde_claro, self.modo_cor))
        self.botao_verde_claro.place(x=45, y=670, width=32, height=32)

        # Ciano
        self.botao_ciano = Button(
            self.frame_lateral,
            bg=self.ciano,
            relief=RIDGE,
            activebackground=self.cinza_escuro,
            border=1,
            command=lambda: self.selecionaCor(self.ciano, self.modo_cor))
        self.botao_ciano.place(x=80, y=670, width=32, height=32)

        # Azul
        self.botao_azul = Button(
            self.frame_lateral,
            bg=self.azul,
            relief=RIDGE,
            activebackground=self.cinza_escuro,
            border=1,
            command=lambda: self.selecionaCor(self.azul, self.modo_cor))
        self.botao_azul.place(x=10, y=705, width=32, height=32)

        # Roxo
        self.botao_roxo = Button(
            self.frame_lateral,
            bg=self.roxo,
            relief=RIDGE,
            activebackground=self.cinza_escuro,
            border=1,
            command=lambda: self.selecionaCor(self.roxo, self.modo_cor))
        self.botao_roxo.place(x=45, y=705, width=32, height=32)

        # Rosa
        self.botao_rosa = Button(
            self.frame_lateral,
            bg=self.rosa,
            relief=RIDGE,
            activebackground=self.cinza_escuro,
            border=1,
            command=lambda: self.selecionaCor(self.rosa, self.modo_cor))
        self.botao_rosa.place(x=80, y=705, width=32, height=32)

# ----- FERRAMENTAS ----- #
    def selecionaCor(self, cor, modo_cor):
        if modo_cor == "borda":
            self.cor_borda = cor
        
        elif modo_cor == "preenchimento":
            self.cor_preenchimento = cor

    def selecionaFerramenta(self, ferramenta):
        self.ferramenta = ferramenta

# Seletor do modo cor

# Borracha (a implementar)

# Balde de tinta (a implementar)

# ----- ATALHOS (a implementar) ----- #

# ctrl + z
# ctrl + shif + z

# ----- FUNÇÕES DE DESENHO ----- #

    # Quando o mouse é pressionado
    def iniciar_figura_nova(self, event):
        if self.ferramenta == "linha":
            self.figura_nova = Linha(event.x, event.y, event.x, event.y, self.cor_borda)

        elif self.ferramenta == "lapis":
            self.figura_nova = Lapis([(event.x, event.y)], self.cor_borda)

        elif self.ferramenta == "oval":
            self.figura_nova = Oval(event.x, event.y, event.x, event.y, self.cor_borda, self.cor_preenchimento)
        
        elif self.ferramenta == "retangulo":
            self.figura_nova = Retangulo(event.x, event.y, event.x, event.y, self.cor_borda, self.cor_preenchimento)

        elif self.ferramenta == "quadrado":
            self.figura_nova = Quadrado(event.x, event.y, event.x, event.y, self.cor_borda, self.cor_preenchimento)

        elif self.ferramenta == "circulo":
            self.figura_nova = Circulo(event.x, event.y, event.x, event.y, self.cor_borda, self.cor_preenchimento)
    
    # Quando o mouse é movido
    def atualizar_figura_nova(self, event):   
        self.figura_nova.atualizar(event)

        self.desenhar_figuras()
        self.desenhar_figura_nova()
    
    # Quando o mouse é solto
    def incluir_figura_nova(self, event): 
        if not self.figura_nova.incompleta():
            self.figuras.append(self.figura_nova)

        self.desenhar_figuras()
        self.figura_nova = None

    # Permite que tenhamos nossas figuras armazenadas desenhadas e sem rastro
    def desenhar_figuras(self):
        self.canva.delete("all")

        for fig in self.figuras:
            fig.desenhar(self.canva)

    # Desenha a nova figura
    def desenhar_figura_nova(self):
        self.figura_nova.desenhar(self.canva, dash=(4,2))
