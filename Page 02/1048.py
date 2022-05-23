salario = float(input())

if salario >= 0.0 and salario <= 400.00:
    reajuste = salario * 0.15
    print('Novo salario: %.2f' % (salario + reajuste))
    print('Reajuste ganho: %.2f' % reajuste)
    print('Em percentual: 15 %')
elif salario >= 400.01 and salario <= 800.00:
    reajuste = salario * 0.12
    print('Novo salario: %.2f' % (salario + reajuste))
    print('Reajuste ganho: %.2f' % reajuste)
    print('Em percentual: 12 %')
elif salario >= 800.01 and salario <= 1200.00:
    reajuste = salario * 0.1
    print('Novo salario: %.2f' % (salario + reajuste))
    print('Reajuste ganho: %.2f' % reajuste)
    print('Em percentual: 10 %')
elif salario >= 1200.01 and salario <= 2000.00:
    reajuste = salario * 0.07
    print('Novo salario: %.2f' % (salario + reajuste))
    print('Reajuste ganho: %.2f' % reajuste)
    print('Em percentual: 7 %')
elif salario >= 2000.01:
    reajuste = salario * 0.04
    print('Novo salario: %.2f' % (salario + reajuste))
    print('Reajuste ganho: %.2f' % reajuste)
    print('Em percentual: 4 %')