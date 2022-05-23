n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    sumValues = 0

    if (x % 2) == 0: x += 1

    for i in range(y):        
        sumValues += x
        x += 2
    
    print(sumValues)