def GastoCombustivel(kmh, horas):
    return (kmh * horas) / 12

horas = int(input())
kmh = int(input())

print('%.3f' % GastoCombustivel(kmh, horas))