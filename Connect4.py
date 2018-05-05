import os
import sys
from Jogo import Jogo
from Jogo import bcolors
# from minimax import Int_Art
from minimax_poda import IntArt

clear = lambda: os.system('cls')

sys.setrecursionlimit(1500)

def mainLoop():
    xogao = Jogo()
    computador = IntArt()
    computador.jogo_copia = xogao

    while(True):
        clear()
        os.system('cls')
        xogao.imprime()
        xogao.imprime_vez()

        entrada = int(input(bcolors.BOLD + bcolors.VERDE + "Sua vez: "))

        while entrada > 7 or entrada < 0 or xogao.ondeLivre[entrada] < 0:
            entrada = int(input(bcolors.BOLD + bcolors.VERMELHO + "Diga uma coluna válida"))
            if xogao.ondeLivre[entrada] < 0:
                continue

        xogao.coloca_disco(entrada)
        xogao.coloca_disco(computador.buscaAlphaBeta())

        if xogao.alguemGanhou() != 0 or xogao.cheio():
            xogao.imprime_vencedor()
            break


mainLoop()
