from BombaCombustivel import BombaCombustivel

bomba_combustivel = BombaCombustivel('gasolina', 7.4, 500)

bomba_combustivel.abastecer_por_litro(5)

print(bomba_combustivel.quantidade_combustivel)

bomba_combustivel.abastecer_por_valor(50)

print(f'{bomba_combustivel.quantidade_combustivel}')