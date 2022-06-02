quantidade = int(input("Informe a quantidade adquirida do produto: "))
preco = float(input("Informe o preço unitário do produto: "))

total = quantidade * preco

if quantidade <= 5:
    total -= total * 0.02
elif quantidade > 5 and quantidade <= 10:
    total -= total * 0.03
else:
    total -= total * 0.05

print("Valor total: {}".format(total))