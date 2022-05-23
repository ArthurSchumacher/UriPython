def Tempo(a, b, c, d):
    dif = ((c * 60) + d) - ((a * 60) + b)
    if dif <= 0:
        dif += 24 * 60
    
    return dif

hInicial, mInicial, hFinal, mFinal = map(int, input().split())
totalSegundos = Tempo(hInicial, mInicial, hFinal, mFinal)

print('O JOGO DUROU', totalSegundos // 60, 'HORA(S) E', totalSegundos % 60, 'MINUTO(S)')