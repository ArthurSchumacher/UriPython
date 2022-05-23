def media(a: float, b: float, c: float):
    return print('%.1f' % (((a * 2) + (b * 3) + (c * 5)) / 10))

N = int(input())

for i in range(N):
    nota1, nota2, nota3 = map(float, input().split())

    media(nota1, nota2, nota3)