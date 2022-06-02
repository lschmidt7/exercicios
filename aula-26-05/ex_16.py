lado1 = float(input("Informe o lado 1 do tringulo"))
lado2 = float(input("Informe o lado 2 do tringulo"))
lado3 = float(input("Informe o lado 3 do tringulo"))

if lado1 == lado2 and lado2 == lado3:
    print("Equilatero")
elif lado1 == lado2 and lado2 != lado3 or lado2 == lado3 and lado3 != lado1 or lado3 == lado1 and lado1 != lado2:
    print("Isóceles")
else:
    print("Escaleno")