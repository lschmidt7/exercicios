from Ret import Ret
from Ponto import Ponto

ret = Ret()

ret.ponto_1 = Ponto(4,3) 
ret.ponto_2 = Ponto(10,6)

ponto_central = ret.centro()

print(type(ponto_central))

ponto_central.exibe()