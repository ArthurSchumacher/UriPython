def printArray(array, texto):
    for posicao, num in enumerate(array):
        print('%s[%d] = %d' % (texto, posicao, num))

valoresPares = []
valoresImpares = []

for i in range(15):
    nValor = int(input())

    if nValor % 2 == 0: 
        valoresPares.append(nValor)

        if len(valoresPares) == 5:
            printArray(valoresPares, 'par')
            valoresPares = []            

    if nValor % 2 != 0: 
        valoresImpares.append(nValor)

        if len(valoresImpares) == 5:
            printArray(valoresImpares, 'impar')
            valoresImpares = []     

printArray(valoresImpares, 'impar')
printArray(valoresPares, 'par')