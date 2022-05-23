Lista = list(map(int, input().split()))
A = Lista.pop(0)
N = 0
Soma = 0

for i in Lista:
    if i > 0:
        N = i
        break

for j in range(N):
    Soma += A + j

print(Soma)