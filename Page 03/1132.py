n1 = int(input())
n2 = int(input())

if n1 > n2:
    lista = [n1, n2]
    lista.reverse()
    n1 = lista[0]
    n2 = lista[1]

sumValues = 0

for i in range(n1, n2 + 1):
    if (i % 13) != 0:
        sumValues += i

print(sumValues)