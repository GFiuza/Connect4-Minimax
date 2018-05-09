import copy
from Jogo import *
from avaliação import *
PROFUNDIDADEM = 5


class IntArt:
    jogo_copia = None

    def max_retorno(self, contador, alfa, beta):                                                          # Função que retorna o valor da melhor jogada pelo estado atual para a IA
        if self.jogo_copia.alguemGanhou() != 0 or self.jogo_copia.cheio() or contador == PROFUNDIDADEM:   # Verifica teste terminal
            return pontuacao(self.jogo_copia.tabuleiro)                                                   # e retorna o melhor encontrado
        valor_no = float('-inf')                                                                          # Inicia valor para a jogada
        for i in range(7):                                                                                # Para cada possível jogada
            if self.jogo_copia.ondeLivre[i] == -1:                                                        # se a coluna estiver cheia, nada faz
                continue                                                                                  #
            self.jogo_copia.coloca_disco(i)                                                               # realiza a jogada
            valor_no = max(valor_no, self.mini_retorno(contador+1, alfa, beta))                           # analisa valor para as possíveis proximas jogadas
            self.jogo_copia.retira_disco(i)                                                               # retorna o tabuleiro ao estado atual
            if valor_no >= beta:                                                                          # verifica se é possível fazer a poda
                return valor_no                                                                           #
            alfa = max(alfa, valor_no)                                                                    # atualiza valor de alfa, que representa a melhor jogada previamente analisada
        return valor_no                                                                                   #

    def mini_retorno(self, contador, alfa, beta):                                                         # Função que retorna o valor da melhor jogada pelo estado atual para o humano
        if self.jogo_copia.alguemGanhou() != 0 or self.jogo_copia.cheio() or contador == PROFUNDIDADEM:   # Verifica teste terminal
            return pontuacao(self.jogo_copia.tabuleiro)                                                   # e retorna o melhor encontrado
        valor_no = float('inf')                                                                           # Inicia valor para a jogada
        for i in range(7):                                                                                # Para cada possível jogada
            if self.jogo_copia.ondeLivre[i] == -1:                                                        # se a coluna estiver cheia, nada faz
                continue                                                                                  #
            self.jogo_copia.coloca_disco(i)                                                               # realiza a jogada
            valor_no = min(valor_no, self.max_retorno(contador+1, alfa, beta))                            # analisa valor para as possíveis proximas jogadas
            self.jogo_copia.retira_disco(i)                                                               # retorna o tabuleiro ao estado atual
            if valor_no <= alfa:                                                                          # verifica se é possível fazer a poda
                return valor_no                                                                           #
            beta = min(beta, valor_no)                                                                    # atualiza valor de alfa, que representa a melhor jogada previamente analisada
        return valor_no                                                                                   #

    def buscaAlphaBeta(self):                                                               # Função que gerencia a busca, junto com qual será a próxima jogada
        profundidade = 0                                                                    # controla a profundidade maxima
        melhor_jogada = 0                                                                   # representa a coluna da jogada
        valor_no = float('-inf')                                                            # Inicia valor para a jogada
        for i in range(7):                                                                  # Para cada possível jogada
            if self.jogo_copia.ondeLivre[i] == -1:                                          # se a coluna estiver cheia, nada faz
                continue                                                                    #
            self.jogo_copia.coloca_disco(i)                                                 # realiza a jogada
            valor_filho = self.mini_retorno(profundidade + 1, float('-inf'), float('inf'))  # analisa valor para as possíveis proximas jogadas inicializando alfa e beta
            if valor_filho > valor_no:                                                      # verifica se a jogada recém analisada vale mais do que a maior antes atualizada
                melhor_jogada = i                                                           # atualiza índice
                valor_no = valor_filho                                                      # atualiza novo maior valor
            self.jogo_copia.retira_disco(i)                                                 # retorna o tabuleiro ao estado atual
        return melhor_jogada                                                                # retorna a coluna da melhor jogada
