N, M = map(int, input().split(' '))
count = 0

for i in range(1, M + 1):
    count += 1

    if count == N:
        print(i, end = '\n')
        count = 0
    else:
        print(i, end = ' ')