
mensagens = int(input("Informe o total de mensagens enviadas: "))

preco = 5

if mensagens > 60 and mensagens <= 180:
    preco += (mensagens - 60) * 0.05
elif mensagens > 180:
    preco += 120 * 0.05
    preco += (mensagens - 180) * 0.1

preco += 0.12 * preco

print("Valor Final: R${}".format(preco))