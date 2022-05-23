nTestes = int(input())

for i in range(nTestes):
    nPrimo = int(input())
    nPrimoVerif = 0

    for j in range(1, nPrimo + 1):
        if (nPrimo % j) == 0:
            nPrimoVerif += 1
    
    if nPrimoVerif == 2: print(nPrimo, 'eh primo')
    if nPrimoVerif != 2: print(nPrimo, 'nao eh primo')