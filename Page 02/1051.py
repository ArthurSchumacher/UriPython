def salaryTax(salary):
    if salary <= 2000.00:
        return print('Isento')
    if salary >= 2000.01 and salary <= 3000.00:
        return print('R$ %.2f' % ((salary - 2000.00) * 0.08))
    if salary >= 3000.01 and salary < 4500.00:
        return print('R$ %.2f' % ((salary - 3000.00) * 0.18 + (1000.00 * 0.08)))
    if salary >= 4500.00:
        return print('R$ %.2f' % ((salary - 4500.00) * 0.28 + (1500.00 * 0.18) + (1000.00 * 0.08)))


salary = float(input())

salaryTax(salary)
