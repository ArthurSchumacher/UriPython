lista = []

for i in range(10):
    lista.append(int(input()))

    if lista[i] <= 0: lista[i] = 1

for j in range(len(lista)):
    print('X[%d] = %d' % (j, lista[j]))