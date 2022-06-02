nota1 = float(input("Informe a nota do 1º bimestre"))
nota2 = float(input("Informe a nota do 2º bimestre"))
nota3 = float(input("Informe a nota do 3º bimestre"))
nota4 = float(input("Informe a nota do 4º bimestre"))

media = (nota1 + nota2 + nota3 + nota4) / 4

numero_aulas = int(input("Informe a quantidade de aulas: "))
numero_faltas = int(input("Informe a quantidade de faltas: "))

percentual_faltas = numero_faltas / numero_aulas

if percentual_faltas > 0.25:
    print("Reprovado por faltas")
elif media < 7:
    print("Reprovado por nota")
else:
    print("Aprovado")