tamanhoMatriz = 12
somaValores = 0
totalAceito = 0

oMatriz = input()

matriz = []
for i in range(tamanhoMatriz):
    linha = []

    for j in range(tamanhoMatriz):
        linha.append(float(input()))
    
    matriz.append(linha)

for k in range(tamanhoMatriz):
    for l in range(tamanhoMatriz):
        if l > k: 
            somaValores += matriz[k][l]
            totalAceito += 1        

if oMatriz == 'S': print(f'{somaValores:.1f}')
if oMatriz == 'M': print(f'{(somaValores / totalAceito):.1f}')