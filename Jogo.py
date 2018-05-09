TAM_LIN = 6
TAM_COL = 7

from avaliação import *

class bcolors: # DEFINIÇÃO DE CORES PARA INTERFACE NO TERMINAL
    ROSA = '\033[95m'
    AZUL = '\033[94m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    VERMELHO = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    j1 = BOLD + "_" + AMARELO + "X" + ROSA + "_" + ENDC
    j2 = BOLD + "_" + AZUL + "O" + ROSA + "_" + ENDC
    empty_cell = ROSA + BOLD + "___" + ENDC
    background = ROSA + BOLD

class Jogo: # CLASSE QUE É INSTÂNCIADA NO LOOP                      # A variável tabuleiro é a matriz
    tabuleiro = None                                                # vez é uma variável que varia entre -1 e 1 e indica a
    vez = None                                                      # vez do jogador atual (vez = ID do jogador atual)
    ondeLivre = None                                                # ondeLivre será o vetor auxiliar para casas livres

    def __init__(self):                                             # Faz a inicialização da matriz com valores 0
        self.tabuleiro = [[0] * TAM_COL for i in range(TAM_LIN)]    # Começa o jogo sempre na vez do jogador humano
        self.vez = 1                                                # Cria um vetor auxiliar que marca a posição das
        self.ondeLivre = [TAM_LIN-1] * TAM_COL                      # casas livres para cada coluna. O vetor inicia com [5,5,5,5,5,5,5]

    def coloca_disco(self, col):                                    # Função que insere um disco na coluna col. É uma jogada.
        if self.ondeLivre[col] >= 0:                                # Verifica no vetor auxiliar se a casa está disponível
            self.tabuleiro[self.ondeLivre[col]][col] = self.vez     # Pinta a casa livre da coluna col com o id do jogador atual
            self.vez *= -1                                          # Inverte a var. vez para passar a jogada para o outro jogador
            self.ondeLivre[col] -= 1                                # Diminui de ondeLivre 1 unidade porque col tem uma peça a mais

    def retira_disco(self, col):                                    # Função que retira um disco da coluna col. É uma jogada.
        if self.ondeLivre[col] < 5:                                 # A condição ondeLivre[col] < 5 verifica se tem pelo menos uma peça
            self.ondeLivre[col] += 1                                # naquela coluna. Se houver, aumenta o valor para descer na pilha.
            self.tabuleiro[self.ondeLivre[col]][col] = 0            # Pinta a casa cujo disco foi removido de 0
            self.vez *= -1                                          # Inverte a vez novamente.

    def alguemGanhou(self):                                                         # Função que verifica se algum jogador completou
        for i in range(6):                                                          # uma sequencia de 4 peças consecutivas
            for j in range(7):                                                      # Para cada posição da matriz, ele verifica se aquela
                if(checaVertical(self.tabuleiro, 1, 4, i, j, 0) != 0):              # casa pertence a uma sequencia de 4 peças consecutivas.
                    return 1                                                        # usando funcoes auxiliares para testes na vertical, horizontal e diagonal
                if (checaVertical(self.tabuleiro, -1, 4, i, j, 0) != 0):            #
                    return -1                                                       #
                    # A função faz essa checagem tanto para peças do jogador 1
                if (checaHorizontal(self.tabuleiro, 1, 4, i, j, 0) != 0):           # quanto para peças do jogador 2
                    return 1                                                        #
                if (checaHorizontal(self.tabuleiro, -1, 4, i, j, 0) != 0):          #
                    return -1                                                       #
                    #
                if (checaDiagonal(self.tabuleiro, 1, 4, i, j, 0) != 0):             #
                    return 1                                                        #
                if (checaDiagonal(self.tabuleiro, -1, 4, i, j, 0) != 0):            #
                    return -1                                                       #
                    # Se nenhuma sequencia de 4 for achada,
        return 0                                                                    # a funcao retorna 0

    def cheio(self):                                                                # Usando o auxiliar ondeLivre, verifica
        if sum(self.ondeLivre) == -7:                                               # se o tabuleiro está cheio, resultando num empate
            return True                                                             # ou numa vitória de última hora
        return False                                                                #

    def imprime_vez(self):                                                                          # Imprime_vez, imprime e
        if self.vez == 1:                                                                           # imprime_vencedor sao
            print(bcolors.AMARELO + bcolors.BOLD + "### Vez do jogador 1 ###" + bcolors.ENDC)       # funcoes de interface
        else:                                                                                       #
            print(bcolors.AZUL + bcolors.BOLD + "### Vez do jogador 2 ###" + bcolors.ENDC)          #

    def imprime(self):
        empty_cell = bcolors.empty_cell
        print("\n")
        for i in range(TAM_LIN):
            for j in range(TAM_COL):
                print(bcolors.background + "|", end='')
                if self.tabuleiro[i][j] == 0:
                    print(empty_cell, end='')
                else:
                    if self.tabuleiro[i][j] == 1:
                        print(bcolors.j1, end='')
                    else:
                        print(bcolors.j2, end='')
            print(bcolors.background + "|")

        print(bcolors.background + "  0   1   2   3   4   5   6\n")

    def imprime_vencedor(self):
        if self.alguemGanhou() == 1:
            print("\n" + bcolors.AMARELO + bcolors.BOLD + "!!! JOGADOR 1 VENCEU !!!")
            return
        if self.alguemGanhou() == -1:
            print("\n" + bcolors.AZUL + bcolors.BOLD + "!!! JOGADOR 2 VENCEU !!!")
            return
        if self.cheio():
            print("\n" + bcolors.AMARELO + bcolors.BOLD + "!!! EMP" + bcolors.AZUL + bcolors.BOLD + "ATE !!!")
            return
