def dddByRegion(ddd):
    if ddd == 11: return 'Sao Paulo'
    if ddd == 19: return 'Campinas'
    if ddd == 21: return 'Rio de Janeiro'
    if ddd == 27: return 'Vitoria'
    if ddd == 31: return 'Belo Horizonte'
    if ddd == 32: return 'Juiz de Fora'
    if ddd == 61: return 'Brasilia'
    if ddd == 71: return 'Salvador'

    return 'DDD nao cadastrado'

ddd = int(input())

print(dddByRegion(ddd))