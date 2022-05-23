idade = int(input())

tempo = [365, 30, 1]
resultado = []

for i in tempo:
    qtd = int(idade / i)
    resultado.append(str(qtd))
    idade -= qtd * i

print(resultado[0], 'ano(s)')
print(resultado[1], 'mes(es)')
print(resultado[2], 'dia(s)')