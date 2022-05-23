interWins = 0
gremioWins = 0
drawGames = 0

menu = 1
while menu == 1:
    inter, gremio = map(int, input().split())

    if inter > gremio: interWins += 1
    if inter < gremio: gremioWins += 1
    if inter == gremio: drawGames += 1

    while menu != 2:
        print('Novo grenal (1-sim 2-nao)')
        menu = int(input())

        if menu == 1: break
        if menu == 2:
            print((interWins + gremioWins + drawGames), 'grenais')
            print('Inter:' + str(interWins))
            print('Gremio:' + str(gremioWins))
            print('Empates:' + str(drawGames))

            if interWins > gremioWins: print('Inter venceu mais')
            if interWins < gremioWins: print('Gremio venceu mais')
            if interWins == gremioWins: print('Nao houve vencedor')
            break