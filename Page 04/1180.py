nLimite = int(input())
listaValores = list(map(int, input().split()))

listaOrdenada = sorted(listaValores)
posicao = listaValores.index(listaOrdenada[0])

print('Menor valor:', listaOrdenada[0])
print('Posicao:', posicao)