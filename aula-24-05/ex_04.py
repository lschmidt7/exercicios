print("Digite o número de livros comprados pelo cliente: ")
livros = int(input())

pontos = 0

if livros == 1:
    pontos = 5
elif livros == 2:
    pontos = 15
elif livros == 3:
    pontos = 30
elif livros >= 4:
    pontos = 60

print("Pontuação do cliente: {} pontos".format(pontos))