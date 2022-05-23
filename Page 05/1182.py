tamanhoMatriz = 3
somaValores = 0

cMatriz = int(input())
oMatriz = input()

matriz = []
for i in range(tamanhoMatriz):
    linha = []

    for j in range(tamanhoMatriz):
        linha.append(float(input()))

    matriz.append(linha)

for k in range(tamanhoMatriz):   
    somaValores += matriz[k][cMatriz]

if oMatriz == 'S': print(f'{somaValores}')
if oMatriz == 'M': print(f'{somaValores / tamanhoMatriz:.1f}')