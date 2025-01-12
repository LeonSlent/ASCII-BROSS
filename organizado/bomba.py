import matrizes
import player
import mapa

ativar_bomba = False
existe_bomba = False
relogio_bomba = 0
bomba_y = 0
bomba_x = 0
explosao_y = 0
explosao_x = 0

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
                matriz[bomba_y + i][bomba_x + j] = caractere


def verificar_colisao(matriz, novo_y, novo_x):
    #verifica se as posições da bomba estão dentro da matriz
    if 0 <= novo_y <= matrizes.matriz_y - len(bomba) and 0 <= novo_x <= matrizes.matriz_x - len(bomba):
        #verifica se todos os indices que a bomba irá ocupar estão disponiveis
        for i in range(len(bomba)):
            for j in range(len(bomba)):
                if matriz[novo_y + i][ novo_x + j] != matrizes.vazio:
                    return False
    else:
        return False
    return True

def verificar_bloco(matriz, novo_y, novo_x):
    for i in range(len(explosao)):
        for j in range(len(explosao)):
            if matriz[novo_y + i][novo_x + j] in ["█", "▄", "▐", "▌", "▀"]:
                player.player_vivo = False
            if matriz[novo_y + i][novo_x + j] == "▓":
                return False

    return True


def desenhar_explosao( matriz, bomba_y, bomba_x):
    contador = 5
    #logica para colocar o indice na explosao em uma posicao divisivel por 5
    if bomba_x % 5 < 3:
        explosao_x = bomba_x - (bomba_x % 5)
    else:
        explosao_x = bomba_x + (5 - (bomba_x % 5))
    
    if bomba_y % 5 < 3:
        explosao_y = bomba_y - (bomba_y % 5)
    else:
        explosao_y = bomba_y + (5 - (bomba_y % 5))

    #Desenha a explosao central
    for i, linha in enumerate(explosao):
        for j, caractere in enumerate(linha):
                matriz[explosao_y + i][explosao_x + j] = caractere

    #Desenha a explosão para cima
    while True:
        #verifica se a explosão será desenhada dentro da matriz
        if explosao_y - contador < 0:
            contador = 5
            break
        #verifica se o proximo indice que a explosão irá ocupar é um bloco indestrutivel
        if verificar_bloco(matriz, explosao_y - contador, explosao_x):
            for i, linha in enumerate(explosao):
                #desenha a explosão
                for j, caractere in enumerate(linha):
                    matriz[explosao_y + i - contador][explosao_x + j] = caractere
                    mapa.cenario[explosao_y + i - contador][explosao_x + j] = " "
            contador += 5
        else:
            contador = 5
            break

    #Desenha a explosão para baixo 
    while True:
        #verifica se a explosão será desenhada dentro da matriz
        if explosao_y + contador > 30:
            contador = 5
            break

        #verifica se o proximo indice que a explosão irá ocupar é um bloco indestrutivel
        if verificar_bloco(matriz, explosao_y + contador, explosao_x):
            #desenha a explosão
            for i, linha in enumerate(explosao):
                for j, caractere in enumerate(linha):
                    matriz[explosao_y + i + contador][explosao_x + j] = caractere
                    mapa.cenario[explosao_y + i + contador][explosao_x + j] = " "
            contador += 5
        else:
            contador = 5
            break


    #Desenha a explosão para esquerda
    while True:
        #verifica se a explosão será desenhada dentro da matriz
        if explosao_x - contador < 0:
            contador = 5
            break

        if verificar_bloco(matriz, explosao_y, explosao_x - contador):
            for i, linha in enumerate(explosao):
                for j, caractere in enumerate(linha):
                    matriz[explosao_y + i][explosao_x + j - contador] = caractere
                    mapa.cenario[explosao_y + i][explosao_x + j - contador] = " "
            contador += 5
        else:
            contador = 5
            break

    #Desenha a explosão para direita
    while True:
        #verifica se a explosão será desenhada dentro da matriz
        if explosao_x + contador > 90:
            contador = 5
            break

        if verificar_bloco(matriz, explosao_y, explosao_x + contador):
            for i, linha in enumerate(explosao):
                for j, caractere in enumerate(linha):
                    matriz[explosao_y + i][explosao_x + j + contador] = caractere
                    mapa.cenario[explosao_y + i][explosao_x + j + contador] = " "
            contador += 5
        else:
            contador = 5
            break