N = int(input())
valuesIn = 0
valuesOut = 0

for i in range(N):
    X = int(input())

    if X >= 10 and X <= 20: valuesIn += 1
    if X < 10 or X > 20: valuesOut += 1

print(valuesIn, 'in')
print(valuesOut, 'out')