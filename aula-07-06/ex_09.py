from random import randint

tabuleiro = [ [0] * 20 ] * 20

# distribuindo os navios
for linha in range(20):
    coluna = randint(0,19)
    tabuleiro[linha][coluna] = 1

tentativas = 0
acertos = 0

sequencia_acertos = 0
maior_sequencia_acertos = 0

while tentativas <= 35 or acertos < 20:
    linha = int(input("Informe a linha: "))
    coluna = int(input("Informe a coluna: "))
    if tabuleiro[linha][coluna] == 1:
        print("Você acertou um navio!")
        tabuleiro[linha][coluna] = 0
        acertos +=1
        sequencia_acertos += 1
    else:
        if sequencia_acertos > maior_sequencia_acertos:
            maior_sequencia_acertos = sequencia_acertos
            sequencia_acertos = 0
        print("Infelizmente você errou!")
    tentativas+=1

total = tentativas + acertos

estatisticas = {
    'acertos_agua': tentativas - acertos,
    'acertos_navio': acertos,
    'porcentagem_agua': (tentativas - acertos) / total,
    'porcentagem_navio': acertos / total,
    'acertos_ininterruptos': maior_sequencia_acertos
}

if acertos == 20:
    print("Parabéns você ganhou!")
else:
    print("Continue tentando!")