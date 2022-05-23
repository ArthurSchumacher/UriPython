X, Y = map(int, input().split())

while X != Y:

    if X < Y: print('Crescente')
    if X > Y: print('Decrescente')

    X, Y = map(int, input().split())