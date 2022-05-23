lista = []
temp = 0

for i in range(20):
    lista.append(int(input()))

begin = 0
end = 19

while begin != 10:

    temp = lista[begin]
    lista[begin] = lista[end]
    lista[end] = temp

    begin += 1
    end -= 1

for j in range(len(lista)):
    print('N[%d] = %d' % (j, lista[j]))