
class BombaCombustivel:

    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros = valor / self.valor_litro
        print(f'Você abasteceu {litros:.2} litros em um total de R$ {valor}')
        self.alterar_quantidade_combustivel(litros)

    def abastecer_por_litro(self, litros):
        valor = litros * self.valor_litro
        print(f'Você abasteceu {litros} litros em um total de R$ {valor}')
        self.alterar_quantidade_combustivel(litros)

    def alterar_valor(self, valor_litro):
        self.valor_litro = valor_litro

    def alterar_combustivel(self, tipo_combustivel):
        self.tipo_combustivel = tipo_combustivel

    def alterar_quantidade_combustivel(self, litros):
        if litros <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros
        else:
            print('Quantidade de litros insuficientes')
