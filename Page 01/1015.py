from math import sqrt

def Distancia(x1, x2, y1, y2):
    return sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

x1, y1 = map(float, input().split(' '))
x2, y2 = map(float, input().split(' '))

print('%.4f' % Distancia(x1, x2, y1, y2))