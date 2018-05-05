TAM_LIN = 6
TAM_COL = 7

from avaliação import *

class bcolors:
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

class Jogo:
    tabuleiro = None
    vez = None
    ondeLivre = None

    def __init__(self):
        self.tabuleiro = [[0] * TAM_COL for i in range(TAM_LIN)]
        self.vez = 1
        self.ondeLivre = [TAM_LIN-1] * TAM_COL

    def coloca_disco(self, col):
        if self.ondeLivre[col] >= 0:
            self.tabuleiro[self.ondeLivre[col]][col] = self.vez
            self.vez *= -1
            self.ondeLivre[col] -= 1

    def retira_disco(self, col):
        if self.ondeLivre[col] < 5:
            self.ondeLivre[col] += 1
            self.tabuleiro[self.ondeLivre[col]][col] = 0
            self.vez *= -1

    def alguemGanhou(self):
        for i in range(6):
            for j in range(7):
                if(checaVertical(self.tabuleiro, 1, 4, i, j, 0) != 0):
                    return 1
                if (checaVertical(self.tabuleiro, -1, 4, i, j, 0) != 0):
                    return -1

                if (checaHorizontal(self.tabuleiro, 1, 4, i, j, 0) != 0):
                    return 1
                if (checaHorizontal(self.tabuleiro, -1, 4, i, j, 0) != 0):
                    return -1

                if (checaDiagonal(self.tabuleiro, 1, 4, i, j, 0) != 0):
                    return 1
                if (checaDiagonal(self.tabuleiro, -1, 4, i, j, 0) != 0):
                    return -1
        '''onde_cont = 0
        #Horizontal
        for i in range(TAM_LIN - 1,TAM_LIN - self.ondeLivre[onde_cont], -1):
            onde_cont += 1
            for j in range(0,TAM_COL - 3):
                total = self.tabuleiro[i][j] +  self.tabuleiro[i][j+1] + self.tabuleiro[i][j+2 ] + self.tabuleiro[i][j+3]
                if total == 4:
                    return 1
                if total == -4:
                    return -1

        #Vertical
        for i in range(TAM_LIN - 1, 2, -1):
            for j in range(0, TAM_COL - 1):
                if self.ondeLivre[j] < 2:
                    total = self.tabuleiro[i][j] +  self.tabuleiro[i-1][j] + self.tabuleiro[i-2][j] + self.tabuleiro[i-3][j]
                    if total == 4:
                        return 1
                    if total == -4:
                        return -1


        #Diagonal Crescente
        for i in range(TAM_LIN - 1, 2, -1):
            for j in range(0, TAM_COL - 3):
                if self.ondeLivre[j+3] < 2: # Verifica ultima coluna da diagonal crescente
                    total = self.tabuleiro[i][j] +  self.tabuleiro[i-1][j+1] + self.tabuleiro[i-2][j+2] + self.tabuleiro[i-3][j+3]
                    if total == 4:
                        return 1
                    if total == -4:
                        return -1

        # Diagonal Decrescente
        for i in range(TAM_LIN - 1, 2, -1):
            for j in range(0, TAM_COL - 3):
                if self.ondeLivre[j] < 2:  # Verifica a primeira coluna da diagonal decrescente
                    total = self.tabuleiro[i-3][j] + self.tabuleiro[i-2][j+1] + self.tabuleiro[i-1][j+2] + self.tabuleiro[i][j+3]
                    if total == 4:
                        return 1
                    if total == -4:
                        return -1'''
        return 0

    def cheio(self):
        if sum(self.ondeLivre) == -7:
            return True
        return False

    def imprime_vez(self):
        if self.vez == 1:
            print(bcolors.AMARELO + bcolors.BOLD + "### Vez do jogador 1 ###" + bcolors.ENDC)
        else:
            print(bcolors.AZUL + bcolors.BOLD + "### Vez do jogador 2 ###" + bcolors.ENDC)

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
        if self.cheio():
            self.tabuleiro = [[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1]]
            return
        if self.alguemGanhou() == 1:
            self.tabuleiro = [[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1]]
            self.imprime()
            print("\n" + bcolors.AMARELO + bcolors.BOLD + "!!! JOGADOR 1 VENCEU !!!")
        if self.alguemGanhou() == -1:
            self.tabuleiro = [[-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1,-1]]
            self.imprime()
            print("\n" + bcolors.AZUL + bcolors.BOLD + "!!! JOGADOR 2 VENCEU !!!")
