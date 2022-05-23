Alcool = 0
Gasolina = 0
Diesel = 0

N = 0
while N != 4:
    N = int(input())

    if N == 1: Alcool += 1
    if N == 2: Gasolina += 1
    if N == 3: Diesel += 1

print('MUITO OBRIGADO')
print('Alcool:', Alcool)
print('Gasolina:', Gasolina)
print('Diesel:', Diesel)