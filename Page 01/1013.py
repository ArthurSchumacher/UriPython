def Maior(arg1, arg2):
    return (arg1 + arg2 + abs(arg1 - arg2)) / 2

A, B, C = map(int, input().split(' '))

temp = Maior(A, B)
maior = Maior(temp, C)

print('%.0d eh o maior' % maior)