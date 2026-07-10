class BaldeTinta:
    def __init__(self):

        self.encontrar_figura = encontrar_figura
        self.cor_preenchimento = cor_preenchimento

    def preencher(self, event):
        ids = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)

        for id_canvas in ids:
            figura = self.encontrar_figura(id_canvas)

        if figura:
            figura.cor_preenchimento = self.cor_preenchimento

        self.desenhar_figuras()