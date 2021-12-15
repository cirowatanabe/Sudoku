# Sudoku

O Sudoku clássico consiste em um diagrama de 9x9, subdividido em 9 quadrados de 3x3, como na figura abaixo. O objetivo do jogo é completar todas as células que estão em branco, utilizando números de 1 a 9 e respeitando as seguintes regras:  toda linha deve possuir todos os números de 1 a 9, sem repetições; toda coluna deve possuir todos os números de 1 a 9, sem repetições. Ao final, todo quadrado de 3x3 também terá os números de 1 a 9 sem repetições.

![Exemplo de um diagrama de Sudoku](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

Ao iniciar o programa, é solicitado ao usuário que o diagrama seja preenchido com a configuração inicial. O diagrama é representado através de uma lista estruturada, cujos elementos são outras 9 listas (cada uma representando uma linha do diagrama), que por sua vez também contém 9 listas internas (que representam as células em branco), cada uma com os números de 1 a 9 – com a exceção dos elementos que foram preenchidos no início (os quais substituem as listas com números de 1 a 9). Essas listas numéricas funcionam como conjuntos de possibilidades, o que significa que o programa ainda não sabe quais dos elementos numéricos irão compor a solução final do quebra cabeça.  A estratégia básica do programa é “enxugar” esses conjuntos de possibilidades, retirando os números que não podem estar naquela posição específica. Isso é feito utilizando procedimentos heurísticos que humanos usualmente empregam quando tentam encontrar a solução. 

Por exemplo, o primeiro número do diagrama (linha 1, coluna 1) é 5. Isso implica que todas as células em branco – conjuntos de possibilidades – na mesma linha não poderão ser preenchidas pelo valor 5, já que isso é contra as regras do jogo. O programa, então, retira o número 5 de todos os conjuntos de possibilidades da linha 1. O mesmo vale para a coluna 1. Essa heurística é implementada através do seguinte código:

```
def enxugando_linhas(a):
    for c in a:		
        for m in c:
            if type(m) == int:
                for k in c:
                    if type(k) == list and m in k:
                        k.remove(m)
    return a


def enxugando_colunas(a):
    for c in a:
        for m, k in enumerate(c):
            if type(k) == int:
                for j in a:
                    if type(j[m]) == list and k in j[m]:
                        j[m].remove(k)
    return a
```

Onde que o parâmetro `a` é a lista que representa o diagrama completo. Outra heurística interessante consiste em eliminar de um conjunto de possibilidades os números que estão preenchidos em outras células, mas no mesmo quadrado que ele. Por exemplo, a célula da linha 1/coluna 3 não pode conter como possibilidade o número 6. Sabemos disso porque já há um 6 nesse quadrado. Mas as funções `enxugando_linhas()` e `enxugando_colunas()` ignoram esse fato, pois o 6 não está na mesma linha ou coluna que a célula da linha 1/coluna 3. Para isso, usamos o código

```
def enxugando_quadrados(a):

    # QUADRADO 1:
    for c in range(0, 3):
        for p in range(0, 3):
            if type(a[c][p]) == int:
                for k in range(0, 3):
                    for j in range(0, 3):
                        if type(a[k][j]) == list and a[c][p] in a[k][j]:
                            a[k][j].remove(a[c][p])
```

Outros laços são usados para os outros quadrados.

Heurísticas desse tipo foram definidas e são aplicadas repetidas vezes até que todos os conjuntos de possibilidades sejam reduzidos a um único valor. Esses valores compõem a solução para o diagrama. 
