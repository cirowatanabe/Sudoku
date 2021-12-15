def grade():
    grade = [['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-', '-', '-', '-', '-']]
    return grade


def show_grade(a):
    print('SHOW GRADE')
    for m, k in enumerate(a):
        for i in range(0, 9):
            print(k[i], end=' ')
            if i == 2 or i == 5:
                print('| ', end='')
        print('')
        if m == 2 or m == 5:
            print('-' * 21)
    print('\033[1;31m=-=\033[m'*20)
    return a


def preenchimento(a):
    while True:
        while True:
            try:
                linha = int(input('Qual a linha? '))
                while linha > 9 or linha < 1:
                    linha = int(input('Erro: O número da linha precisa estar entre 1 e 9: '))
            except:
                print('Digite um valor válido.')
            else:
                break
        while True:
            try:
                coluna = int(input('Qual a coluna? '))
                while coluna > 9 or coluna < 1:
                    coluna = int(input('Erro: O número da coluna precisa estar entre 1 e 9: '))
            except:
                print('Digite um valor válido.')
            else:
                break
        while True:
            try:
                valor = int(input('Número: '))
                while valor > 9 or valor < 1:
                    valor = int(input('Erro: O valor precisa estar entre 1 e 9: '))
            except:
                print('Digite um valor válido.')
            else:
                break
        a[linha - 1][coluna - 1] = valor
        for m, k in enumerate(a):
            for i in range(0, 9):
                print(k[i], end=' ')
                if i == 2 or i == 5:
                    print('| ', end='')
            print('')
            if m == 2 or m == 5:
                print('-' * 21)
        pergunta = str(input('Deseja continuar? [S/N] ')).strip().upper()
        if pergunta in 'N':
            break
    print('PREENCHIMENTO')
    show_grade(a)
    return a


def grade_real(a):
    for m, k in enumerate(a):
        for d, b in enumerate(k):
            if b == '-':
                a[m][d] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print('GRADE REAL')
    show_grade(a)
    return a


def enxugando_linhas(a):
    for c in a:
        for m in c:
            if type(m) == int:
                for k in c:
                    if type(k) == list and m in k:
                        k.remove(m)
    print('ENXUGANDO LINHAS')
    show_grade(a)
    return a


def enxugando_colunas(a):
    for c in a:
        for m, k in enumerate(c):
            if type(k) == int:
                for j in a:
                    if type(j[m]) == list and k in j[m]:
                        j[m].remove(k)
    print('ENXUGANDO COLUNAS')
    show_grade(a)
    return a


def enxugando_quadrados(a):

    # QUADRADO 1:
    for c in range(0, 3):
        for p in range(0, 3):
            if type(a[c][p]) == int:
                for k in range(0, 3):
                    for j in range(0, 3):
                        if type(a[k][j]) == list and a[c][p] in a[k][j]:
                            a[k][j].remove(a[c][p])

    # QUADRADO 2:
    for c in range(0, 3):
        for p in range(3, 6):
            if type(a[c][p]) == int:
                for k in range(0, 3):
                    for j in range(3, 6):
                        if type(a[k][j]) == list and a[c][p] in a[k][j]:
                            a[k][j].remove(a[c][p])

    # QUADRADO 3:
    for c in range(0, 3):
        for p in range(6, 9):
            if type(a[c][p]) == int:
                for k in range(0, 3):
                    for j in range(6, 9):
                        if type(a[k][j]) == list and a[c][p] in a[k][j]:
                            a[k][j].remove(a[c][p])

    # QUADRADO 4:
        for c in range(3, 6):
            for p in range(0, 3):
                if type(a[c][p]) == int:
                    for k in range(3, 6):
                        for j in range(0, 3):
                            if type(a[k][j]) == list and a[c][p] in a[k][j]:
                                a[k][j].remove(a[c][p])
    # QUADRADO 5:
        for c in range(3, 6):
            for p in range(3, 6):
                if type(a[c][p]) == int:
                    for k in range(3, 6):
                        for j in range(3, 6):
                            if type(a[k][j]) == list and a[c][p] in a[k][j]:
                                a[k][j].remove(a[c][p])

    # QUADRADO 6:
    for c in range(3, 6):
        for p in range(6, 9):
            if type(a[c][p]) == int:
                for k in range(3, 6):
                    for j in range(6, 9):
                        if type(a[k][j]) == list and a[c][p] in a[k][j]:
                            a[k][j].remove(a[c][p])

    # QUADRADO 7:
    for c in range(6, 9):
        for p in range(0, 3):
            if type(a[c][p]) == int:
                for k in range(6, 9):
                    for j in range(0, 3):
                        if type(a[k][j]) == list and a[c][p] in a[k][j]:
                            a[k][j].remove(a[c][p])

    # QUADRADO 8:
    for c in range(6, 9):
        for p in range(3, 6):
            if type(a[c][p]) == int:
                for k in range(6, 9):
                    for j in range(3, 6):
                        if type(a[k][j]) == list and a[c][p] in a[k][j]:
                            a[k][j].remove(a[c][p])

    # QUADRADO 9:
    for c in range(6, 9):
        for p in range(6, 9):
            if type(a[c][p]) == int:
                for k in range(6, 9):
                    for j in range(6, 9):
                        if type(a[k][j]) == list and a[c][p] in a[k][j]:
                            a[k][j].remove(a[c][p])
    #print('ENXUGANDO QUADRADOS')
    #show_grade(a)
    return a


def eliminando_unitarias(a):
    for t, c in enumerate(a):
        for m, k in enumerate(c):
            if type(k) == list and len(k) == 1:
                a[t][m] = k[0]
    #print('ELIMINANDO UNITÁRIAS')
    #show_grade(a)
    return a


def preenchendo_quadrados(a):

    # QUADRADO 1
    for c in range(0, 3):
        for p in range(0, 3):
            if type(a[c][p]) == list:
                for j in a[c][p]:
                    counter = 0
                    for m in range(0, 3):
                        for w in range(0, 3):
                            if type(a[m][w]) == int and a[m][w] == j:
                                counter += 1
                            elif type(a[m][w]) == list and j in a[m][w]:
                                counter += 1
                    if counter == 1:
                        a[c][p] = j
                        break

    # QUADRADO 2
    for c in range(0, 3):
        for p in range(3, 6):
            if type(a[c][p]) == list:
                for j in a[c][p]:
                    counter = 0
                    for m in range(0, 3):
                        for w in range(3, 6):
                            if type(a[m][w]) == int and a[m][w] == j:
                                counter += 1
                            elif type(a[m][w]) == list and j in a[m][w]:
                                counter += 1
                    if counter == 1:
                        a[c][p] = j
                        break

    # QUADRADO 3
    for c in range(0, 3):
        for p in range(6, 9):
            if type(a[c][p]) == list:
                for j in a[c][p]:
                    counter = 0
                    for m in range(0, 3):
                        for w in range(6, 9):
                            if type(a[m][w]) == int and a[m][w] == j:
                                counter += 1
                            elif type(a[m][w]) == list and j in a[m][w]:
                                counter += 1
                    if counter == 1:
                        a[c][p] = j
                        break

    # QUADRADO 4
    for c in range(3, 6):
        for p in range(0, 3):
            if type(a[c][p]) == list:
                for j in a[c][p]:
                    counter = 0
                    for m in range(3, 6):
                        for w in range(0, 3):
                            if type(a[m][w]) == int and a[m][w] == j:
                                counter += 1
                            elif type(a[m][w]) == list and j in a[m][w]:
                                counter += 1
                    if counter == 1:
                        a[c][p] = j
                        break

    # QUADRADO 5
    for c in range(3, 6):
        for p in range(3, 6):
            if type(a[c][p]) == list:
                for j in a[c][p]:
                    counter = 0
                    for m in range(3, 6):
                        for w in range(3, 6):
                            if type(a[m][w]) == int and a[m][w] == j:
                                counter += 1
                            elif type(a[m][w]) == list and j in a[m][w]:
                                counter += 1
                    if counter == 1:
                        a[c][p] = j
                        break

    # QUADRADO 6
    for c in range(3, 6):
        for p in range(6, 9):
            if type(a[c][p]) == list:
                for j in a[c][p]:
                    counter = 0
                    for m in range(3, 6):
                        for w in range(6, 9):
                            if type(a[m][w]) == int and a[m][w] == j:
                                counter += 1
                            elif type(a[m][w]) == list and j in a[m][w]:
                                counter += 1
                    if counter == 1:
                        a[c][p] = j
                        break

    # QUADRADO 7
    for c in range(6, 9):
        for p in range(0, 3):
            if type(a[c][p]) == list:
                for j in a[c][p]:
                    counter = 0
                    for m in range(6, 9):
                        for w in range(0, 3):
                            if type(a[m][w]) == int and a[m][w] == j:
                                counter += 1
                            elif type(a[m][w]) == list and j in a[m][w]:
                                counter += 1
                    if counter == 1:
                        a[c][p] = j
                        break

    # QUADRADO 8
    for c in range(6, 9):
        for p in range(3, 6):
            if type(a[c][p]) == list:
                for j in a[c][p]:
                    counter = 0
                    for m in range(6, 9):
                        for w in range(3, 6):
                            if type(a[m][w]) == int and a[m][w] == j:
                                counter += 1
                            elif type(a[m][w]) == list and j in a[m][w]:
                                counter += 1
                    if counter == 1:
                        a[c][p] = j
                        break

    # QUADRADO 9
    for c in range(6, 9):
        for p in range(6, 9):
            if type(a[c][p]) == list:
                for j in a[c][p]:
                    counter = 0
                    for m in range(6, 9):
                        for w in range(6, 9):
                            if type(a[m][w]) == int and a[m][w] == j:
                                counter += 1
                            elif type(a[m][w]) == list and j in a[m][w]:
                                counter += 1
                    if counter == 1:
                        a[c][p] = j
                        break
    print('PREENCHENDO QUADRADOS')
    show_grade(a)
    return a


def busca_horizontal(a):

    # QUADRADO 1
    for c in range(0, 3):
        for d in range(0, 3):
            if type(a[c][d]) == list:
                for n in a[c][d]:
                    counter = 0
                    for k in range(0, 3):
                        for j in range(0, 3):
                            if type(a[k][j]) == int and a[k][j] == n:
                                counter += 1
                            elif type(a[k][j]) == list and n in a[k][j] and k != c:
                                counter += 1
                    if counter == 0:
                        for t in range(3, 9):
                            if type(a[c][t]) == list and n in a[c][t]:
                                a[c][t].remove(n)

    # QUADRADO 2
    for c in range(0, 3):
        for d in range(3, 6):
            if type(a[c][d]) == list:
                for n in a[c][d]:
                    counter = 0
                    for k in range(0, 3):
                        for j in range(3, 6):
                            if type(a[k][j]) == int and a[k][j] == n:
                                counter += 1
                            elif type(a[k][j]) == list and n in a[k][j] and k != c:
                                counter += 1
                    if counter == 0:
                        for t in range(0, 3):
                            if type(a[c][t]) == list and n in a[c][t]:
                                a[c][t].remove(n)
                        for u in range(6, 9):
                            if type(a[c][u]) == list and n in a[c][u]:
                                a[c][u].remove(n)

    # QUADRADO 3
    for c in range(0, 3):
        for d in range(6, 9):
            if type(a[c][d]) == list:
                for n in a[c][d]:
                    counter = 0
                    for k in range(0, 3):
                        for j in range(6, 9):
                            if type(a[k][j]) == int and a[k][j] == n:
                                counter += 1
                            elif type(a[k][j]) == list and n in a[k][j] and k != c:
                                counter += 1
                    if counter == 0:
                        for u in range(0, 6):
                            if type(a[c][u]) == list and n in a[c][u]:
                                a[c][u].remove(n)

    # QUADRADO 4
    for c in range(3, 6):
        for d in range(0, 3):
            if type(a[c][d]) == list:
                for n in a[c][d]:
                    counter = 0
                    for k in range(3, 6):
                        for j in range(0, 3):
                            if type(a[k][j]) == int and a[k][j] == n:
                                counter += 1
                            elif type(a[k][j]) == list and n in a[k][j] and k != c:
                                counter += 1
                    if counter == 0:
                        for u in range(3, 9):
                            if type(a[c][u]) == list and n in a[c][u]:
                                a[c][u].remove(n)

    # QUADRADO 5
    for c in range(3, 6):
        for d in range(3, 6):
            if type(a[c][d]) == list:
                for n in a[c][d]:
                    counter = 0
                    for k in range(3, 6):
                        for j in range(3, 6):
                            if type(a[k][j]) == int and a[k][j] == n:
                                counter += 1
                            elif type(a[k][j]) == list and n in a[k][j] and k != c:
                                counter += 1
                    if counter == 0:
                        for u in range(0, 3):
                            if type(a[c][u]) == list and n in a[c][u]:
                                a[c][u].remove(n)
                        for t in range(6, 9):
                            if type(a[c][t]) == list and n in a[c][t]:
                                a[c][t].remove(n)

    # QUADRADO 6
    for c in range(3, 6):
        for d in range(6, 9):
            if type(a[c][d]) == list:
                for n in a[c][d]:
                    counter = 0
                    for k in range(3, 6):
                        for j in range(6, 9):
                            if type(a[k][j]) == int and a[k][j] == n:
                                counter += 1
                            elif type(a[k][j]) == list and n in a[k][j] and k != c:
                                counter += 1
                    if counter == 0:
                        for u in range(0, 6):
                            if type(a[c][u]) == list and n in a[c][u]:
                                a[c][u].remove(n)

    # QUADRADO 7
    for c in range(6, 9):
        for d in range(0, 3):
            if type(a[c][d]) == list:
                for n in a[c][d]:
                    counter = 0
                    for k in range(6, 9):
                        for j in range(0, 3):
                            if type(a[k][j]) == int and a[k][j] == n:
                                counter += 1
                            elif type(a[k][j]) == list and n in a[k][j] and k != c:
                                counter += 1
                    if counter == 0:
                        for u in range(3, 9):
                            if type(a[c][u]) == list and n in a[c][u]:
                                a[c][u].remove(n)

    # QUADRADO 8
    for c in range(6, 9):
        for d in range(3, 6):
            if type(a[c][d]) == list:
                for n in a[c][d]:
                    counter = 0
                    for k in range(6, 9):
                        for j in range(3, 6):
                            if type(a[k][j]) == int and a[k][j] == n:
                                counter += 1
                            elif type(a[k][j]) == list and n in a[k][j] and k != c:
                                counter += 1
                    if counter == 0:
                        for u in range(0, 3):
                            if type(a[c][u]) == list and n in a[c][u]:
                                a[c][u].remove(n)
                        for t in range(6, 9):
                            if type(a[c][t]) == list and n in a[c][t]:
                                a[c][t].remove(n)

    # QUADRADO 9
    for c in range(6, 9):
        for d in range(6, 9):
            if type(a[c][d]) == list:
                for n in a[c][d]:
                    counter = 0
                    for k in range(6, 9):
                        for j in range(6, 9):
                            if type(a[k][j]) == int and a[k][j] == n:
                                counter += 1
                            elif type(a[k][j]) == list and n in a[k][j] and k != c:
                                counter += 1
                    if counter == 0:
                        for u in range(0, 6):
                            if type(a[c][u]) == list and n in a[c][u]:
                                a[c][u].remove(n)
    print('BUSCA HORIZONTAL')
    show_grade(a)
    return a


def busca_vertical(a):
    # QUADRADO 1
    for c in range(0, 3):
        for d in range(0, 3):
            if type(a[c][d]) == list:
                for n in a[c][d]:
                    counter = 0
                    for k in range(0, 3):
                        for j in range(0, 3):
                            if type(a[k][j]) == int and a[k][j] == n:
                                counter += 1
                            elif type(a[k][j]) == list and n in a[k][j] and j != d:
                                counter += 1
                    if counter == 0:
                        for t in range(3, 9):
                            if type(a[t][d]) == list and n in a[t][d]:
                                a[t][d].remove(n)

    # QUADRADO 2
    for c in range(0, 3):
        for d in range(3, 6):
            if type(a[c][d]) == list:
                for n in a[c][d]:
                    counter = 0
                    for k in range(0, 3):
                        for j in range(3, 6):
                            if type(a[k][j]) == int and a[k][j] == n:
                                counter += 1
                            elif type(a[k][j]) == list and n in a[k][j] and j != d:
                                counter += 1
                    if counter == 0:
                        for t in range(3, 9):
                            if type(a[t][d]) == list and n in a[t][d]:
                                a[t][d].remove(n)

    # QUADRADO 3
    for c in range(0, 3):
        for d in range(6, 9):
            if type(a[c][d]) == list:
                for n in a[c][d]:
                    counter = 0
                    for k in range(0, 3):
                        for j in range(6, 9):
                            if type(a[k][j]) == int and a[k][j] == n:
                                counter += 1
                            elif type(a[k][j]) == list and n in a[k][j] and j != d:
                                counter += 1
                    if counter == 0:
                        for t in range(3, 9):
                            if type(a[t][d]) == list and n in a[t][d]:
                                a[t][d].remove(n)

    # QUADRADO 4
    for c in range(3, 6):
        for d in range(0, 3):
            if type(a[c][d]) == list:
                for n in a[c][d]:
                    counter = 0
                    for k in range(3, 6):
                        for j in range(0, 3):
                            if type(a[k][j]) == int and a[k][j] == n:
                                counter += 1
                            elif type(a[k][j]) == list and n in a[k][j] and j != d:
                                counter += 1
                    if counter == 0:
                        for t in range(0, 3):
                            if type(a[t][d]) == list and n in a[t][d]:
                                a[t][d].remove(n)
                        for u in range(6, 9):
                            if type(a[u][d]) == list and n in a[u][d]:
                                a[u][d].remove(n)
    # QUADRADO 5
    for c in range(3, 6):
        for d in range(3, 6):
            if type(a[c][d]) == list:
                for n in a[c][d]:
                    counter = 0
                    for k in range(3, 6):
                        for j in range(3, 6):
                            if type(a[k][j]) == int and a[k][j] == n:
                                counter += 1
                            elif type(a[k][j]) == list and n in a[k][j] and j != d:
                                counter += 1
                    if counter == 0:
                        for t in range(0, 3):
                            if type(a[t][d]) == list and n in a[t][d]:
                                a[t][d].remove(n)
                        for u in range(6, 9):
                            if type(a[u][d]) == list and n in a[u][d]:
                                a[u][d].remove(n)
    # QUADRADO 6
    for c in range(3, 6):
        for d in range(6, 9):
            if type(a[c][d]) == list:
                for n in a[c][d]:
                    counter = 0
                    for k in range(3, 6):
                        for j in range(6, 9):
                            if type(a[k][j]) == int and a[k][j] == n:
                                counter += 1
                            elif type(a[k][j]) == list and n in a[k][j] and j != d:
                                counter += 1
                    if counter == 0:
                        for t in range(0, 3):
                            if type(a[t][d]) == list and n in a[t][d]:
                                a[t][d].remove(n)
                        for u in range(6, 9):
                            if type(a[u][d]) == list and n in a[u][d]:
                                a[u][d].remove(n)

    # QUADRADO 7
    for c in range(6, 9):
        for d in range(0, 3):
            if type(a[c][d]) == list:
                for n in a[c][d]:
                    counter = 0
                    for k in range(6, 9):
                        for j in range(0, 3):
                            if type(a[k][j]) == int and a[k][j] == n:
                                counter += 1
                            elif type(a[k][j]) == list and n in a[k][j] and j != d:
                                counter += 1
                    if counter == 0:
                        for t in range(0, 6):
                            if type(a[t][d]) == list and n in a[t][d]:
                                a[t][d].remove(n)

    # QUADRADO 8
    for c in range(6, 9):
        for d in range(3, 6):
            if type(a[c][d]) == list:
                for n in a[c][d]:
                    counter = 0
                    for k in range(6, 9):
                        for j in range(3, 6):
                            if type(a[k][j]) == int and a[k][j] == n:
                                counter += 1
                            elif type(a[k][j]) == list and n in a[k][j] and j != d:
                                counter += 1
                    if counter == 0:
                        for t in range(0, 6):
                            if type(a[t][d]) == list and n in a[t][d]:
                                a[t][d].remove(n)

    # QUADRADO 9
    for c in range(6, 9):
        for d in range(6, 9):
            if type(a[c][d]) == list:
                for n in a[c][d]:
                    counter = 0
                    for k in range(6, 9):
                        for j in range(6, 9):
                            if type(a[k][j]) == int and a[k][j] == n:
                                counter += 1
                            elif type(a[k][j]) == list and n in a[k][j] and j != d:
                                counter += 1
                    if counter == 0:
                        for t in range(0, 6):
                            if type(a[t][d]) == list and n in a[t][d]:
                                a[t][d].remove(n)
    print('BUSCA VERTICAL')
    show_grade(a)
    return a


def sudoku():
    a = grade_real(preenchimento(show_grade(grade())))
    while True:
        counter = 0
        for c in a:
            for j in c:
                if type(j) == list:
                    counter += 1
                    busca_vertical(busca_horizontal(preenchendo_quadrados(eliminando_unitarias(enxugando_quadrados
                                                                                               (enxugando_colunas
                                                                                                (enxugando_linhas(a)))))))
        if counter == 0:
            break
    show_grade(a)







