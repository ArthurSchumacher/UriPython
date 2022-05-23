X, Z = (int(input()) for _ in range(2))
soma = valor_Min = 0

while Z <= X:
    Z = int(input())

while soma < Z:
    soma += X
    X += 1
    valor_Min += 1

print(valor_Min)