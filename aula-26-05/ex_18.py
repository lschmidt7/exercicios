# salários até R$ 280,00 (incluindo): aumento de 20%
# salários entre R$ 280,00 e R$ 700,00: aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
# salários de R$ 1500,00 em diante: aumento de 5% 

salario = float(input("Informe o salário: "))

if salario <= 280:
    reajuste = 0.2
    aumento = reajuste * salario
    novo_salario = salario + aumento
elif salario > 280 and salario <= 700:
    reajuste = 0.15
    aumento = reajuste * salario
    novo_salario = salario + aumento
elif salario > 700 and salario <= 1500:
    reajuste = 0.1
    aumento = reajuste * salario
    novo_salario = salario + aumento
else:
    reajuste = 0.05
    aumento = reajuste * salario
    novo_salario = salario + aumento

print("Salário antes do reajuste: R$ {}".format(salario))
print("Percentual de aumento: {}%".format(reajuste * 100))
print("Valor de aumento: R$ {}".format(aumento))
print("Novo Salário: R$ {}".format(novo_salario))