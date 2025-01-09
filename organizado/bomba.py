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
    " * * ",
    "*****",
    " *** ",
    "*****",
    " * * "
]


def desenhar_bomba(matriz, bomba_y, bomba_x):
    '''
        função que desenha a bomba na tela
    '''
    for i, linha in enumerate(bomba):
        for j, caractere in enumerate(linha):
            matriz[bomba_y + i][bomba_x + j] = caractere


def verificar_colisao(novo_y, novo_x):
    if 0 <= novo_y <= matrizes.matriz_y - len(bomba) and 0 <= novo_x <= matrizes.matriz_x - len(bomba):
        return True
    else: return False