lista = []

for i in range(100):
    lista.append(float(input()))

for j in range(len(lista)):
    if lista[j] <= 10:
        print('A[%d] = %.1f' % (j, lista[j]))