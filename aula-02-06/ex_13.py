
n = int(input("Qual será o n-ésimo termo da série: "))

i = 1

for impar in range(1, n):
    print(f'{i}/{impar}')
    i+=1