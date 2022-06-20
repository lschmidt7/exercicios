# v = (4.0 / 3.0) * ℼ * r³

from math import pi

def calcula_volume_esfera(raio):
    volume = (4/3) * pi * pow(raio, 3)
    return volume

raio = float(input('Informe o raio de uma esfera: '))

volume = calcula_volume_esfera(raio)

print(f'Volume: {volume}')