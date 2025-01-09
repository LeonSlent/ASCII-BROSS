import os
import WConio2
import cursor

import matrizes
from matrizes import vazio, matriz_y, matriz_x, matriz
import menu
import player
import bomba
import mapa

dimensao_jogo = len(player.player_baixo)

def gameplay(angulo_player, ativar_bomba, existe_bomba):
    while True:
        bomba.relogio_bomba += 0.5
        # posicionando cursor da tela sempre no mesmo lugar
        WConio2.gotoxy(0, 0)

        matrizes.limpar_tela(matriz_y, matriz_x, vazio, matriz)

        mapa.desenhar_mapa(matriz)

        #estrutura de condição para decidir qual angulo do player deve ser desenhado na tela
        if angulo_player == "baixo":
            player.desenhar_player(matriz, player.player_baixo)
        elif angulo_player == "cima":
            player.desenhar_player(matriz, player.player_cima)
        elif angulo_player == "esquerda":
            player.desenhar_player(matriz, player.player_esquerda)
        elif angulo_player == "direita":
            player.desenhar_player(matriz, player.player_direita)

        #estrutura para colocar a bomba para o lado que o player esta direcionado
        if ativar_bomba == True:
            if existe_bomba == False:
                bomba.bomba_y = player.player_y
                bomba.bomba_x = player.player_x

                if angulo_player == "esquerda":
                    bomba.bomba_x -= dimensao_jogo
                elif angulo_player == "direita":
                    bomba.bomba_x += dimensao_jogo
                elif angulo_player == "cima":
                    bomba.bomba_y -= dimensao_jogo
                elif angulo_player == "baixo":
                    bomba.bomba_y += dimensao_jogo

                existe_bomba = True

            if bomba.relogio_bomba > 500:
                existe_bomba = False
                ativar_bomba = False
                bomba.relogio_bomba = 0
            bomba.desenhar_bomba(matriz, bomba.bomba_y, bomba.bomba_x)
            

        matrizes.desenhar_tela(matriz_y, matriz_x, matriz)

        if WConio2.kbhit():
            value, symbol = WConio2.getch()

            #movimenta e muda de angulo o player
            if symbol in 'aA' and player.verificar_colisao(matriz, player.player_y, player.player_x - 1, "esquerda"):
                player.player_x -= 1
                angulo_player = "esquerda"
            elif symbol in 'dD' and player.verificar_colisao(matriz, player.player_y, player.player_x + 1, "direita"):
                player.player_x += 1
                angulo_player = "direita"
            elif symbol in 'wW' and player.verificar_colisao(matriz, player.player_y - 1, player.player_x, "cima"):
                player.player_y -= 1
                angulo_player = "cima"
            elif symbol in 'sS' and player.verificar_colisao(matriz, player.player_y + 1, player.player_x, "baixo"):
                player.player_y += 1
                angulo_player = "baixo"

            #player coloca a bomba no mapa
            elif symbol in 'fF':
                if angulo_player == "esquerda" and bomba.verificar_colisao(player.player_y, player.player_x - 5):
                    ativar_bomba = True
                elif angulo_player == "direita" and bomba.verificar_colisao(player.player_y, player.player_x + 5):
                    ativar_bomba = True
                elif angulo_player == "cima" and bomba.verificar_colisao(player.player_y - 5, player.player_x):
                    ativar_bomba = True
                elif angulo_player == "baixo" and bomba.verificar_colisao(player.player_y + 5, player.player_x):
                    ativar_bomba = True

            elif symbol in 'lL':
                break






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
                #menu.transicao_tela(menu.contador, menu.relogio)
                gameplay(player.angulo_player, bomba.ativar_bomba, bomba.existe_bomba)
                

            elif symbol in 'xX':
                pass
            elif symbol in 'Cc':
                exit()