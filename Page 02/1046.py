def Tempo(x, y):
    if y <= x:
        y += 24
    
    tempo = y - x
    return tempo

hInicial, hFinal = map(int, input().split())

print('O JOGO DUROU', Tempo(hInicial, hFinal), 'HORA(S)')