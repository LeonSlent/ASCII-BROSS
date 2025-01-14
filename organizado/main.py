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

def gameplay(angulo_player_um, ativar_bomba_um, existe_bomba_um, angulo_player_dois, ativar_bomba_dois, existe_bomba_dois):
    while True:
        
        # posicionando cursor da tela sempre no mesmo lugar
        WConio2.gotoxy(0, 0)

        matrizes.limpar_tela(matriz_y, matriz_x, vazio, matriz)

        mapa.desenhar_mapa(matriz)

        if player.player_vivo_um == True:
            #estrutura de condição para decidir qual angulo do player deve ser desenhado na tela
            if angulo_player_um == "baixo":
                player.desenhar_player(matriz, player.player_baixo, player.player_y_um, player.player_x_um)
            elif angulo_player_um == "cima":
                player.desenhar_player(matriz, player.player_cima, player.player_y_um, player.player_x_um)
            elif angulo_player_um == "esquerda":
                player.desenhar_player(matriz, player.player_esquerda, player.player_y_um, player.player_x_um)
            elif angulo_player_um == "direita":
                player.desenhar_player(matriz, player.player_direita, player.player_y_um, player.player_x_um)

        #estrutura para colocar a bomba para o lado que o player esta direcionado
        
        if ativar_bomba_um == True:
            bomba.relogio_bomba_um += 1
            if existe_bomba_um == False:
                bomba.bomba_y_um = player.player_y_um
                bomba.bomba_x_um = player.player_x_um
                existe_bomba_um = True

                if angulo_player_um == "esquerda":
                    bomba.bomba_x_um -= dimensao_jogo
                elif angulo_player_um == "direita":
                    bomba.bomba_x_um += dimensao_jogo
                elif angulo_player_um == "cima":
                    bomba.bomba_y_um -= dimensao_jogo
                elif angulo_player_um == "baixo":
                    bomba.bomba_y_um += dimensao_jogo

            if existe_bomba_um == True and bomba.relogio_bomba_um < 500:
                bomba.desenhar_bomba(matriz, bomba.bomba_y_um, bomba.bomba_x_um)

            elif existe_bomba_um == True and bomba.relogio_bomba_um < 1000:
                bomba.desenhar_explosao(matriz, bomba.bomba_y_um, bomba.bomba_x_um, 1)
                
            elif existe_bomba_um == True and bomba.relogio_bomba_um == 1000:
                    existe_bomba_um = False
                    ativar_bomba_um = False
                    bomba.relogio_bomba_um = 0


        if player.player_vivo_dois == True:
            #estrutura de condição para decidir qual angulo do player deve ser desenhado na tela
            if angulo_player_dois == "baixo":
                player.desenhar_player(matriz, player.player_baixo, player.player_y_dois, player.player_x_dois)
            elif angulo_player_dois == "cima":
                player.desenhar_player(matriz, player.player_cima, player.player_y_dois, player.player_x_dois)
            elif angulo_player_dois == "esquerda":
                player.desenhar_player(matriz, player.player_esquerda, player.player_y_dois, player.player_x_dois)
            elif angulo_player_dois == "direita":
                player.desenhar_player(matriz, player.player_direita, player.player_y_dois, player.player_x_dois)

        #estrutura para colocar a bomba para o lado que o player está direcionado

        if ativar_bomba_dois == True:
            bomba.relogio_bomba_dois += 1
            if existe_bomba_dois == False:
                bomba.bomba_y_dois = player.player_y_dois
                bomba.bomba_x_dois = player.player_x_dois
                existe_bomba_dois = True

                if angulo_player_dois == "esquerda":
                    bomba.bomba_x_dois -= dimensao_jogo
                elif angulo_player_dois == "direita":
                    bomba.bomba_x_dois += dimensao_jogo
                elif angulo_player_dois == "cima":
                    bomba.bomba_y_dois -= dimensao_jogo
                elif angulo_player_dois == "baixo":
                    bomba.bomba_y_dois += dimensao_jogo

            if existe_bomba_dois == True and bomba.relogio_bomba_dois < 500:
                bomba.desenhar_bomba(matriz, bomba.bomba_y_dois, bomba.bomba_x_dois)

            elif existe_bomba_dois == True and bomba.relogio_bomba_dois < 1000:
                bomba.desenhar_explosao(matriz, bomba.bomba_y_dois, bomba.bomba_x_dois, 2)

            elif existe_bomba_dois == True and bomba.relogio_bomba_dois == 1000:
                existe_bomba_dois = False
                ativar_bomba_dois = False
                bomba.relogio_bomba_dois = 0
            
            

        matrizes.desenhar_tela(matriz_y, matriz_x, matriz)

        if WConio2.kbhit():
            value, symbol = WConio2.getch()

            #movimenta e muda de angulo o player
            if symbol in 'aA' and player.verificar_colisao(matriz, player.player_y_um, player.player_x_um - 1, "esquerda"):
                player.player_x_um -= 1
                angulo_player_um = "esquerda"
            elif symbol in 'dD' and player.verificar_colisao(matriz, player.player_y_um, player.player_x_um + 1, "direita"):
                player.player_x_um += 1
                angulo_player_um = "direita"
            elif symbol in 'wW' and player.verificar_colisao(matriz, player.player_y_um - 1, player.player_x_um, "cima"):
                player.player_y_um -= 1
                angulo_player_um = "cima"
            elif symbol in 'sS' and player.verificar_colisao(matriz, player.player_y_um + 1, player.player_x_um, "baixo"):
                player.player_y_um += 1
                angulo_player_um = "baixo"

            #player coloca a bomba no mapa
            elif symbol in 'fF':
                if angulo_player_um == "esquerda" and bomba.verificar_colisao(matriz, player.player_y_um, player.player_x_um - dimensao_jogo):
                    ativar_bomba_um = True
                elif angulo_player_um == "direita" and bomba.verificar_colisao(matriz, player.player_y_um, player.player_x_um + dimensao_jogo):
                    ativar_bomba_um = True
                elif angulo_player_um == "cima" and bomba.verificar_colisao(matriz, player.player_y_um - dimensao_jogo, player.player_x_um):
                    ativar_bomba_um = True
                elif angulo_player_um == "baixo" and bomba.verificar_colisao(matriz, player.player_y_um + dimensao_jogo, player.player_x_um):
                    ativar_bomba_um = True

            elif symbol in 'lL':
                break

            if symbol in '4' and player.verificar_colisao(matriz, player.player_y_dois, player.player_x_dois - 1, "esquerda"):
                player.player_x_dois -= 1
                angulo_player_dois = "esquerda"
            elif symbol in '6' and player.verificar_colisao(matriz, player.player_y_dois, player.player_x_dois + 1, "direita"):
                player.player_x_dois += 1
                angulo_player_dois = "direita"
            elif symbol in '8' and player.verificar_colisao(matriz, player.player_y_dois - 1, player.player_x_dois, "cima"):
                player.player_y_dois -= 1
                angulo_player_dois = "cima"
            elif symbol in '5' and player.verificar_colisao(matriz, player.player_y_dois + 1, player.player_x_dois, "baixo"):
                player.player_y_dois += 1
                angulo_player_dois = "baixo"

            # Player coloca a bomba no mapa
            elif symbol in 'mM':
                if angulo_player_dois == "esquerda" and bomba.verificar_colisao(matriz, player.player_y_dois, player.player_x_dois - dimensao_jogo):
                    ativar_bomba_dois = True
                elif angulo_player_dois == "direita" and bomba.verificar_colisao(matriz, player.player_y_dois, player.player_x_dois + dimensao_jogo):
                    ativar_bomba_dois = True
                elif angulo_player_dois == "cima" and bomba.verificar_colisao(matriz, player.player_y_dois - dimensao_jogo, player.player_x_dois):
                    ativar_bomba_dois = True
                elif angulo_player_dois == "baixo" and bomba.verificar_colisao(matriz, player.player_y_dois + dimensao_jogo, player.player_x_dois):
                    ativar_bomba_dois = True

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
                gameplay(player.angulo_player_um, bomba.ativar_bomba_um, bomba.existe_bomba_um, player.angulo_player_dois, bomba.ativar_bomba_dois, bomba.existe_bomba_dois)
                

            elif symbol in 'xX':
                pass
            elif symbol in 'Cc':
                exit()