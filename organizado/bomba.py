

ativar_bomba = False
existe_bomba = False

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