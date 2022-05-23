def Media(n1, n2, n3, n4):
    return ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

def Media2(n1, n2):
    return (n1 + n2) / 2

Nota_1, Nota_2, Nota_3, Nota_4 = map(float, input().split(' '))
media = Media(Nota_1, Nota_2, Nota_3, Nota_4)
print('Media: %.1f' % media)

if  media >= 7.0:
    print('Aluno aprovado.')
elif media >= 5.0 and media < 7.0:
    print('Aluno em exame.')

    Nota_5 = float(input())
    media2 = Media2(media, Nota_5)

    print('Nota do exame: %.1f' % Nota_5)
    if media2 >= 5.0:
        print('Aluno aprovado.')
        print('Media final: %.1f' % media2)
    else:
        print('Aluno reprovado.')
        print('Media final: %.1f' % media2)
else:
    print('Aluno reprovado.')