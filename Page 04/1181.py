lMatriz = int(input())
oMatriz = input()
somaValores = 0

matriz = []
for i in range(12):
    linha = []

    for j in range(12):
        linha.append(float(input()))

    matriz.append(linha)

for k in matriz[lMatriz]:
    somaValores += k

if oMatriz == 'S': print('%.1f' % (somaValores))
if oMatriz == 'M': print('%.1f' % (somaValores / 12))