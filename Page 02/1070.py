X = int(input())
printCount = 0

for i in range(12):
    if (X % 2) != 0:
        print(X)

        printCount += 1
        if printCount == 6: break
        
    X += 1