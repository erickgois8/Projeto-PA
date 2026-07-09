from dataclasses import dataclass

@dataclass
class Cores:
    modo: str = "borda"
    borda: str = "#000000"
    preenchimento: str = ""

    def selecionar_modo(self, modo):
        self.modo = modo

    def selecionar_cor(self, modo, cor):
        if modo == "borda":
            self.borda = cor

        elif modo == "preenchimento":
            self.preenchimento = cor