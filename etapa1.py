from tkinter import *
from tkinter import ttk

# ----- Tradutor de cores ----- #
cores = {"Preto" : "#000000",
         "Vermelho" : "#FF0000",
         "Verde" : "#00FF00",
         "Azul" : "#0000FF",
         "Amarelo" : "#FFFF00",
         "Rosa" : "#FF007F",
         "Cor de burro quando foge" : "#654321"}

# ----- Funções de desenho ----- #

# Quando mouse é pressionado
def iniciar_figura_nova(event) : 
    global figura_nova

    cor_borda = cores[cores_borda_var.get()] # contorno_atual -> cor_borda para melhorar legibilidade
    cor_preenchimento = cores[cores_preenchimento_var.get()]

    if tipo_figura_var.get() == "Linha" :
        figura_nova = ("linha", (event.x, event.y, event.x, event.y), cor_borda, cor_preenchimento)

    elif tipo_figura_var.get() == "Rabisco" :
        figura_nova = ("rabisco", [(event.x, event.y)], cor_borda, cor_preenchimento)

    elif tipo_figura_var.get() == "Oval" :
        figura_nova = ("oval", (event.x, event.y, event.x, event.y), cor_borda, cor_preenchimento)

    elif tipo_figura_var.get() == "Retângulo" :
        figura_nova = ("retangulo", (event.x, event.y, event.x, event.y), cor_borda, cor_preenchimento)

    elif tipo_figura_var.get() == "Quadrado" :
        figura_nova = ("quadrado", (event.x, event.y, event.x, event.y), cor_borda, cor_preenchimento)

    elif tipo_figura_var.get() == "Círculo" :
        figura_nova = ("circulo", (event.x, event.y, event.x, event.y), cor_borda, cor_preenchimento)

# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event) :
    global figura_nova

    cor_borda = cores[cores_borda_var.get()]
    cor_preenchimento = cores[cores_preenchimento_var.get()] # Recuperando as cores

    if figura_nova[0] == "rabisco" :
        figura_nova[1].append((event.x, event.y))

    elif figura_nova[0] == "linha" :
        figura_nova = ("linha", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), cor_borda, cor_preenchimento)

    elif figura_nova[0] == "circulo" :
        figura_nova = ("circulo", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), cor_borda, cor_preenchimento)

    elif figura_nova[0] == "oval" :
        figura_nova = ("oval", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), cor_borda, cor_preenchimento)

    elif figura_nova[0] == "retangulo" :
        figura_nova = ("retangulo", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), cor_borda, cor_preenchimento)

    elif figura_nova[0] == "quadrado" : # Devemos criar lados de mesmo tamanho
            x_inicio, y_inicio = figura_nova[1][0], figura_nova[1][1]
            
            # Descobrindo tamanho dos lados
            dist_x = event.x - x_inicio
            dist_y = event.y - y_inicio

            # Buscando o maior lado
            tamanho = max(abs(dist_x), abs(dist_y))

            # Garantindo que o quadrado será desenhado
            novo_x = x_inicio + tamanho * (1 if dist_x >= 0 else -1)
            novo_y = y_inicio + tamanho * (1 if dist_y >= 0 else -1) 

            # Na posição certa
            figura_nova = ("quadrado", (x_inicio, y_inicio, novo_x, novo_y), cor_borda, cor_preenchimento)

    desenhar_figuras()
    desenhar_figura_nova()

# Quando mouse é solto
def incluir_figura_nova(event) : 
    if not incompleta(figura_nova) : # Para evitar incluir figuras incompletas, como uma linha sem comprimento ou um rabisco com um único ponto
        figuras.append(figura_nova)

    desenhar_figuras()

def desenhar_figuras() :
    canvas.delete("all")

    for fig, values, cB, cP in figuras :   # cB = cor da borda e cP = cor de preenchimento
        if fig == "linha" :
            canvas.create_line(values[0], values[1], values[2], values[3], fill=cB)

        elif fig == "circulo" :
            raio = ((values[0] - values[2]) ** 2 + (values[1] - values[3]) ** 2) ** 0.5
            canvas.create_oval(values[0] - raio, values[1] - raio, values[0] + raio, values[1] + raio, fill=cP, outline=cB)

        elif fig == "oval" :
            canvas.create_oval(values[0], values[1], values[2], values[3], fill=cP, outline=cB)

        elif fig == "retangulo" :
            canvas.create_rectangle(values[0], values[1], values[2], values[3], fill=cP, outline=cB)

        elif fig == "quadrado" :
            canvas.create_rectangle(values[0], values[1], values[2], values[3], fill=cP, outline=cB)

        elif fig == "rabisco" :
            canvas.create_line(values, fill=cB)

def desenhar_figura_nova() :
    fig, values, cB, cP = figura_nova

    if fig == "linha" :
        canvas.create_line(values[0], values[1], values[2], values[3], fill=cB, dash = (4, 2))

    elif fig == "circulo" :
        raio = ((values[0] - values[2]) ** 2 + (values[1] - values[3]) ** 2) ** 0.5
        canvas.create_oval((values[0] - raio, values[1] - raio, values[0] + raio, values[1] + raio), fill=cP, outline=cB, dash = (4,2))

    elif fig == "oval" :
        canvas.create_oval(values[0], values[1], values[2], values[3], fill=cP, outline=cB, dash = (4, 2))

    elif fig == "retangulo" :
        canvas.create_rectangle(values[0], values[1], values[2], values[3], fill=cP, outline=cB, dash = (4,2))

    elif fig == "quadrado" :
        canvas.create_rectangle(values[0], values[1], values[2], values[3], fill=cP, outline=cB, dash = (4,2))

    elif fig == "rabisco" :
        canvas.create_line(values, fill=cB, dash = (4, 2))

def incompleta(figura) :
    fig, values, cB, cP = figura

    if fig == "rabisco" :
        return len(values) <= 1


    # Invertendo para eliminar a necessidade do OR em todas as formas
    else :
        return (values[0], values[1]) == (values[2], values[3]) 



# ----- MAIN ----- #
figuras = []       # Todas as figuras desenhadas
figura_nova = None # Figura que está sendo desenhada, mas ainda não foi incluída em figuras

root = Tk()
frame = Frame(root)

# Widgets arranjados com Layout grid dentro de frame
paddings = {'padx': 5, 'pady': 5} 

# label
label = ttk.Label(frame,  text='Minha nova arte')
label.grid(column=0, row=0, sticky=W, **paddings)

# ----- Menu de Figuras ----- #
tipo_figura_var = StringVar(root) # Guarda o tipo de figura selecionado no option menu
option_menu = ttk.OptionMenu(frame, tipo_figura_var,
                             "Linha", "Linha", "Rabisco", "Círculo", "Oval", "Retângulo", "Quadrado") # Linha é repetido por exigência
option_menu.grid(column=1, row=0, sticky=W, **paddings)

# ----- Menu de cores (borda) ----- #
cores_borda_var = StringVar(root) # Guarda a cor selecionada
option_menu_cores_borda = ttk.OptionMenu(frame, cores_borda_var,
                                   "Preto", "Preto", "Vermelho", "Verde", "Azul", "Amarelo", "Rosa", "Cor de burro quando foge")
option_menu_cores_borda.grid(column=2, row=0, sticky=W, **paddings)

# ----- Menu de cores (preenchimento) ----- #
cores_preenchimento_var = StringVar(root)
option_menu_cores_preenchimento = ttk.OptionMenu(frame, cores_preenchimento_var,
                                    "Preto", "Preto", "Vermelho", "Verde", "Azul", "Amarelo", "Rosa", "Cor de burro quando foge")
option_menu_cores_preenchimento.grid(column=3, row=0, sticky=W, **paddings)

# ------------------------------------------------------------------- #

# Área de desenho
canvas = Canvas(frame, bg='white', width=1280, height=720)
canvas.grid(column=0, row=1, columnspan=3, sticky=W, **paddings)

frame.pack()

# Eventos de mouse associados ao canvas - com seus callbacks
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

root.mainloop()
