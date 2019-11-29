# PROYECTOINTEGRADOR 2.0


def memorama():
    print('Jugador 1')
    global cont1
    global limit
    while True:
        x = int(input('Ingresa un valor 1 en la horizontal: '))
        y = int(input('Ingresa un valor 1 en la vertical: '))
        if ((x < 6 and y < 6) and (matriz1[x][y] == '-')):
            break

    matriz1[x][y] = matriz2[x][y]
    print(imprimir())
    # if y > 5:
    # print('ERROR')
    while True:
        x2 = int(input('Ingresa un valor 2 en la horizontal: '))
        y2 = int(input('Ingresa un valor 2 en la vertical: '))
        if ((x2 < 6 and y2 < 6) and (x2 != x or y2 != y) and (matriz1[x2][y2] == '-')):
            break
    # if x2 > 5:
    # print('ERROR')
    # matriz1[x][y] = '-'
    # else:
    # y2 = int(input('Ingresa un valor en la vertical: '))
    # if y2 > 5:
    # print('ERROR')
    # matriz1[x][y] = '-'

    matriz1[x2][y2] = matriz2[x2][y2]
    print(imprimir())

    carta1 = matriz1[x][y]
    carta2 = matriz1[x2][y2]
    if carta1 == carta2:
        cont1 = cont1 + 1
        limit = limit + 2
    else:
        matriz1[x][y] = '-'
        matriz1[x2][y2] = '-'
        print(imprimir())


def memorama2():
    print('Jugador 2')
    global cont2
    global limit
    while True:
        x = int(input('Ingresa un valor 1 en la horizontal: '))
        y = int(input('Ingresa un valor 1 en la vertical: '))
        if ((x < 6 and y < 6) and (matriz1[x][y] == '-')):
            break

    matriz1[x][y] = matriz2[x][y]
    print(imprimir())
    # if y > 5:
    # print('ERROR')
    while True:
        x2 = int(input('Ingresa un valor 2 en la horizontal: '))
        y2 = int(input('Ingresa un valor 2 en la vertical: '))
        if ((x2 < 6 and y2 < 6) and (x2 != x or y2 != y) and (matriz1[x2][y2] == '-')):
            break

    matriz1[x2][y2] = matriz2[x2][y2]
    print(imprimir())
    carta3 = matriz1[x][y]
    carta4 = matriz1[x2][y2]
    if carta3 == carta4:
        cont2 = cont2 + 1
        limit = limit + 2
    else:
        matriz1[x][y] = '-'
        matriz1[x2][y2] = '-'
        print(imprimir())


def imprimir():
    contador = 0
    print('  0 1 2 3 4 5 \n')

    for i in range(6):
        print(contador, '', end='')
        contador += 1
        for j in range(6):
            print((matriz1[i][j]), '', end='')
        print("")



def programaPrincipal():
    while variable == 5:
        random.shuffle(matriz2)
        for i in matriz2:
            random.shuffle(i)
        memorama()


x = 0
y = 0
x2 = 0
y2 = 0
cont1 = 0
cont2 = 0
limit = 0
matriz1 = [['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'],
           ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-']]
matriz2 = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [1, 2, 3, 4, 5, 6],
           [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]
guion = '-'
variable = 5
print(imprimir())
while True:
    print(memorama())
    if (limit > 35) :
        break
    print(memorama2())

    if (limit > 35) :
        break
    answer = str(input('Quieres seguir jugando ? '))
    if (answer == 'NO' or answer == 'no' or answer == 'No'):
        break
print("Puntuación jugador 1 : ", cont1)
print("Puntuación jugador 2 : ", cont2)
if (cont1 > cont2) :
    print(' GANA JUGADOR 1 ! ')
else:
    if (cont2 > cont1) :
        print(' GANA JUGADOR 2 !')
    else: print(' EMPATE ')