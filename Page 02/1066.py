A, B, C, D, E = (int(input()) for _ in range(5))
values = [A, B, C, D, E]
pairValues = 0
oddValues = 0
positiveValues = 0
negativeValues = 0

for i in values:
    if (i % 2) == 0: pairValues += 1
    if (i % 2) != 0: oddValues += 1
    if i > 0: positiveValues += 1
    if i < 0: negativeValues += 1

print(pairValues, 'valor(es) par(es)')
print(oddValues, 'valor(es) impar(es)')
print(positiveValues, 'valor(es) positivo(s)')
print(negativeValues, 'valor(es) negativo(s)')