A, B, C, D, E = (int(input()) for _ in range(5))
values = [A, B, C, D, E]
pairValues = 0

for i in values:
    if (i % 2) == 0:
        pairValues += 1

print(pairValues, 'valores pares')