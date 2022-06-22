import csv

f = open('compras.csv')
csv_reader = csv.reader(f, delimiter=',')

data = list(csv_reader)

index = 1

for linha in data[index:]:
    data[index][2] = int(data[index][2])
    data[index][4] = int(data[index][4])
    data[index][5] = int(data[index][5])
    index += 1

print(data[0])
print(data[4])