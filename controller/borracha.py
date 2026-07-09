class Borracha:
    def __init__(self, raio=5):
        self.raio = raio

    def usar(self, x, y, model, view):
        xi, yi = x - self.raio, y - self.raio
        xf, yf = x + self.raio, y + self.raio

        
        ids_afetados = view.obter_ids_sobrepostos(xi, yi, xf, yf)

        if ids_afetados:
            model.remover_figuras_por_ids(ids_afetados)
            return True 
            
        return False 


















