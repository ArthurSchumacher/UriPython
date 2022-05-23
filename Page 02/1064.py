A, B, C, D, E, F = (float(input()) for _ in range(6))
lista = [A, B, C, D, E, F]
positiveNumbers = 0
sumNumbers = 0

for i in lista:
    if i > 0:
        positiveNumbers += 1
        sumNumbers += i

print(positiveNumbers, 'valores positivos')
print('%.1f' % (sumNumbers / positiveNumbers))