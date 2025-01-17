import matrizes
import player
import mapa

#Player_1
ativar_bomba_um = False
existe_bomba_um = False
relogio_bomba_um = 0
bomba_y_um = 0
bomba_x_um = 0
explosao_y_um = 0
explosao_x_um = 0

#Player_2
ativar_bomba_dois = False
existe_bomba_dois = False
relogio_bomba_dois = 0
bomba_y_dois = 0
bomba_x_dois = 0
explosao_y_dois = 0
explosao_x_dois = 0


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

def bloco_indestrutivel(matriz, novo_y, novo_x):
    #verifica o novo indice
    for i in range(len(explosao)):
        for j in range(len(explosao)):


                
            #verifica se a explosão pegou no player
            if matriz[novo_y + i][novo_x + j] in ["\033[36m█\033[0m", "\033[36m▄\033[0m", "\033[36m▐\033[0m", "\033[36m▌\033[0m", "\033[36m▀\033[0m"]:
                player.player_vivo_um = False
            if matriz[novo_y + i][novo_x + j] in ["\033[91m█\033[0m", "\033[91m▄\033[0m", "\033[91m▐\033[0m", "\033[91m▌\033[0m", "\033[91m▀\033[0m"]:
                player.player_vivo_dois = False


            #verifica se é um bloco indestrutivel
            if matriz[novo_y + i][novo_x + j] == "█":
                return False

    return True

def bloco_destrutivel(matriz, novo_y, novo_x):
    #verifica o novo indice
    for i in range(len(explosao)):
        for j in range(len(explosao)):

            if matriz[novo_y + i][novo_x + j] == "░":
                return True
    return False



def desenhar_explosao(matriz, bomba_y, bomba_x):
    raio_explosao = 5
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
        if explosao_y - raio_explosao < 0:
            raio_explosao = 5
            break
        #verifica se o proximo indice que a explosão irá ocupar é um bloco indestrutivel
        if bloco_indestrutivel(matriz, explosao_y - raio_explosao, explosao_x):
            if bloco_destrutivel(matriz, explosao_y - raio_explosao, explosao_x) and raio_explosao > 10:
                raio_explosao = 5
                break
            #desenha a explosão
            for i, linha in enumerate(explosao):
                for j, caractere in enumerate(linha):
                    matriz[explosao_y + i - raio_explosao][explosao_x + j] = caractere
                    mapa.copia_cenario[explosao_y + i - raio_explosao][explosao_x + j] = " "
            raio_explosao += 5

        else:
            raio_explosao = 5
            break

        



    #Desenha a explosão para baixo 
    while True:
        #verifica se a explosão será desenhada dentro da matriz
        if explosao_y + raio_explosao > 30:
            raio_explosao = 5
            break

        #verifica se o proximo indice que a explosão irá ocupar é um bloco indestrutivel
        if bloco_indestrutivel(matriz, explosao_y + raio_explosao, explosao_x):
            if bloco_destrutivel(matriz, explosao_y + raio_explosao, explosao_x) and raio_explosao > 10:
                raio_explosao = 5
                break
            #desenha a explosão
            for i, linha in enumerate(explosao):
                for j, caractere in enumerate(linha):
                    matriz[explosao_y + i + raio_explosao][explosao_x + j] = caractere
                    mapa.copia_cenario[explosao_y + i + raio_explosao][explosao_x + j] = " "
            raio_explosao += 5

        else:
            raio_explosao = 5
            break




    #Desenha a explosão para esquerda
    while True:
        #verifica se a explosão será desenhada dentro da matriz
        if explosao_x - raio_explosao < 0:
            raio_explosao = 5
            break

        #verifica se o proximo indice que a explosão irá ocupar é um bloco indestrutivel
        if bloco_indestrutivel(matriz, explosao_y, explosao_x - raio_explosao):
            if bloco_destrutivel(matriz, explosao_y, explosao_x - raio_explosao) and raio_explosao > 10:
                raio_explosao = 5
                break
            #desenha a explosão
            for i, linha in enumerate(explosao):
                for j, caractere in enumerate(linha):
                    matriz[explosao_y + i][explosao_x + j - raio_explosao] = caractere
                    mapa.copia_cenario[explosao_y + i][explosao_x + j - raio_explosao] = " "
            raio_explosao += 5

        else:
            raio_explosao = 5
            break




    #Desenha a explosão para direita
    while True:
        #verifica se a explosão será desenhada dentro da matriz
        if explosao_x + raio_explosao > 90:
            raio_explosao = 5
            break

        #verifica se o proximo indice que a explosão irá ocupar é um bloco indestrutivel
        if bloco_indestrutivel(matriz, explosao_y, explosao_x + raio_explosao):
            if bloco_destrutivel(matriz, explosao_y, explosao_x + raio_explosao) and raio_explosao > 10:
                raio_explosao = 5
                break
            #desenha a explosão
            for i, linha in enumerate(explosao):
                for j, caractere in enumerate(linha):
                    matriz[explosao_y + i][explosao_x + j + raio_explosao] = caractere
                    mapa.copia_cenario[explosao_y + i][explosao_x + j + raio_explosao] = " "
            raio_explosao += 5

        else:
            raio_explosao = 5
            break
