n = float(input())
idades = 0
total = 0

while n > 0:
    idades += n
    total += 1

    n = float(input())

print('%.2f' % (idades / total))