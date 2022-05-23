valores = list(map(float, input().split()))
continuar = True

A, B, C = sorted(valores, reverse = True)

if A >= (B + C):
    print('NAO FORMA TRIANGULO')
    continuar = False

if A ** 2 == ((B ** 2) + (C ** 2)) and continuar:
    print('TRIANGULO RETANGULO')

if A ** 2 > ((B ** 2) + (C ** 2)) and continuar:
    print('TRIANGULO OBTUSANGULO')

if A ** 2 < ((B ** 2) + (C ** 2)) and continuar:
    print('TRIANGULO ACUTANGULO')

if A == B == C and continuar:
    print('TRIANGULO EQUILATERO')

if (A == B or B == C) and not (A == B and B == C) and continuar:
    print('TRIANGULO ISOSCELES')