import copy
from Jogo import *
from avaliação import *
from cutoff import cutoff, cutoff_quant, cutoff_quant_zera
PROFUNDIDADEM = 5

class Int_Art:
    jogo_copia = None

    def max_retorno(self, contador):
        if self.jogo_copia.alguemGanhou() != 0 or self.jogo_copia.cheio() or contador == PROFUNDIDADEM or cutoff(self, contador, False):
            return pontuacao(self.jogo_copia.tabuleiro)
        valor_no = float('-inf')
        for i in range(7):
            if self.jogo_copia.ondeLivre[i] == -1:
                continue
            self.jogo_copia.coloca_disco(i)
            valor_no = max(valor_no, self.mini_retorno(contador+1))
            self.jogo_copia.retira_disco(i)
        return valor_no

    def mini_retorno(self, contador):
        if self.jogo_copia.alguemGanhou() != 0 or self.jogo_copia.cheio() or contador == PROFUNDIDADEM or cutoff(self, contador, True):
            return pontuacao(self.jogo_copia.tabuleiro)
        valor_no = float('inf')
        for i in range(7):
            if self.jogo_copia.ondeLivre[i] == -1:
                continue
            self.jogo_copia.coloca_disco(i)
            valor_no = min(valor_no, self.max_retorno(contador+1))
            self.jogo_copia.retira_disco(i)
        return valor_no

    def minimax_retorno(self):
        cutoff_quant_zera()
        profundidade = 0
        melhor_jogada = 0
        valor_no = float('-inf')
        for i in range(7):
            if self.jogo_copia.ondeLivre[i] == -1:
                continue
            self.jogo_copia.coloca_disco(i)
            valor_filho = self.mini_retorno(profundidade+1)

            # print("Filho =", valor_filho)
            if valor_filho > valor_no:
                melhor_jogada = i
                valor_no = valor_filho
            self.jogo_copia.retira_disco(i)
        #
        cutoff_quant()
        return melhor_jogada