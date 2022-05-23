def validation():
    while True:
        arg = float(input())

        if arg < 0 or arg > 10: print('nota invalida')
        if arg >= 0 and arg <= 10: return arg

def media(arg1, arg2):
    return print('media = %.2f' % ((arg1 + arg2) / 2))

ans = 1
while ans == 1:
    N1 = validation()
    N2 = validation()

    media(N1, N2)

    while ans != 2:
        print('novo calculo (1-sim 2-nao)')
        ans = int(input())

        if ans == 1: break