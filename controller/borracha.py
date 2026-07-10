class Borracha:
    def __init__(self,raio= 5):
        self.raio = raio

    def usar(self, canvas, figuras, figura, event):
    
        x1 = event.x - self.raio
        y1 = event.y - self.raio
        x2 = event.x + self.raio
        y2 = event.y + self.raio

        
        ids = self.canvas.find_overlapping(x1, y2, x2, y2)

        for figura in self.figuras[:]:
            if figura.id in ids:
                self.figuras.remove(figura)
            
        self.desenhar_figuras()


















