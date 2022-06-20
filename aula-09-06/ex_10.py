
palavra = 'bandeira'

quantidade_letras = len(palavra)

palavra = [c for c in palavra]

palavra_escondida = ['_'] * quantidade_letras

pontuacao = 4

def exibe_palavra_escondida():
    palavra_atual = ''
    for letra in palavra_escondida:
        palavra_atual += letra
    print(palavra_atual)

def busca_posicao_letras(letra):
    indices = []
    for i, c in enumerate(palavra):
        if c == letra:
            indices.append(i)
    return indices

while pontuacao > 0 and '_' in palavra_escondida:
    print(f'\nChances Restantes: {pontuacao}')
    exibe_palavra_escondida()
    letra = input('Digite uma letra: ')
    posicoes = busca_posicao_letras(letra)
    if len(posicoes) == 0:
        print('Você errou!')
        pontuacao -= 1
    else:
        for i in posicoes:
            palavra_escondida[i] = palavra[i]
            palavra[i] = '_'

if pontuacao == 0:
    print("\nVocê perdeu, tente novamente!\n")
else:
    print("\nParabéns você ganhou!\n")