from dataclasses import dataclass

@dataclass
class Ferramentas:
    tipo_ferramenta: str = "lapis"

    def selecionar_ferramenta(self, ferramenta):
        self.tipo_ferramenta = ferramenta