n1 = int(input())
n2 = int(input())

if n1 > n2:
    lista = [n1, n2]
    lista.reverse()
    n1 = lista[0]
    n2 = lista[1]

for i in range(n1 + 1, n2):
    if (i % 5) == 2 or (i % 5) == 3:
        print(i)