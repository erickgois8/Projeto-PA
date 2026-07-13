class Estado:
    def __init__(self):
        self.__modo_cor = "borda"
        self.__cor_borda = "#000000"
        self.__cor_preenchimento = None
        self.__espessura = 3
    
    @property
    def modo_cor(self):
        return self.__modo_cor
    
    @property
    def cor_borda(self):
        return self.__cor_borda
    
    @property
    def cor_preenchimento(self):
        return self.__cor_preenchimento
    
    @property
    def espessura(self):
        return self.__espessura

    def selecionar_modo_cor(self, modo_cor):
        self.__modo_cor = modo_cor

    def selecionar_cor(self, cor):
        if self.__modo_cor == "borda":
            self.__cor_borda = cor
        
        elif self.__modo_cor == "preenchimento":
            self.__cor_preenchimento = cor

    def limpar_cor(self):
        self.__cor_preenchimento = None  