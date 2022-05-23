A, B, C, D, E, F = (float(input()) for _ in range(6))
values = [A, B, C, D, E, F]
positiveValues = 0

for value in values:
    if value > 0:
        positiveValues += 1

print(positiveValues, 'valores positivos')
