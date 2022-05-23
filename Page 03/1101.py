M, N = map(int, input().split())
while M > 0 and N > 0:
    sumValues = 0

    if N > M:
        lista = [M, N]
        lista.reverse()
        M = lista[0]
        N = lista[1]
    
    for i in range(N, M + 1):
        sumValues += i
        print(i, end=' ')

    print('Sum=%d' % sumValues)

    M, N = map(int, input().split())