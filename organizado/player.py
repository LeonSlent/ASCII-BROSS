import matrizes

player_y = 0
player_x = 0

angulo_player = "baixo"
player_vivo = True



player_baixo = [
        " ▄▄▄ ",
        " ▄▀▄ ",
        "▐███▌",
        " ▐▀▌ ",
        " ▀ ▀ "
]

player_cima = [
        " ▄▄▄ ",
        " ███ ",
        "▐███▌",
        " ▐▀▌ ",
        " ▀ ▀ "
]

player_direita = [
        " ▄▄▄ ",
        " ██▄ ",
        "▐███▌",
        " █▀▌ ",
        " ▀ ▀ "
]

player_esquerda = [
        " ▄▄▄ ",
        " ▄██ ",
        "▐███▌",
        " ▐▀█ ",
        " ▀ ▀ "
]

def desenhar_player(matriz, player):
    '''
        função que desenha o player na tela
    '''
    for i, linha in enumerate(player):
        for j, caractere in enumerate(linha):
            matriz[player_y + i][player_x + j] = caractere

def verificar_colisao(matriz, novo_y, novo_x, angulo):
    '''
    Verifica se uma posição na matriz está disponível para movimentação.
    Retorna True se a posição está livre e False se há colisão.
    '''
    #verifica se as novas posições do player estão dentro da matriz
    if 0 <= novo_y <= matrizes.matriz_y - len(player_baixo) and 0 <= novo_x <= matrizes.matriz_x - len(player_baixo[0]):
        #verifica qual angulo o player ira se mover e verifica se as novas posições que irá ocupar estão disponiveis
        if angulo == "direita":
            for i in range(len(player_baixo)):
                if matriz[novo_y + i][novo_x + len(player_baixo) - 1] != matrizes.vazio:
                    return False
        elif angulo == "esquerda":
            for i in range(len(player_baixo)):
                if matriz[novo_y + i][novo_x] != matrizes.vazio:
                    return False
        elif angulo == "cima":
            for i in range(len(player_baixo)):
                if matriz[novo_y][novo_x + i] != matrizes.vazio:
                    return False
        elif angulo == "baixo":
            for i in range(len(player_baixo)):
                if matriz[novo_y + len(player_baixo) - 1][novo_x + i] != matrizes.vazio:
                    return False
    else:
        return False
    return True

def calcular_pontuacoes(player_vivo):
    arquivo = open("pontuacoes.txt", "a+")
    if  player_vivo:
        arquivo.write("+30\n")
    else:
        arquivo.write("-30\n")

    arquivo.seek(0)

    with open("pontuacoes.txt") as arquivo_pontuacao:
        soma = 0
        for pontos in arquivo_pontuacao:
         pontos = pontos.strip()
         if pontos:
                valor = eval(pontos)
                soma += int(valor)
        with open("pontuacoes.txt", "w") as arquivo_saida:
            arquivo_saida.write(str(soma))

        print(f"Soma total das pontuações: {soma}")
calcular_pontuacoes(player_vivo)
