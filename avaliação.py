def checaVertical(tabuleiro, jogador, qtd, poslinha, poscoluna, printar):
    contador = 0
    j = qtd
    i = poslinha
    while(i < len(tabuleiro) and tabuleiro[i][poscoluna] == jogador and j > 0): #Até que alcance a borda de baixo do tabuleiro, ache peças do jogador escolhido em sequência e até qtd vezes
        contador += 1 #Conta quantas peças do jogador foram achadas em sequência
        i += 1
        j -= 1
    if (contador == qtd): #Caso tenha qtd peças do jogador em sequência
        if (printar == 1 and qtd == 4): #Só printa a(s) jogada(s) que fez o jogador ganhar
            print("4 peças em sequência na vertical!")
            for i in range(poslinha, poslinha + 4):
                print("Posição " + str(i) + ", " + str(poscoluna) + "\n")
        return 1
    return 0

def checaHorizontal(tabuleiro, jogador, qtd, poslinha, poscoluna, printar):
    contador = 0
    j = qtd
    i = poscoluna
    while(i >= 0 and tabuleiro[poslinha][i] == jogador and j > 0): #Até que alcance a borda esquerda do tabuleiro, ache peças do jogador escolhido em sequência e até qtd vezes
        contador += 1
        i -= 1
        j -= 1
    if (contador == qtd): #Se achou qtd peças em sequência na esquerda
        if (printar == 1 and qtd == 4):
            print("4 peças em sequência na horizontal!")
            for i in range(poscoluna-3,poscoluna+1):
                print("Posição " + str(poslinha) + ", " + str(i) + "\n")
        return 1
    i = poscoluna
    j = qtd
    contador = 0
    while(i < len(tabuleiro) and tabuleiro[poslinha][i] == jogador and j > 0): #Até que alcance a borda direita do tabuleiro, ache peças do jogador escolhido em sequência e até qtd vezes
        contador += 1
        i += 1
        j -= 1
    if (contador == qtd): #Se achou qrd peças em sequência na direita
        if (printar == 1 and qtd == 4):
            print("4 peças em sequência na horizontal!")
            for i in (poscoluna+3,poscoluna-1, -1):
                print("Posição " + str(poslinha) + ", " + str(i) + "\n")
        return 1
    return 0

def checaDiagonal(tabuleiro, jogador, qtd, poslinha, poscoluna, printar):
    diagonais = 0
    contador = 0
    k = qtd
    i = poslinha
    j = poscoluna
    #Vamos checar primeiro a diagonal que começa no topo e termina em baixo
    while(i > -1 and j > -1 and tabuleiro[i][j] == jogador and k > 0): #Primeira metade da diagonal 
        contador += 1
        i -= 1
        j -= 1
        k -= 1
    if (contador == qtd):
        if (printar == 1 and qtd == 4):
            print("4 peças em sequência na primeira diagonal!")
            i = poslinha-3
            j = poscoluna-3
            k = qtd
            while(k > 0):
                print("Posição " + str(i) + ", " + str(j) + "\n")
                i += 1
                j += 1
                k -= 1
        diagonais = 1
        
    contador = 0
    k = qtd
    i = poslinha
    j = poscoluna
    while(i < len(tabuleiro) and j < len(tabuleiro[i]) and tabuleiro[i][j] == jogador and k > 0): #Segunda metade da diagonal 
        contador += 1
        i += 1
        j += 1
        k -= 1
    if (contador == qtd):
        if (printar == 1 and qtd == 4):
            print("4 peças em sequência na primeira diagonal!")
            i = poslinha+3
            j = poscoluna+3
            k = qtd
            while(k > 0):
                print("Posição " + str(i) + ", " + str(j) + "\n")
                i -= 1
                j -= 1
                k -= 1
        diagonais = 1
        
    contador = 0
    k = qtd
    i = poslinha
    j = poscoluna
    #Vamos checar a diagonal que começa em baixo e termina no topo
    while(i < len(tabuleiro) and j > -1 and tabuleiro[i][j] == jogador and k > 0): #Primeira metade da diagonal 
        contador += 1
        i += 1
        j -= 1
        k -= 1
    if (contador == qtd):
        if (printar == 1 and qtd == 4):
            print("4 peças em sequência na segunda diagonal!")
            i = poslinha+3
            j = poscoluna-3
            k = qtd
            while(k > 0):
                print("Posição " + str(i) + ", " + str(j) + "\n")
                i -= 1
                j += 1
                k -= 1
        return diagonais+1

    contador = 0
    k = qtd
    i = poslinha
    j = poscoluna
    #Vamos checar a diagonal que começa em baixo e termina no topo
    while(i > -1 and j < len(tabuleiro[i]) and tabuleiro[i][j] == jogador and k > 0): #Segunda metade da diagonal 
        contador += 1
        i -= 1
        j += 1
        k -= 1
    if (contador == qtd):
        if (printar == 1 and qtd == 4):
            print("4 peças em sequência na segunda diagonal!")
            i = poslinha-3
            j = poscoluna+3
            k = qtd
            while(k > 0):
                print("Posição " + str(i) + ", " + str(j) + "\n")
                i += 1
                j -= 1
                k -= 1
        return diagonais+1
    return diagonais

        
def pontuacao(tabuleiro):
    pontJogador = checaQuantidade(tabuleiro, -1, 2, 0) + 25*checaQuantidade(tabuleiro, -1, 3, 0) + 10000*checaQuantidade(tabuleiro, -1, 4, 0)
    #print("Pontuação do jogador: " + str(pontJogador) + "\n")
    pontIA = checaQuantidade(tabuleiro, 1, 2, 0) + 25*checaQuantidade(tabuleiro, 1, 3, 0) + 10000*checaQuantidade(tabuleiro, 1, 4, 0)
    #print("Pontuação da IA: " + str(pontIA) + "\n")
    return pontJogador - pontIA

def checaQuantidade(tabuleiro, jogador, qtdPecas, printar):
    contador=0
    for i in range(0,6):
        for j in range(0,7):
            contador += checaVertical(tabuleiro,jogador,qtdPecas, i, j, printar)
            contador += checaHorizontal(tabuleiro,jogador,qtdPecas, i, j, printar)
            contador += checaDiagonal(tabuleiro,jogador,qtdPecas, i, j, printar)
    return contador
