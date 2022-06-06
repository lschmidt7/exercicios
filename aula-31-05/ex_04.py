media_salarial = 0
media_num_filhos = 0
maior_salario = -1
percentual_abaixo_2000 = 0


for i in range(5):
    salario = int(input("Informe o seu salário: "))
    num_filhos = int(input("Quantos filhos você tem? "))

    media_salarial += salario
    media_num_filhos += num_filhos

    if salario > maior_salario:
        maior_salario = salario
    
    if salario < 2000:
        percentual_abaixo_2000 += 1

percentual_abaixo_2000 /= 5

print(f"Média salarial: {media_salarial}")
print(f"Média do número de filhos: {media_num_filhos}")
print(f"Maior salário: {maior_salario}")
print(f"Percentual de salários abaixo de 2000: {percentual_abaixo_2000}")