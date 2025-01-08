import os
import WConio2
import cursor

import matrizes
from matrizes import vazio, matriz_y, matriz_x, matriz
import menu
import player
import bomba

def gameplay(angulo_player, ativar_bomba):
    while True:
        # posicionando cursor da tela sempre no mesmo lugar
        WConio2.gotoxy(0, 0)

        matrizes.limpar_tela(matriz_y, matriz_x, vazio, matriz)

        #estrutura de condição para decidir qual angulo do player deve ser desenhado na tela
        if angulo_player == "baixo":
            player.desenhar_player(matriz, player.player_baixo)
        elif angulo_player == "cima":
            player.desenhar_player(matriz, player.player_cima)
        elif angulo_player == "esquerda":
            player.desenhar_player(matriz, player.player_esquerda)
        elif angulo_player == "direita":
            player.desenhar_player(matriz, player.player_direita)

        if ativar_bomba == True:
            bomba.desenhar_bomba(matriz)

        matrizes.desenhar_tela(matriz_y, matriz_x, matriz)

        if WConio2.kbhit():
            value, symbol = WConio2.getch()

            if symbol in 'aA' and player.verificar_colisao(player.player_y, player.player_x - 1):
                player.player_x -= 1
                angulo_player = "esquerda"
            elif symbol in 'dD' and player.verificar_colisao(player.player_y, player.player_x + 1):
                player.player_x += 1
                angulo_player = "direita"
            elif symbol in 'wW' and player.verificar_colisao(player.player_y - 1, player.player_x):
                player.player_y -= 1
                angulo_player = "cima"
            elif symbol in 'sS' and player.verificar_colisao(player.player_y + 1, player.player_x):
                player.player_y += 1
                angulo_player = "baixo"
            elif symbol in 'fF':
                ativar_bomba = True






if __name__ == '__main__':
    os.system('cls')
    cursor.hide()

    matrizes.iniciar_matriz(matriz_y, matriz_x, vazio, matriz)

    while (True):

        # posicionando cursor da tela sempre no mesmo lugar
        WConio2.gotoxy(0, 0)

        # limpando a matriz antes de desenhar nela
        matrizes.limpar_tela(matriz_y, matriz_x, vazio, matriz)

        menu.desenhar_logo(matriz_x, matriz)
        menu.desenhar_opcoes(matriz_x, matriz)

        # impressão da tela
        matrizes.desenhar_tela(matriz_y, matriz_x, matriz)
        
        if WConio2.kbhit():
            value, symbol = WConio2.getch()

            if symbol in 'zZ':
                menu.transicao_tela(menu.contador, menu.relogio)
                gameplay(player.angulo_player, bomba.ativar_bomba)
                

            elif symbol in 'xX':
                pass
            elif symbol in 'Cc':
                exit()