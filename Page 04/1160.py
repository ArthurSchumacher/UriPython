nTestes = int(input())

for i in range(nTestes):
    popA, popB, crescA, crescB = map(float, input().split())
    anos = 0

    while popA <= popB:

        percPopA = int(popA * ((crescA / 100)))
        percPopB = int(popB * ((crescB / 100)))

        popA += percPopA
        popB += percPopB

        anos += 1

        if anos > 100:
            print('Mais de 1 seculo.')
            break
    
    if anos <= 100: print(anos, 'anos.')