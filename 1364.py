N, M = map(int, input().split(' '))

while M > 0 or N > 0:
    simApagados = 0
    simbolos = []

    for i in range(N):
        simbolos.append(input())

    for j in range(M):
        Linha = input()

        for simbolo in simbolos:
            simApagados += Linha.count(simbolo)
            Linha = Linha.replace(simbolo, '')

    print(simApagados)

    N, M = map(int, input().split(' '))