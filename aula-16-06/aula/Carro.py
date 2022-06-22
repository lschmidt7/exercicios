
# definição da classe carro
class Carro:

    def __init__(self, numero_rodas, cor='preto'):
        self.numero_rodas = numero_rodas
        self.cor = cor

    def acelerar(self, velocidade):
        print(f"Acelerando meu carro de {self.numero_rodas} rodas a {velocidade} km/h")