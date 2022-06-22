from Ponto import Ponto

class Ret:

    def __init__(self):
        self.ponto_1 = None
        self.ponto_2 = None
    
    def centro(self):
        ponto_central = Ponto()
        ponto_central.x = (self.ponto_1.x + self.ponto_2.x) / 2
        ponto_central.y = (self.ponto_1.y + self.ponto_2.y) / 2
        return ponto_central