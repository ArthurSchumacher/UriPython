from decimal import Decimal

i = 0
j = 1
while i <= 2:
    if i == 0 or i == 1 or i == 2:
        print('I=%d J=%d' % (i, j))
    else:
        print('I=%.1f J=%.1f' % (i, j))

    j += 1
    if j == (i + 4):
        i += Decimal('0.2')
        j -= Decimal('2.8')