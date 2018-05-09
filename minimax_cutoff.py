import copy
from Jogo import *
from avaliação import *
from cutoff import cutoff  # , cutoff_quant, cutoff_quant_zera
PROFUNDIDADEM = 5

class Int_Art:
    jogo_copia = None

    def max_retorno(self, contador):
        if self.jogo_copia.alguemGanhou() != 0 or self.jogo_copia.cheio() or contador == PROFUNDIDADEM or cutoff(self, contador, False):
            return pontuacao(self.jogo_copia.tabuleiro)     # Se alguém ganhou, ou se o tabuleiro está cheio,
        valor_no = float('-inf')                            # ou atingiu a profundidade, ou o cutoff retornou true,
        for i in range(7):                                  # o nó se torna folha. caso não seja folha, expande a
            if self.jogo_copia.ondeLivre[i] == -1:          # árvore de recursão onde há jogadas e chama a função de
                continue                                    # mínimo para os filhos, escolhendo o valor máximo
            self.jogo_copia.coloca_disco(i)                 # entre eles.
            valor_no = max(valor_no, self.mini_retorno(contador+1))
            self.jogo_copia.retira_disco(i)
        return valor_no

    def mini_retorno(self, contador):
        if self.jogo_copia.alguemGanhou() != 0 or self.jogo_copia.cheio() or contador == PROFUNDIDADEM or cutoff(self, contador, True):
            return pontuacao(self.jogo_copia.tabuleiro)     # Mesmas condições para o nó se tornar folha que a
        valor_no = float('inf')                             # função anterior. Se for folha, retorna o valor do
        for i in range(7):                                  # tabuleiro. Senão, Expande a recursão para os filhos
            if self.jogo_copia.ondeLivre[i] == -1:          # disponíveis, chamando função de máximo para eles
                continue                                    # e seleciona o menor valor dentre todos os filhos.
            self.jogo_copia.coloca_disco(i)
            valor_no = min(valor_no, self.max_retorno(contador+1))
            self.jogo_copia.retira_disco(i)
        return valor_no

    def minimax_retorno(self):                          # Inicializa a chamada recursiva do algoritmo minimax,
        profundidade = 0                                # e ao final de tudo, escolhe a melhor jogada computada
        melhor_jogada = 0                               # e a executa. Essa primeira iteração se comporta como
        valor_no = float('-inf')                        # o algoritmo de máximo, pois chama o mínimo para seus filhos
        for i in range(7):                              # e retorna o maior dentre eles.
            if self.jogo_copia.ondeLivre[i] == -1:
                continue
            self.jogo_copia.coloca_disco(i)
            valor_filho = self.mini_retorno(profundidade+1)

            if valor_filho > valor_no:
                melhor_jogada = i
                valor_no = valor_filho
            self.jogo_copia.retira_disco(i)
        return melhor_jogada
