from math import sqrt

A, B, C = map(float, input().split(' '))

try:
    delta = (B ** 2) - 4 * A * C
    r1 = (-B + sqrt(delta)) / (2 * A)
    r2 = (-B - sqrt(delta)) / (2 * A)

    print('R1 = %.5f' % r1)
    print('R2 = %.5f' % r2)

except:
    print('Impossivel calcular')