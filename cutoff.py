from avaliação import pontuacao

quant = 0
func = 0


def cutoff_quant():
    print("Quantidade de vezes que a função foi chamada =", func)
    print("Quantidade de cutoffs =", quant)
    print("Porcentagem =", quant/func)


def cutoff_quant_zera():
    global quant
    global func
    quant = 0
    func = 0


def cutoff(ia, contador, eh_min):
    global func
    func += 1
    if contador < 2:
        return False

    jogo = ia.jogo_copia.tabuleiro
    possibilidades_ia = 0
    possibilidades_jogador = 0

    # Linhas
    for i in range(len(jogo)):
        for j in range(0, len(jogo[i]) - 4):
            n = min(jogo[i][j:j+4]) + max(jogo[i][j:j+4])
            if n < 0:
                possibilidades_ia += 1
            elif n > 0:
                possibilidades_jogador += 1

    # Colunas
    for j in range(len(jogo[0])):
        for i in range(0, len(jogo) - 4):

            temp = []
            for k in range(i, i+4):
                temp.append(jogo[k][j])

            n = min(temp) + max(temp)
            if n < 0:
                possibilidades_ia += 1
            elif n > 0:
                possibilidades_jogador += 1

    # Diagonais cima pra baixo
    for i in range(len(jogo) - 3):
        for j in range(len(jogo[i]) - 3):
            temp = diagonal_cima_baixo(jogo, i, j)
            n = min(temp) + max(temp)
            if n < 0:
                possibilidades_ia += 1
            elif n > 0:
                possibilidades_jogador += 1

    #Diagonal baixo pra cima
    for i in range(3, len(jogo)):
        for j in range(len(jogo[i]) - 3):
            temp = diagonal_baixo_cima(jogo, i, j)
            n = min(temp) + max(temp)
            if n < 0:
                possibilidades_ia += 1
            elif n > 0:
                possibilidades_jogador += 1

    if possibilidades_jogador > possibilidades_ia:
        global quant
        quant += 1
        return True
    else:
        return False

    if eh_min:  # Se estiver calculando o mínimo, ou seja, simulando a jogada do jogador
        # Se a IA possir mais jogadas que o jogador, ativa o cutoff
        if possibilidades_jogador < possibilidades_ia:
            return True
        else:
            return False
    else:  # Se estiver calculando o max, ou seja, simulando jogada da IA
        # Se o jogador tiver mais possibilidades que a IA, ativa o cutoff
        if possibilidades_jogador > possibilidades_ia:
            return True
        else:
            return False

# Retorna uma lista com os valores da diagonal de cima pra baixo (\)
def diagonal_cima_baixo(jogo, i, j):
    resp = []
    for n in range(4):
        resp.append(jogo[i+n][j+n])
    return resp

# Retorna uma lista com os valores da diagonal de baixo pra cima (/)
def diagonal_baixo_cima(jogo, i, j):
    resp = []
    for n in range(4):
        resp.append(jogo[i-n][j+n])
    return resp
