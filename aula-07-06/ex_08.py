from random import randint

tabuleiro = []

for i in range(20):
    tabuleiro.append([])
    for j in range(20):
        tabuleiro[i].append(0)

# linha = 
# tabuleiro = [ [0] * 20 ] * 20

# # distribuindo os navios
for linha in range(20):
    coluna = randint(0,19)
    tabuleiro[linha][coluna] = 1

tentativas = 0
acertos = 0

while tentativas <= 35 or acertos < 20:
    linha = int(input("Informe a linha: "))
    coluna = int(input("Informe a coluna: "))
    if tabuleiro[linha][coluna] == 1:
        print("Você acertou um navio!")
        tabuleiro[linha][coluna] = 0
        acertos += 1
    else:
        print("Infelizmente você errou!")
    tentativas += 1

if acertos == 20:
    print("Parabéns você ganhou!")
else:
    print("Continue tentando!")