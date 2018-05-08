import os
import sys
from Jogo import Jogo
from Jogo import bcolors
from minimax_cutoff import Int_Art
# from minimax import Int_Art
# from minimax_poda import IntArt

clear = lambda: os.system('cls')

sys.setrecursionlimit(1500)


def mainLoop():
    xogao = Jogo()
    computador = Int_Art()
    computador.jogo_copia = xogao
    xogao.imprime()

    while True:
        xogao.imprime_vez()

        entrada = int(input(bcolors.BOLD + bcolors.VERDE + "Sua vez: "))

        while entrada > 6 or entrada < 0 or xogao.ondeLivre[entrada] < 0:
            entrada = int(input(bcolors.BOLD + bcolors.VERMELHO + "Diga uma coluna válida: "))
            if entrada <= 6 and entrada >= 0 and xogao.ondeLivre[entrada] < 0:
                continue

        xogao.coloca_disco(entrada)
        clear()
        os.system('cls')
        xogao.imprime()

        if xogao.alguemGanhou() != 0 or xogao.cheio():
            xogao.imprime_vencedor()
            break

        xogao.imprime_vez()

        xogao.coloca_disco(computador.minimax_retorno())
        clear()
        os.system('cls')
        xogao.imprime()

        if xogao.alguemGanhou() != 0 or xogao.cheio():
            xogao.imprime_vencedor()
            break


mainLoop()
