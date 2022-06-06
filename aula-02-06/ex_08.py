# Escreva um programa que leia a idade e salário de 10 pessoas. Informe em seguida:
# Qual é a média de idade entre as pessoas?
# Quantas pessoas há por faixa etária, considerando: 
# jovens < 18
# 18 <= adultos < 60
# idosos >= 60
# Em seguida, mostre qual é a faixa etária que acumula o maior salário.

media_idade = 0

jovens = 0
adultos = 0
idosos = 0

salario_jovens = 0
salario_adultos = 0
salario_idosos = 0

for i in range(10):
    
    idade = int(input("Informe sua idade: "))
    salario = float(input("Informe seu salario: "))
    media_idade += idade

    if idade < 18:
        jovens += 1
        salario_jovens += salario
    elif 18 <= idade < 60:
        adultos += 1
        salario_adultos += salario
    else:
        idosos += 1
        salario_idosos += salario

print(f"Média de idade: {media_idade}")
print(f"Jovens: {jovens}")
print(f"Adultos: {adultos}")
print(f"Idosos: {idosos}")

if salario_jovens > salario_idosos and salario_jovens > salario_adultos:
    print("Jovens tem o maior salário")
elif salario_adultos > salario_idosos and salario_adultos > salario_jovens:
    print("Adultos tem o maior salário")
elif salario_idosos > salario_jovens and salario_jovens > salario_adultos:
    print("Idosos tem o maior salário")