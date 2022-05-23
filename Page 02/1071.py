X, Y = (int(input()) for _ in range(2))
sumValues = 0

for i in range((Y + 1), X):
    if (i % 2) != 0:
        sumValues += i

print(sumValues)