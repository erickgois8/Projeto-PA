from dataclasses import dataclass, field

@dataclass
class Borracha():
    pontos: list
    cor_borda: str

    def apagar(self, canvas, dash=()):
        canvas.createline(self.pontos, fill=self.cor_borda, dash=dash)
    
    def incompleta(self):
        return len(self.pontos) <= 1