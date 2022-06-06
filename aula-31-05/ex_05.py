
altura_chico = 1.5
altura_ze = 1.1

anos = 0

while altura_ze < altura_chico:
    altura_chico += 0.02
    altura_ze += 0.03
    anos += 1

print(f"Serão necessários {anos}")