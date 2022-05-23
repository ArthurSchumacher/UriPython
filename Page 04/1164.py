nTestes = int(input())

for i in range(nTestes):
    nPerfeito = int(input())
    sumValues = 0

    for j in range(nPerfeito):
        sumValues += j

        if sumValues == nPerfeito:
            print(nPerfeito, 'eh perfeito')
            break
    
    if sumValues != nPerfeito:
        print(nPerfeito, 'nao eh perfeito')