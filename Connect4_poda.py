import os
import sys
from Jogo import Jogo
from Jogo import bcolors
from minimax_poda import IntArt
clear = lambda: os.system('cls')
                                                                                                # Esse comando foi inserida para evitar
#sys.setrecursionlimit(1500)                                                                    # que a pilha estourasse antes
                                                                                                # da implementacao das buscas.
                                                                                                # Após as estratégicas de poda e
                                                                                                # heurística, a parada da recursão
                                                                                                # mais rápida parece ter restringido
                                                                                                # o estouro.

def mainLoop():                                                                                 # Cria uma instancia de Jogo
    xogao = Jogo()                                                                              # Cria uma instancia de IntArt
    computador = IntArt()                                                                       # Cria uma cópia do jogo para passar
    computador.jogo_copia = xogao                                                               # dentro do loop
    xogao.imprime()                                                                             # printa o estado atual

    while True:                                                                                 # Escopo do loop principal
        xogao.imprime_vez()                                                                     #
                                                                                                #
        entrada = int(input(bcolors.BOLD + bcolors.VERDE + "Sua vez: "))                        # Lê a entrada do jogador humano.
                                                                                                #
        while entrada > 6 or entrada < 0 or xogao.ondeLivre[entrada] < 0:                       # Limita a entrada de inteiros para valores
            entrada = int(input(bcolors.BOLD + bcolors.VERMELHO + "Diga uma coluna válida: "))  # válidos
            if entrada <= 6 and entrada >= 0 and xogao.ondeLivre[entrada] < 0:                  # Se uma coluna está cheia, não pode inserir
                continue                                                                        # uma peça nela

        xogao.coloca_disco(entrada)                                                             # Chama a função de Jogo para inserir uma
        clear()                                                                                 # peça no tabuleiro
        os.system('cls')                                                                        #
        xogao.imprime()                                                                         # Imprime o estado atual

        if xogao.alguemGanhou() != 0 or xogao.cheio():                                          # Verifica se há alguma condição de parada
            xogao.imprime_vencedor()                                                            # para dar um break no loop
            break                                                                               #

        xogao.imprime_vez()

        xogao.coloca_disco(computador.buscaAlphaBeta())                                         # Já com a vez invertida, chama a funcao
        clear()                                                                                 # de colocar disco para a instancia de IA
        os.system('cls')
        xogao.imprime()

        if xogao.alguemGanhou() != 0 or xogao.cheio():                                          # Verifica novamente se houve uma
            xogao.imprime_vencedor()                                                            # condicao de parada (empate ou vitoria)
            break                                                                               # e faz um break se houver.

mainLoop()                                                                                      # chama o mainLoop()
