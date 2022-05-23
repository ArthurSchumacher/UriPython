nValor = float(input())
listaValores = []
listaValores.append(nValor)

for i in range(1, 100):
    listaValores.append(nValor / 2)
    
    nValor /= 2

for j in range(len(listaValores)):
    print('N[%d] = %.4f' % (j, listaValores[j]))