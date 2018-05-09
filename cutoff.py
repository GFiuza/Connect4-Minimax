from avaliação import pontuacao


def cutoff(ia, contador, eh_min):       # Função de cutoff. Ele avalia as possíveis de 4 espaços no tabuleiro
                                        # e avalia se o jogador tem chance de colocar 4 peças naquele lugar
    if contador < 2:                    # A função só funciona para profundidades a partir de 2
        return False                    # senão ela não consegue bloquear certos movimentos do jogador

    jogo = ia.jogo_copia.tabuleiro
    possibilidades_ia = 0
    possibilidades_jogador = 0

    for i in range(len(jogo)):                              # Em cada linha, extrai subvetores de quatro
        for j in range(0, len(jogo[i]) - 4):                # posições e avalia se há uma ou mais peças
            n = min(jogo[i][j:j+4]) + max(jogo[i][j:j+4])   # pertencentes somente à um jogador e avalia
            if n < 0 and jogo[i][j:j+4].count(0) == 1:      # quantas peças há. Se tem duas peças, aumenta
                possibilidades_ia += 7                      # a probabilidade da pessoa em 3. Se for três peças,
            elif n > 0 and jogo[i][j:j+4].count(0) == 1:    # aumenta em 7.
                possibilidades_jogador += 7
            elif n < 0 and jogo[i][j:j + 4].count(0) == 2:
                possibilidades_ia += 3
            elif n > 0 and jogo[i][j:j + 4].count(0) == 2:
                possibilidades_jogador += 3

    for j in range(len(jogo[0])):                           # Mesma coisa que a função de cima, mas agora com as
        for i in range(0, len(jogo) - 4):                   # colunas. O algoritmo extraisubcolunas, transformando-as
                                                            # em um vetor de quatro posições.
            temp = []
            for k in range(i, i+4):
                temp.append(jogo[k][j])

            n = min(temp) + max(temp)
            if n < 0 and temp.count(0) == 1:
                possibilidades_ia += 7
            elif n > 0 and temp.count(0) == 1:
                possibilidades_jogador += 7
            elif n < 0 and temp.count(0) == 2:
                possibilidades_ia += 3
            elif n > 0 and temp.count(0) == 2:
                possibilidades_jogador += 3

    for i in range(len(jogo) - 3):                          # Mesma coisa que as funções de cima, mas agora
        for j in range(len(jogo[i]) - 3):                   # pegando as diagonais de cima para baixo, novamente
            temp = diagonal_cima_baixo(jogo, i, j)          # transformando-as em um vetor de quatro posições
            n = min(temp) + max(temp)                       # para ser mais fácil de trabalhar ocm os dados.
            if n < 0 and temp.count(0) == 1:                # Para extrair a coluna e colocar em um vetor,
                possibilidades_ia += 7                      # utiliza a função auxiliar diagonal_cima_baixo()
            elif n > 0 and temp.count(0) == 1:
                possibilidades_jogador += 7
            elif n < 0 and temp.count(0) == 2:
                possibilidades_ia += 3
            elif n > 0 and temp.count(0) == 2:
                possibilidades_jogador += 3

    for i in range(3, len(jogo)):                           # Idêntico à função anterior, mas agora usando a função
        for j in range(len(jogo[i]) - 3):                   # diagonal_baixo_cima() para extrair as diagonais de baixo
            temp = diagonal_baixo_cima(jogo, i, j)          # pra cima. NOTA: quando falo de diagonal de baixo pra cima
            n = min(temp) + max(temp)                       # e de cima pra baixo, me refiro da esquerda para a direita
            if n < 0 and temp.count(0) == 1:
                possibilidades_ia += 7
            elif n > 0 and temp.count(0) == 1:
                possibilidades_jogador += 7
            elif n < 0 and temp.count(0) == 2:
                possibilidades_ia += 3
            elif n > 0 and temp.count(0) == 2:
                possibilidades_jogador += 3

    if possibilidades_jogador > 2*possibilidades_ia:    # Se as possibilidades do jogador for maior do que
        return True                                     # o dobro das possibilidades da IA, cutoff é ativado,
    else:                                               # caso contrário, a recursão continua no minimax
        return False


def diagonal_cima_baixo(jogo, i, j):    # Retorna uma lista com os valores da diagonal de cima pra baixo,
    resp = []                           # a partir de um dado elemento
    for n in range(4):
        resp.append(jogo[i+n][j+n])
    return resp


def diagonal_baixo_cima(jogo, i, j):    # Retorna uma lista com os valores da diagonal de baixo pra cima,
    resp = []                           # a partir de um dado elemento
    for n in range(4):
        resp.append(jogo[i-n][j+n])
    return resp
