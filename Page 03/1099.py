N = int(input())

for i in range(N):
    lista = list(map(int, input().split()))
    sumValues = 0

    X = lista[0]; Y = lista[1]

    if Y > X:
        lista.reverse()
        X = lista[0]
        Y = lista[1]

    for j in range((Y + 1), X):
        if (j % 2) != 0:
            sumValues += j

    print(sumValues)