nValor = int(input())
listaValores = []
counter = 0

for i in range(1000):
    
    listaValores.append(counter)
    counter += 1

    if counter == nValor: counter = 0

for k in range(len(listaValores)):
    print('N[%d] = %d' % (k, listaValores[k]))