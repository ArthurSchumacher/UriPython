def SalarioComBonus(a, b):
    return a + (b * 0.15)

nome = str(input())
salario = float(input())
valor_vendas = float(input())

print('TOTAL = R$', format(SalarioComBonus(salario, valor_vendas), '.2f'))