import matrizes
import menu
import WConio2

#Player 1
player_y_um = 0
player_x_um = 0

angulo_player_um = "baixo"
player_vivo_um = True
pontuacao_player_um = 0

#Player 2
player_y_dois = 30
player_x_dois = 90

angulo_player_dois = "baixo"
player_vivo_dois = True
pontuacao_player_dois = 0

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

def colorir_player(player, cor):
    player_colorido = [
        list("     "),
        list("     "),
        list("     "),
        list("     "),
        list("     ")
    ]
    for i, linha in enumerate(player):
        for j, caractere in enumerate(linha):
            if cor == 1 and caractere != " ":
                player_colorido[i][j] = f"\033[36m{caractere}\033[0m" 
            if cor == 2 and caractere != " ":
                player_colorido[i][j] = f"\033[91m{caractere}\033[0m" 
    return player_colorido

player_baixo_um = colorir_player(player_baixo, 1)
player_cima_um = colorir_player(player_cima, 1)
player_direita_um = colorir_player(player_direita, 1)
player_esquerda_um = colorir_player(player_esquerda, 1)

player_baixo_dois = colorir_player(player_baixo, 2)
player_cima_dois = colorir_player(player_cima, 2)
player_direita_dois = colorir_player(player_direita, 2)
player_esquerda_dois = colorir_player(player_esquerda, 2)

def desenhar_player(matriz, player, player_y, player_x):
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


def calcular_pontuacoes():
    global pontuacao_player_um, pontuacao_player_dois
    try:
        with open("pontuacoes.txt", "a+") as arquivo_pontuacao:
            arquivo_pontuacao.seek(0)
            linhas = arquivo_pontuacao.readlines()
            if len(linhas) >= 1:
                pontuacao_player_um = int(linhas[0].strip())
            if len(linhas) >= 2:
                pontuacao_player_dois = int(linhas[1].strip())
    except FileNotFoundError:
        pontuacao_player_um = 0
        pontuacao_player_dois = 0

    #Reinicia a pontuacao ao apertar 'R'
    if WConio2.kbhit():
        value, symbol = WConio2.getch()

        if symbol in 'rR':
            pontuacao_player_um = 0
            pontuacao_player_dois = 0
                
    if menu.player_perdeu == 1:
        pontuacao_player_dois += 1
        menu.player_perdeu = 0
    elif menu.player_perdeu == 2:
        pontuacao_player_um += 1
        menu.player_perdeu = 0
        
    with open("pontuacoes.txt", "w") as arquivo_saida:
        arquivo_saida.write(f"{pontuacao_player_um}\n")
        arquivo_saida.write(f"{pontuacao_player_dois}\n")


def desenhar_pontuacoes(matriz):
    calcular_pontuacoes()

    pontuacao_texto = [
        list(f"JOGADOR AZUL: {pontuacao_player_um}"),
        list(f"JOGADOR VERMELHO: {pontuacao_player_dois}")
    ]
    for i, linha in enumerate(pontuacao_texto):
        for y, caracter in enumerate(linha):
            if i == 0:
                pontuacao_texto[i][y] = f"\033[36m{caracter}\033[0m"
            if i == 1:
                pontuacao_texto[i][y] = f"\033[91m{caracter}\033[0m"


    for i, linha in enumerate(pontuacao_texto):
        for j, caractere in enumerate(linha):
            if i == 0:
                matriz[25 + i][10 + j] = caractere
            if i == 1:
                matriz[24 + i][67 + j] = caractere


