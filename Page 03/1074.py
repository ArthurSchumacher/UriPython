X = int(input())

for i in range(X):
    N = int(input())

    if N == 0: print('NULL')
    if (N % 2) == 0 and (N > 0): print('EVEN POSITIVE')
    if (N % 2) == 0 and (N < 0): print('EVEN NEGATIVE')
    if (N % 2) != 0 and (N > 0): print('ODD POSITIVE')
    if (N % 2) != 0 and (N < 0): print('ODD NEGATIVE')