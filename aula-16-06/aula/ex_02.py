from Retangulo import Retangulo

base = int(input('Informe o valor da base do retângulo: '))
altura = int(input('Informe o valor da altura do retângulo: '))

ret = Retangulo(base, altura)

pisos = ret.area()

rodapes = ret.perimetro()

print(f'Pisos (1 x 1 m²): {pisos}')
print(f'Rodapes (1 m): {rodapes}')