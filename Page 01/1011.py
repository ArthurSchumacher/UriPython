def Volume(r):
    pi = 3.14159
    return (4 / 3) * pi * (r ** 3)

raio = float(input())

print('VOLUME = %.3f' % Volume(raio))