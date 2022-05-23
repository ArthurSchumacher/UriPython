coelhos = 0
ratos = 0
sapos = 0
X = int(input())

for i in range(X):
    Y, Z = map(str, input().split())

    if Z == 'C': coelhos += float(Y)
    if Z == 'R': ratos += float(Y)
    if Z == 'S': sapos += float(Y)

total = (coelhos + ratos + sapos)

print('Total: %.0f cobaias' % total)
print('Total de coelhos: %.0f' % coelhos)
print('Total de ratos: %.0f' % ratos)
print('Total de sapos: %.0f' % sapos)
print('Percentual de coelhos: %.2f' % ((coelhos * 100)/total), '%')
print('Percentual de ratos: %.2f' % ((ratos * 100)/total), '%')
print('Percentual de sapos: %.2f' % ((sapos * 100)/total), '%')