def Triangulo(arg1, arg2):
    return (arg1 * arg2) / 2

def Circulo(arg1):
    pi = 3.14159
    return pi * (arg1 ** 2)

def Trapezio(arg1, arg2, arg3):
    return ((arg1 + arg2) / 2) * arg3

def Quadrado(arg1):
    return arg1 ** 2

def Retangulo(arg1, arg2):
    return arg1 * arg2

A, B, C = map(float, input().split(' '))

print('TRIANGULO: %.3f' % Triangulo(A, C))
print('CIRCULO: %.3f' % Circulo(C))
print('TRAPEZIO: %.3f' % Trapezio(A, B, C))
print('QUADRADO: %.3f' % Quadrado(B))
print('RETANGULO: %.3f' % Retangulo(A, B))