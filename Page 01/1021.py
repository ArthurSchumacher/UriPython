valor = float(input())

cedulas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for cedula in cedulas:
    qtd_cedulas = int(valor / cedula)
    print('%d nota(s) de R$ %.2f' % (qtd_cedulas, cedula))
    valor -= qtd_cedulas * cedula

print('MOEDAS:')
for moeda in moedas:
    qtd_moedas = int(round(valor, 2) / moeda)
    print('%d moeda(s) de R$ %.2f' % (qtd_moedas, moeda))
    valor -= qtd_moedas * moeda