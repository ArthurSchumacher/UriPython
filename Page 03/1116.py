N = int(input())

for i in range(N):
    X, Y = map(float, input().split())

    if Y != 0: print(X / Y)
    if Y == 0: print('divisao impossivel')