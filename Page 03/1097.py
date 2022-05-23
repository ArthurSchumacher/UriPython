auxI = 1
auxJ = 7

while auxI <= 9:

    for j in range(0, 3):
        print('I=%d J=%d' % (auxI, auxJ))
        auxJ -= 1

    auxI += 2
    auxJ += 5