# Faça um programa que peça o nome e as duas notas de 5 alunos, 
# calcule a média das notas e armazene nome e média cada uma em uma lista, 
# ao final imprima o nome e o número de alunos com média maior ou igual a 7.0.

nomes = []
medias = []

for i in range(5):
    nome = input("Digite o nome do aluno: ")
    nota1 = float("Digite a nota 1 do aluno: ")
    nota2 = float("Digite a nota 2 do aluno: ")

    media = (nota1 + nota2) / 2

    medias.append(media)

for i in range(5):
    if medias[i] >= 7:
        print(f"Aluno: {nomes[i]}, Media: {medias[i]}")