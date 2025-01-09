import matrizes

ativar_bomba = False
existe_bomba = False
relogio_bomba = 0
bomba_y = 0
bomba_x = 0

bomba = [
    " *   ",
    "  *  ",
    " ▄█▄ ",
    "▐███▌",
    " ▀▀▀ "
]

explosao = [
    "*****",
    "*****",
    "*****",
    "*****",
    "*****"
]


def desenhar_bomba(matriz, bomba_y, bomba_x):
    '''
        função que desenha a bomba na tela
    '''
    for i, linha in enumerate(bomba):
        for j, caractere in enumerate(linha):
            if matriz[bomba_y + i][bomba_x + j] == ' ':
                matriz[bomba_y + i][bomba_x + j] = caractere

def desenhar_explosao(matriz, bomba_y, bomba_x):
    '''
        função que desenha a explosao na tela
    '''
    #Desenha a explosao central
    for i, linha in enumerate(explosao):
        for j, caractere in enumerate(linha):
            if matriz[bomba_y + i][bomba_x + j] == ' ' or matriz[bomba_y + i][bomba_x + j] == '▓':
                matriz[bomba_y + i][bomba_x + j] = caractere
    #desenha a explosao para a direita
    for i, linha in enumerate(explosao):
        for j, caractere in enumerate(linha):
            if matriz[(bomba_y + i) + 2][bomba_x + j] != '█' or matriz[(bomba_y + i) + 2][bomba_x + j] == '▓':
                matriz[(bomba_y + i) + 2][bomba_x + j] = caractere
    #desenha a explosao para a esquerda
    for i, linha in enumerate(explosao):
        for j, caractere in enumerate(linha):
            if matriz[(bomba_y + i) - 2][bomba_x + j] == ' ' or matriz[(bomba_y + i) - 2][bomba_x + j] == '▓':
                matriz[(bomba_y + i) - 2][bomba_x + j] = caractere
    #desenha a explosao para baixo
    for i, linha in enumerate(explosao):
        for j, caractere in enumerate(linha):
            if matriz[bomba_y + i][(bomba_x + j) + 5] == ' ' or matriz[bomba_y + i][(bomba_x + j) + 5] == '▓':
                matriz[bomba_y + i][(bomba_x + j) + 5] = caractere
    #desenha a explosao para cima
    for i, linha in enumerate(explosao):
        for j, caractere in enumerate(linha):
            if matriz[bomba_y + i][(bomba_x + j) - 5] == ' ' or matriz[bomba_y + i][(bomba_x + j) - 5] == '▓':
                matriz[bomba_y + i][(bomba_x + j) - 5] = caractere        

def verificar_colisao(novo_y, novo_x):
    if 0 <= novo_y <= matrizes.matriz_y - len(bomba) and 0 <= novo_x <= matrizes.matriz_x - len(bomba):
        return True
    else: return False