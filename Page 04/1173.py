nValor = int(input())
lista = []
lista.append(nValor)

for i in range(9):
    lista.append(lista[i] * 2)

for j in range(len(lista)):
    print('N[%d] = %d' % (j, lista[j]))