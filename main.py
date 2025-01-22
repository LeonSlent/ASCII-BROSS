import os
import WConio2
import cursor
import matrizes
from matrizes import vazio, matriz_y, matriz_x, matriz
import menu
import player
import bomba
import mapa
import pygame
import game

def menu_pontuacao():
    while True:
        WConio2.gotoxy(0, 0)
        matrizes.limpar_tela(matriz_y, matriz_x, vazio, matriz)
        menu.desenhar_PONTUACAO(matriz_x, matriz)
        player.desenhar_pontuacoes(matriz_x, matriz)
        matrizes.desenhar_tela(matriz_y, matriz_x, matriz)


        if WConio2.kbhit():
            value, symbol = WConio2.getch()
            if symbol in 'pP':
                return

if __name__ == '__main__':
    os.system('cls')
    cursor.hide()

    matrizes.iniciar_matriz(matriz_y, matriz_x, vazio, matriz)

    while (True):


        # posicionando cursor da tela sempre no mesmo lugar
        WConio2.gotoxy(0, 0)

        # limpando a matriz antes de desenhar nela
        matrizes.limpar_tela(matriz_y, matriz_x, vazio, matriz)

        menu.desenhar_logo(matriz_x, matriz, menu.logo)
        menu.desenhar_opcoes(matriz_x, matriz)

        # impressão da tela
        matrizes.desenhar_tela(matriz_y, matriz_x, matriz)
        
        if WConio2.kbhit():
            value, symbol = WConio2.getch()

            if symbol in 'zZ':
                menu.tecla_sound.play()
                mapa.copia_cenario = [linha[:] for linha in mapa.cenario]

                menu.transicao_tela(menu.contador, menu.relogio)
                game.gameplay(player.angulo_player_um, bomba.ativar_bomba_um, bomba.existe_bomba_um, player.angulo_player_dois, bomba.ativar_bomba_dois, bomba.existe_bomba_dois)

            elif symbol in 'aA':
                menu.tecla_sound.play()
                mapa.copia_cenario = [linha[:] for linha in mapa.cenario]

                menu.transicao_tela(menu.contador, menu.relogio)
                game.gameplay_advanced(player.angulo_player_um, bomba.ativar_bomba_um, bomba.existe_bomba_um, player.angulo_player_dois, bomba.ativar_bomba_dois, bomba.existe_bomba_dois)

            elif symbol in 'pP':
                menu.tecla_sound.play()
                menu_pontuacao()


            elif symbol in 'Cc':
                menu.tecla_sound.play()
                exit()
