# vermelho + azul = roxo;
# vermelho + amarelo = laranja;
# azul + amarelo = verde.


cor1 = input("Informe a primeira cor")
cor2 = input("Informe a segunda cor")

if cor1 == 'vermelho':
    if cor2 == 'azul':
        print('roxo')
    elif cor2 == 'amarelo':
        print('laranja')

elif cor1 == 'azul':
    if cor2 == 'vermelho':
        print('roxo')
    elif cor2 == 'amarelo':
        print('verde')

elif cor1 == 'amarelo':
    if cor2 == 'azul':
        print('verde')
    elif cor2 == 'vermelho':
        print('laranja')