n = int(input())

while n != 0:
    sumValues = 0

    if (n % 2) != 0: n += 1

    for i in range(5):
        sumValues += n
        n += 2
    
    print(sumValues)
    
    n = int(input())