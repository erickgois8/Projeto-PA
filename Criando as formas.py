from tkinter import *
from tkinter import ttk

# Quando mouse é pressionado
def iniciar_figura_nova(event): 
    global figura_nova
    if tipo_figura_var.get() == 'Linha':
        figura_nova = ("linha", (event.x, event.y, event.x, event.y))
    elif tipo_figura_var.get() == "Rabisco":
        figura_nova = ("rabisco", [(event.x, event.y)])
    elif tipo_figura_var.get() == "Oval":
        figura_nova = ("Oval", (event.x, event.y, event.x, event.y)) #aqui estamos adicionando a opção oval igual fizemos com as outras formas
    elif tipo_figura_var.get() == "Retângulo":
        figura_nova = ("Retângulo", (event.x, event.y, event.x, event.y))
    elif tipo_figura_var.get() == "Quadrado":
        figura_nova = ("Quadrado", (event.x, event.y, event.x, event.y))
    else : # msm coisa de fazer tipo_figura_var.get() == "Circulo"
        figura_nova = ("Circulo", (event.x, event.y, event.x, event.y))

# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova
    if figura_nova[0] == "rabisco":
        figura_nova[1].append((event.x, event.y))
    elif figura_nova[0] == "linha":
        figura_nova = ("linha", (figura_nova[1][0], figura_nova[1][1], event.x, event.y))
    elif figura_nova[0] == "Circulo":
        figura_nova = ("Circulo", (figura_nova[1][0], figura_nova[1][1], event.x, event.y))
    elif figura_nova[0] == "Oval":
        figura_nova = ("Oval", (figura_nova[1][0], figura_nova[1][1], event.x, event.y))
    elif figura_nova[0] == "Retângulo":
        figura_nova = ("Retângulo", (figura_nova[1][0], figura_nova[1][1], event.x, event.y))
    elif figura_nova[0] == "Quadrado": #aq temos que fazer ter o msm tamanho em todos os lados,
            x_inicio, y_inicio = figura_nova[1][0], figura_nova[1][1]

            dist_x = event.x- x_inicio #aq descobrimos o tamanho dos lados
            dist_y = event.y - y_inicio
            tamanho = max(abs(dist_x), abs(dist_y)) #aq pegamos o maior lado
            novo_x = x_inicio + tamanho * (1 if dist_x >= 0 else -1) #aq garantimos q o quadrado vai ser desenhado
            novo_y = y_inicio + tamanho * (1 if dist_y >= 0 else -1) #na posição certa
            figura_nova = ("Quadrado", (x_inicio, y_inicio, novo_x, novo_y))
    desenhar_figuras()
    desenhar_figura_nova()

# Quando mouse é solto
def incluir_figura_nova(event): 
    if not incompleta(figura_nova): # para evitar incluir figuras incompletas, como uma linha sem comprimento ou um rabisco com um único ponto
        figuras.append(figura_nova) 
    desenhar_figuras()

def desenhar_figuras():
    canvas.delete("all")
    for fig, values in figuras:
        if fig == "linha":
            canvas.create_line(values[0], values[1], values[2], values[3])
        elif fig == "Circulo":
            raio = ((values[0]- values[2])**2+ (values[1] - values[3])**2) ** 0.5
            canvas.create_oval(values[0]- raio, values[1]- raio, values[0]+ raio, values[1]+ raio)
        elif fig == "Oval":
            canvas.create_oval(values[0], values[1], values[2], values[3])
        elif fig == "Retângulo":
            canvas.create_rectangle(values[0], values[1], values[2], values[3])
        elif fig == "Quadrado":
            canvas.create_rectangle(values[0], values[1], values[2], values[3])
        else : # fig == "rabisco"
            canvas.create_line(values)

def desenhar_figura_nova():
    fig, values = figura_nova
    if fig == "linha":
        canvas.create_line(values[0], values[1], values[2], values[3], dash=(4, 2))
    elif fig == "Circulo":
        raio = ((values[0]- values[2])**2+ (values[1] - values[3])**2) ** 0.5
        canvas.create_oval((values[0]- raio, values[1]- raio, values[0]+ raio, values[1]+ raio), dash=(4,2))
    elif fig == "Oval":
        canvas.create_oval(values[0], values[1], values[2], values[3], dash=(4, 2))
    elif fig == "Retângulo":
        canvas.create_rectangle(values[0], values[1], values[2], values[3], dash= (4,2))
    elif fig == "Quadrado":
        canvas.create_rectangle(values[0], values[1], values[2], values[3], dash= (4,2))
    else : # fig == "rabisco"
        canvas.create_line(values, dash=(4, 2))

def incompleta(figura):
    fig, values = figura
    if fig == "rabisco":
        return len(values) <= 1
    else :
        return (values[0], values[1]) == (values[2], values[3]) #aq é melho inverter do q ficar dando or em todas as formas




#******* MAIN *******#

figuras = []       # Todas as figuras desenhadas
figura_nova = None # Figura que está sendo desenhada, mas ainda não foi incluída em figuras

root = Tk()
frame = Frame(root)

# Widgets arranjados com Layout grid dentro de frame
paddings = {'padx': 5, 'pady': 5} 

# label
label = ttk.Label(frame,  text='Linha, Circulo, Oval, Retângulo, Quadrado ou Rabisco:')
label.grid(column=0, row=0, sticky=W, **paddings)

# option menu
tipo_figura_var = StringVar(root) # Guarda o tipo de figura selecionado no option menu (já vou pegar o embalo e fazer quadrado tb)
option_menu = ttk.OptionMenu(frame, tipo_figura_var,
                             'Linha', 'Linha', 'Rabisco', "Circulo", "Oval", "Retângulo", "Quadrado") #aq linha é repetida pq é exigido deixar a opção padrão duas vezes
option_menu.grid(column=1, row=0, sticky=W, **paddings)

#*****Menu de cores*****#
label_cor = ttk.Label(frame, text="Cores")
cores_var = StringVar(root) #guarda a cor selecionada
option_menu_cores = ttk.OptionMenu(frame, cores_var,
                                   "Preto", "Preto", "Vermelho", "Verde", "Azul", "Amarelo", "Rosa", "Cor de burro quando foge")
option_menu_cores.grid(column=2, row=0, sticky=W, **paddings)

#*******************************************#
# Área de desenho
canvas = Canvas(frame, bg='white', width=600, height=600)
canvas.grid(column=0, row=1, columnspan=3, sticky=W, **paddings)

frame.pack()

# Eventos de mouse associados ao canvas - com seus callbacks
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

root.mainloop()
