import matrizes

player_y = 0
player_x = 0

angulo_player = "baixo"



player_baixo = [
        " ▄▄▄ ",
        " ▄█▄ ",
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

def verificar_colisao(novo_y, novo_x):
    '''
    Verifica se uma posição na matriz está disponível para movimentação.
    Retorna True se a posição está livre e False se há colisão.
    '''
    if 0 <= novo_y <= matrizes.matriz_y - len(player_baixo) and 0 <= novo_x <= matrizes.matriz_x - len(player_baixo[0]):
        return True
    else:
        return False