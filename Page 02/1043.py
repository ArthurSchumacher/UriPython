def Perimetro(A, B, C):
    return A + B + C

def Trapezio(A, B, C):
    return ((A + B) / 2) * C

A, B, C = map(float, input().split())

if A < (B + C) and B < (A + C) and C < (A + B):
    print('Perimetro = %.1f' % Perimetro(A, B, C))
else:
    print('Area = %.1f' % Trapezio(A, B, C))