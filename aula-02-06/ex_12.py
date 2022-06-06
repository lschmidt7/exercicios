n = int(input("Informe um valor: "))

primeiro = 1
segundo = 1

print(f'{primeiro}, ')
print(f'{segundo}, ')

for i in range(n):
    aux = segundo
    segundo = primeiro + segundo
    primeiro = aux
    print(f'{segundo}, ')