
class Conta:

    def __init__(self, numero_conta, nome_correntista, saldo = 0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
    
    def alterar_nome(self, nome):
        self.nome = nome
    
    def deposito(self, valor):
        self.saldo += valor
    
    def saque(self, valor):
        if self.saldo - valor >= 0:
            self.saldo -= valor
        else:
            print(f"Saldo insuficiente para retirada de {valor}!")
    
    def mosta_saldo(self):
        print(f'R$ {self.saldo}')