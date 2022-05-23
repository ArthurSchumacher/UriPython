tempo = int(input())

qtd_segundos = [3600, 60, 1]
resultado = []

for i in qtd_segundos:
    qtd = int(tempo / i)
    resultado.append(str(qtd))
    tempo -= qtd * i

print(':'.join(resultado))