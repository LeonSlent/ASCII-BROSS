import os
import WConio2
import cursor
import matrizes
from bomba import bomba_x_um, bomba_y_um
from matrizes import vazio, matriz_y, matriz_x, matriz
import menu
import player
import bomba
import mapa
import pygame
import time

from player import player_y_um

pygame.init()
pygame.mixer.init()

pasta_atual = os.path.dirname(os.path.abspath(__file__))

pygame.mixer.music.load(os.path.join(pasta_atual, "Sons", "Fundo.wav"))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

explosion_sound = pygame.mixer.Sound(os.path.join(pasta_atual, "Sons", "Bomba.wav"))
explosion_sound.set_volume(0.7)

tecla_sound = pygame.mixer.Sound(os.path.join(pasta_atual, "Sons", "Tecla.mp3"))
tecla_sound.set_volume(0.7)


dimensao_jogo = len(player.player_baixo)





def gameplay(angulo_player_um, ativar_bomba_um, existe_bomba_um, angulo_player_dois, ativar_bomba_dois, existe_bomba_dois):
    tempo_ativação_bomba_um = None
    tempo_ativação_bomba_dois = None
    tempo_duracao_bomba = 3
    tempo_explosão_bomba = 0.1
    while True:

        # posicionando cursor da tela sempre no mesmo lugar
        WConio2.gotoxy(0, 0)

        matrizes.limpar_tela(matriz_y, matriz_x, vazio, matriz)

        mapa.desenhar_mapa(matriz, mapa.copia_cenario)

        if player.player_vivo_um == False and bomba.relogio_bomba_um == 0 and bomba.relogio_bomba_dois == 0 or player.player_vivo_dois == False and bomba.relogio_bomba_um == 0 and bomba.relogio_bomba_dois == 0:
            menu.menu_fim(0)
            player.player_vivo_um = True
            player.player_vivo_dois = True
            player.player_y_um = 0
            player.player_x_um = 0
            player.player_y_dois = 30
            player.player_x_dois = 90
            break



        if player.player_vivo_um == True:
            #estrutura de condição para decidir qual angulo do player deve ser desenhado na tela
            if angulo_player_um == "baixo":
                player.desenhar_player(matriz, player.player_baixo_um, player.player_y_um, player.player_x_um)
            elif angulo_player_um == "cima":
                player.desenhar_player(matriz, player.player_cima_um, player.player_y_um, player.player_x_um)
            elif angulo_player_um == "esquerda":
                player.desenhar_player(matriz, player.player_esquerda_um, player.player_y_um, player.player_x_um)
            elif angulo_player_um == "direita":
                player.desenhar_player(matriz, player.player_direita_um, player.player_y_um, player.player_x_um)

        if player.player_vivo_dois == True:
            #estrutura de condição para decidir qual angulo do player deve ser desenhado na tela
            if angulo_player_dois == "baixo":
                player.desenhar_player(matriz, player.player_baixo_dois, player.player_y_dois, player.player_x_dois)
            elif angulo_player_dois == "cima":
                player.desenhar_player(matriz, player.player_cima_dois, player.player_y_dois, player.player_x_dois)
            elif angulo_player_dois == "esquerda":
                player.desenhar_player(matriz, player.player_esquerda_dois, player.player_y_dois, player.player_x_dois)
            elif angulo_player_dois == "direita":
                player.desenhar_player(matriz, player.player_direita_dois, player.player_y_dois, player.player_x_dois)


        #estrutura para colocar a bomba para o lado que o player esta direcionado
        
        if ativar_bomba_um:

            if tempo_ativação_bomba_um is None:
                tempo_ativação_bomba_um = time.time()

                bomba.relogio_bomba_um += 1

            if not existe_bomba_um:
                # Configurar a posição inicial da bomba
                bomba.bomba_y_um = player.player_y_um
                bomba.bomba_x_um = player.player_x_um
                existe_bomba_um = True

                # Ajustar a posição com base no ângulo do jogador
                if angulo_player_um == "esquerda":
                    bomba.bomba_x_um -= dimensao_jogo
                elif angulo_player_um == "direita":
                    bomba.bomba_x_um += dimensao_jogo
                elif angulo_player_um == "cima":
                    bomba.bomba_y_um -= dimensao_jogo
                elif angulo_player_um == "baixo":
                    bomba.bomba_y_um += dimensao_jogo

            # Calcular o tempo decorrido
            tempo_decorrido = time.time() - tempo_ativação_bomba_um

            # Lógica para desenhar e explodir a bomba
            if existe_bomba_um and tempo_decorrido < tempo_duracao_bomba:
                bomba.desenhar_bomba(matriz, bomba.bomba_y_um, bomba.bomba_x_um)
            elif existe_bomba_um and tempo_decorrido < tempo_duracao_bomba + tempo_explosão_bomba:
                bomba.desenhar_explosao(matriz, bomba.bomba_y_um, bomba.bomba_x_um)
                explosion_sound.play()
            elif existe_bomba_um and tempo_decorrido >= tempo_duracao_bomba + tempo_explosão_bomba:
                # Resetar o estado após a explosão
                existe_bomba_um = False
                ativar_bomba_um = False
                bomba.relogio_bomba_um = 0
                tempo_ativação_bomba_um = None  # Indicar que a bomba não está ativa

        # estrutura para colocar a bomba para o lado que o player está direcionado

        if ativar_bomba_dois:

            if tempo_ativação_bomba_dois is None:
                tempo_ativação_bomba_dois = time.time()

                bomba.relogio_bomba_dois += 1

            if not existe_bomba_dois:
                # Configurar a posição inicial da bomba
                bomba.bomba_y_dois = player.player_y_dois
                bomba.bomba_x_dois = player.player_x_dois
                existe_bomba_dois = True

                # Ajustar a posição com base no ângulo do jogador
                if angulo_player_dois == "esquerda":
                    bomba.bomba_x_dois -= dimensao_jogo
                elif angulo_player_dois == "direita":
                    bomba.bomba_x_dois += dimensao_jogo
                elif angulo_player_dois == "cima":
                    bomba.bomba_y_dois -= dimensao_jogo
                elif angulo_player_dois == "baixo":
                    bomba.bomba_y_dois += dimensao_jogo

            # Calcular o tempo decorrido
            tempo_decorrido = time.time() - tempo_ativação_bomba_dois

            # Lógica para desenhar e explodir a bomba
            if existe_bomba_dois and tempo_decorrido < tempo_duracao_bomba:
                bomba.desenhar_bomba(matriz, bomba.bomba_y_dois, bomba.bomba_x_dois)
            elif (existe_bomba_dois and tempo_decorrido < tempo_duracao_bomba + tempo_explosão_bomba):
                bomba.desenhar_explosao(matriz, bomba.bomba_y_dois, bomba.bomba_x_dois)
                explosion_sound.play()
            elif existe_bomba_dois and tempo_decorrido >= tempo_duracao_bomba + tempo_explosão_bomba:
                # Resetar o estado após a explosão
                existe_bomba_dois = False
                ativar_bomba_dois = False
                bomba.relogio_bomba_dois = 0
                tempo_ativação_bomba_dois = None
            
            

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


            #movimenta e muda de angulo o player
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


def gameplay_advanced(angulo_player_um, ativar_bomba_um, existe_bomba_um, angulo_player_dois, ativar_bomba_dois, existe_bomba_dois):
    tempo_ativação_bomba_um = None
    tempo_ativação_bomba_dois = None
    tempo_duracao_bomba = 2
    tempo_explosão_bomba = 0.1

    while True:

        # posicionando cursor da tela sempre no mesmo lugar
        WConio2.gotoxy(0, 0)

        matrizes.limpar_tela(matriz_y, matriz_x, vazio, matriz)

        mapa.desenhar_mapa(matriz, mapa.copia_cenario)

        if player.player_vivo_um == False and bomba.relogio_bomba_um == 0 and bomba.relogio_bomba_dois == 0 or player.player_vivo_dois == False and bomba.relogio_bomba_um == 0 and bomba.relogio_bomba_dois == 0:
            menu.menu_fim(0)
            player.player_vivo_um = True
            player.player_vivo_dois = True
            player.player_y_um = 0
            player.player_x_um = 0
            player.player_y_dois = 30
            player.player_x_dois = 90
            break

        if player.player_vivo_um == True:
            # estrutura de condição para decidir qual angulo do player deve ser desenhado na tela
            if angulo_player_um == "baixo":
                player.desenhar_player(matriz, player.player_baixo_um, player.player_y_um, player.player_x_um)
            elif angulo_player_um == "cima":
                player.desenhar_player(matriz, player.player_cima_um, player.player_y_um, player.player_x_um)
            elif angulo_player_um == "esquerda":
                player.desenhar_player(matriz, player.player_esquerda_um, player.player_y_um, player.player_x_um)
            elif angulo_player_um == "direita":
                player.desenhar_player(matriz, player.player_direita_um, player.player_y_um, player.player_x_um)

        if player.player_vivo_dois == True:
            # estrutura de condição para decidir qual angulo do player deve ser desenhado na tela
            if angulo_player_dois == "baixo":
                player.desenhar_player(matriz, player.player_baixo_dois, player.player_y_dois, player.player_x_dois)
            elif angulo_player_dois == "cima":
                player.desenhar_player(matriz, player.player_cima_dois, player.player_y_dois, player.player_x_dois)
            elif angulo_player_dois == "esquerda":
                player.desenhar_player(matriz, player.player_esquerda_dois, player.player_y_dois, player.player_x_dois)
            elif angulo_player_dois == "direita":
                player.desenhar_player(matriz, player.player_direita_dois, player.player_y_dois, player.player_x_dois)

        # estrutura para colocar a bomba para o lado que o player esta direcionad



        if ativar_bomba_um:

            if tempo_ativação_bomba_um is None:
                tempo_ativação_bomba_um = time.time()

            bomba.relogio_bomba_um += 1

            if not existe_bomba_um:
                # Configurar a posição inicial da bomba
                bomba.bomba_y_um = player.player_y_um
                bomba.bomba_x_um = player.player_x_um
                existe_bomba_um = True

                # Ajustar a posição com base no ângulo do jogador
                if angulo_player_um == "esquerda":
                    bomba.bomba_x_um -= dimensao_jogo
                elif angulo_player_um == "direita":
                    bomba.bomba_x_um += dimensao_jogo
                elif angulo_player_um == "cima":
                    bomba.bomba_y_um -= dimensao_jogo
                elif angulo_player_um == "baixo":
                    bomba.bomba_y_um += dimensao_jogo

            # Calcular o tempo decorrido
            tempo_decorrido = time.time() - tempo_ativação_bomba_um

            # Desenhar e explodir a bomba
            if existe_bomba_um and tempo_decorrido < tempo_duracao_bomba:
                bomba.desenhar_bomba(matriz, bomba.bomba_y_um, bomba.bomba_x_um)
            elif existe_bomba_um and tempo_decorrido < tempo_duracao_bomba + tempo_explosão_bomba:
                bomba.desenhar_explosao(matriz, bomba.bomba_y_um, bomba.bomba_x_um)
                explosion_sound.play()
            elif existe_bomba_um and tempo_decorrido >= tempo_duracao_bomba + tempo_explosão_bomba:
                # Resetar o estado após a explosão
                existe_bomba_um = False
                ativar_bomba_um = False
                bomba.relogio_bomba_um = 0
                tempo_ativação_bomba_um = None

        # estrutura para colocar a bomba para o lado que o player está direcionado

        if ativar_bomba_dois:

            if tempo_ativação_bomba_dois is None:
                tempo_ativação_bomba_dois = time.time()

                bomba.relogio_bomba_um += 1

            if not existe_bomba_dois:
                # Configurar a posição inicial da bomba
                bomba.bomba_y_dois = player.player_y_dois
                bomba.bomba_x_dois = player.player_x_dois
                existe_bomba_dois = True

                # Ajustar a posição com base no ângulo do jogador
                if angulo_player_dois == "esquerda":
                    bomba.bomba_x_dois -= dimensao_jogo
                elif angulo_player_dois == "direita":
                    bomba.bomba_x_dois += dimensao_jogo
                elif angulo_player_dois == "cima":
                    bomba.bomba_y_dois -= dimensao_jogo
                elif angulo_player_dois == "baixo":
                    bomba.bomba_y_dois += dimensao_jogo

            # Calcular o tempo decorrido
            tempo_decorrido = time.time() - tempo_ativação_bomba_dois

            # Lógica para desenhar e explodir a bomba
            if existe_bomba_dois and tempo_decorrido < tempo_duracao_bomba:
                bomba.desenhar_bomba(matriz, bomba.bomba_y_dois, bomba.bomba_x_dois)
            elif (existe_bomba_dois and tempo_decorrido < tempo_duracao_bomba + tempo_explosão_bomba):
                bomba.desenhar_explosao(matriz, bomba.bomba_y_dois, bomba.bomba_x_dois)
                explosion_sound.play()
            elif existe_bomba_dois and tempo_decorrido >= tempo_duracao_bomba + tempo_explosão_bomba:
                # Resetar o estado após a explosão
                existe_bomba_dois = False
                ativar_bomba_dois = False
                bomba.relogio_bomba_dois = 0
                tempo_ativação_bomba_dois = None  # Indicar que a bomba não está ativa

        matrizes.desenhar_tela(matriz_y, matriz_x, matriz)

        if WConio2.kbhit():
            value, symbol = WConio2.getch()

            # movimenta e muda de angulo o player
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

            # player coloca a bomba no mapa
            elif symbol in 'fF':
                if angulo_player_um == "esquerda" and bomba.verificar_colisao(matriz, player.player_y_um, player.player_x_um - dimensao_jogo):
                    ativar_bomba_um = True
                elif angulo_player_um == "direita" and bomba.verificar_colisao(matriz, player.player_y_um, player.player_x_um + dimensao_jogo):
                    ativar_bomba_um = True
                elif angulo_player_um == "cima" and bomba.verificar_colisao(matriz, player.player_y_um - dimensao_jogo, player.player_x_um):
                    ativar_bomba_um = True
                elif angulo_player_um == "baixo" and bomba.verificar_colisao(matriz, player.player_y_um + dimensao_jogo, player.player_x_um):
                    ativar_bomba_um = True

            # movimenta e muda de angulo o player
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
                tecla_sound.play()
                mapa.copia_cenario = [linha[:] for linha in mapa.cenario]

                menu.transicao_tela(menu.contador, menu.relogio)
                gameplay(player.angulo_player_um, bomba.ativar_bomba_um, bomba.existe_bomba_um, player.angulo_player_dois, bomba.ativar_bomba_dois, bomba.existe_bomba_dois)

            elif symbol in 'aA':
                tecla_sound.play()
                mapa.copia_cenario = [linha[:] for linha in mapa.cenario]

                menu.transicao_tela(menu.contador, menu.relogio)
                gameplay_advanced(player.angulo_player_um, bomba.ativar_bomba_um, bomba.existe_bomba_um, player.angulo_player_dois, bomba.ativar_bomba_dois, bomba.existe_bomba_dois)

            elif symbol in 'pP':
                tecla_sound.play()
                menu_pontuacao()


            elif symbol in 'Cc':
                tecla_sound.play()
                exit()
