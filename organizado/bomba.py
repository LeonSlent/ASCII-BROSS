#Ativar a bomba
ativar_bomba = False

bomba_x = 10
bomba_y = 10

bomba = [
    "        ",
    "   *    ",
    "    *   ",
    "   ▓▓   ",
    "  ▓▓▓▓  ",
    "  ▓▓▓▓  ",
    "   ▓▓   ",
    "        "
]


def desenhar_bomba(matriz):
    '''
        função que desenha a bomba na tela
    '''
    for i, linha in enumerate(bomba):
        for j, caractere in enumerate(linha):
            matriz[bomba_x + i][bomba_y + j] = caractere