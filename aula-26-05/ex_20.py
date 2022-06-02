
nota1 = int(input("Informe a primeira nota do semestre: "))
nota2 = int(input("Informe a segunda nota do semestre: "))

media = (nota1 + nota2) / 2

conceito = ''

if media >=9:
    conceito = 'A'
elif media >= 7.5 and media <= 8.9:
    conceito = 'B'
elif media >= 6 and media <= 7.4:
    conceito = 'C'
elif media >= 4 and media <= 5.9:
    conceito = 'D'
elif media >= 0 and media <= 3.9:
    conceito = 'E'

print(f"Conceito: {conceito}")

if conceito == 'A' or conceito == 'B' or conceito == 'C':
    print("Aprovado")
else:
    print("Reprovado")