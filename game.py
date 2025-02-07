import WConio2
import matrizes
import menu
import player
import bomba
import mapa
import pygame
import time
pygame.init()
pygame.mixer.init()

dimensao_jogo = len(player.player_baixo)


def gameplay(angulo_player_um, ativar_bomba_um, existe_bomba_um, angulo_player_dois, ativar_bomba_dois, existe_bomba_dois):
    while True:

        # posicionando cursor da tela sempre no mesmo lugar
        WConio2.gotoxy(0, 0)

        matrizes.limpar_tela(matrizes.matriz_y, matrizes.matriz_x, matrizes.vazio, matrizes.matriz)

        mapa.desenhar_mapa(matrizes.matriz, mapa.copia_cenario)

        if player.player_vivo_um == False and bomba.tempo_ativação_bomba_um == None and bomba.tempo_ativação_bomba_dois == None or player.player_vivo_dois == False and bomba.tempo_ativação_bomba_um == None and bomba.tempo_ativação_bomba_dois == None:
            player.calcular_pontuacoes()
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
                player.desenhar_player(matrizes.matriz, player.player_baixo_um, player.player_y_um, player.player_x_um)
            elif angulo_player_um == "cima":
                player.desenhar_player(matrizes.matriz, player.player_cima_um, player.player_y_um, player.player_x_um)
            elif angulo_player_um == "esquerda":
                player.desenhar_player(matrizes.matriz, player.player_esquerda_um, player.player_y_um, player.player_x_um)
            elif angulo_player_um == "direita":
                player.desenhar_player(matrizes.matriz, player.player_direita_um, player.player_y_um, player.player_x_um)

        if player.player_vivo_dois == True:
            # estrutura de condição para decidir qual angulo do player deve ser desenhado na tela
            if angulo_player_dois == "baixo":
                player.desenhar_player(matrizes.matriz, player.player_baixo_dois, player.player_y_dois, player.player_x_dois)
            elif angulo_player_dois == "cima":
                player.desenhar_player(matrizes.matriz, player.player_cima_dois, player.player_y_dois, player.player_x_dois)
            elif angulo_player_dois == "esquerda":
                player.desenhar_player(matrizes.matriz, player.player_esquerda_dois, player.player_y_dois, player.player_x_dois)
            elif angulo_player_dois == "direita":
                player.desenhar_player(matrizes.matriz, player.player_direita_dois, player.player_y_dois, player.player_x_dois)

        # estrutura para colocar a bomba para o lado que o player esta direcionado

        if ativar_bomba_um:

            if bomba.tempo_ativação_bomba_um is None:
                bomba.tempo_ativação_bomba_um = time.time()


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
            tempo_decorrido = time.time() - bomba.tempo_ativação_bomba_um

            # Lógica para desenhar e explodir a bomba
            if existe_bomba_um and tempo_decorrido < bomba.tempo_duracao_bomba:
                bomba.desenhar_bomba(matrizes.matriz, bomba.bomba_y_um, bomba.bomba_x_um)
            elif existe_bomba_um and tempo_decorrido < bomba.tempo_duracao_bomba + bomba.tempo_explosão_bomba:
                bomba.desenhar_explosao(matrizes.matriz, bomba.bomba_y_um, bomba.bomba_x_um)
                menu.explosion_sound.play()
            elif existe_bomba_um and tempo_decorrido >= bomba.tempo_duracao_bomba + bomba.tempo_explosão_bomba:
                # Resetar o estado após a explosão
                existe_bomba_um = False
                ativar_bomba_um = False
                bomba.tempo_ativação_bomba_um = None  # Indicar que a bomba não está ativa

        # estrutura para colocar a bomba para o lado que o player está direcionado

        if ativar_bomba_dois:

            if bomba.tempo_ativação_bomba_dois is None:
                bomba.tempo_ativação_bomba_dois = time.time()


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
            tempo_decorrido = time.time() - bomba.tempo_ativação_bomba_dois

            # Lógica para desenhar e explodir a bomba
            if existe_bomba_dois and tempo_decorrido < bomba.tempo_duracao_bomba:
                bomba.desenhar_bomba(matrizes.matriz, bomba.bomba_y_dois, bomba.bomba_x_dois)
            elif (existe_bomba_dois and tempo_decorrido < bomba.tempo_duracao_bomba + bomba.tempo_explosão_bomba):
                bomba.desenhar_explosao(matrizes.matriz, bomba.bomba_y_dois, bomba.bomba_x_dois)
                menu.explosion_sound.play()
            elif existe_bomba_dois and tempo_decorrido >= bomba.tempo_duracao_bomba + bomba.tempo_explosão_bomba:
                # Resetar o estado após a explosão
                existe_bomba_dois = False
                ativar_bomba_dois = False
                bomba.tempo_ativação_bomba_dois = None

        matrizes.desenhar_tela(matrizes.matriz_y, matrizes.matriz_x, matrizes.matriz)

        if WConio2.kbhit():
            value, symbol = WConio2.getch()

            # movimenta e muda de angulo o player
            if symbol in 'aA' and player.verificar_colisao(matrizes.matriz, player.player_y_um, player.player_x_um - 1, "esquerda"):
                player.player_x_um -= 1
                angulo_player_um = "esquerda"
            elif symbol in 'dD' and player.verificar_colisao(matrizes.matriz, player.player_y_um, player.player_x_um + 1, "direita"):
                player.player_x_um += 1
                angulo_player_um = "direita"
            elif symbol in 'wW' and player.verificar_colisao(matrizes.matriz, player.player_y_um - 1, player.player_x_um, "cima"):
                player.player_y_um -= 1
                angulo_player_um = "cima"
            elif symbol in 'sS' and player.verificar_colisao(matrizes.matriz, player.player_y_um + 1, player.player_x_um, "baixo"):
                player.player_y_um += 1
                angulo_player_um = "baixo"

            # player coloca a bomba no mapa
            elif symbol in 'fF':
                if angulo_player_um == "esquerda" and bomba.verificar_colisao(matrizes.matriz, player.player_y_um, player.player_x_um - dimensao_jogo):
                    ativar_bomba_um = True
                elif angulo_player_um == "direita" and bomba.verificar_colisao(matrizes.matriz, player.player_y_um, player.player_x_um + dimensao_jogo):
                    ativar_bomba_um = True
                elif angulo_player_um == "cima" and bomba.verificar_colisao(matrizes.matriz, player.player_y_um - dimensao_jogo, player.player_x_um):
                    ativar_bomba_um = True
                elif angulo_player_um == "baixo" and bomba.verificar_colisao(matrizes.matriz, player.player_y_um + dimensao_jogo, player.player_x_um):
                    ativar_bomba_um = True

            # movimenta e muda de angulo o player
            if symbol in '4' and player.verificar_colisao(matrizes.matriz, player.player_y_dois, player.player_x_dois - 1, "esquerda"):
                player.player_x_dois -= 1
                angulo_player_dois = "esquerda"
            elif symbol in '6' and player.verificar_colisao(matrizes.matriz, player.player_y_dois, player.player_x_dois + 1, "direita"):
                player.player_x_dois += 1
                angulo_player_dois = "direita"
            elif symbol in '8' and player.verificar_colisao(matrizes.matriz, player.player_y_dois - 1, player.player_x_dois, "cima"):
                player.player_y_dois -= 1
                angulo_player_dois = "cima"
            elif symbol in '5' and player.verificar_colisao(matrizes.matriz, player.player_y_dois + 1, player.player_x_dois, "baixo"):
                player.player_y_dois += 1
                angulo_player_dois = "baixo"

            # Player coloca a bomba no mapa
            elif symbol in 'mM':
                if angulo_player_dois == "esquerda" and bomba.verificar_colisao(matrizes.matriz, player.player_y_dois, player.player_x_dois - dimensao_jogo):
                    ativar_bomba_dois = True
                elif angulo_player_dois == "direita" and bomba.verificar_colisao(matrizes.matriz, player.player_y_dois, player.player_x_dois + dimensao_jogo):
                    ativar_bomba_dois = True
                elif angulo_player_dois == "cima" and bomba.verificar_colisao(matrizes.matriz, player.player_y_dois - dimensao_jogo, player.player_x_dois):
                    ativar_bomba_dois = True
                elif angulo_player_dois == "baixo" and bomba.verificar_colisao(matrizes.matriz, player.player_y_dois + dimensao_jogo, player.player_x_dois):
                    ativar_bomba_dois = True


def gameplay_advanced(angulo_player_um, ativar_bomba_um, existe_bomba_um, angulo_player_dois, ativar_bomba_dois, existe_bomba_dois):
    while True:

        # posicionando cursor da tela sempre no mesmo lugar
        WConio2.gotoxy(0, 0)

        matrizes.limpar_tela(matrizes.matriz_y, matrizes.matriz_x, matrizes.vazio, matrizes.matriz)

        mapa.desenhar_mapa(matrizes.matriz, mapa.copia_cenario)

        if player.player_vivo_um == False and bomba.tempo_ativação_bomba_um == None and bomba.tempo_ativação_bomba_dois == None or player.player_vivo_dois == False and bomba.tempo_ativação_bomba_um == None and bomba.tempo_ativação_bomba_dois == None:
            player.calcular_pontuacoes()
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
                player.desenhar_player(matrizes.matriz, player.player_baixo_um, player.player_y_um, player.player_x_um)
            elif angulo_player_um == "cima":
                player.desenhar_player(matrizes.matriz, player.player_cima_um, player.player_y_um, player.player_x_um)
            elif angulo_player_um == "esquerda":
                player.desenhar_player(matrizes.matriz, player.player_esquerda_um, player.player_y_um, player.player_x_um)
            elif angulo_player_um == "direita":
                player.desenhar_player(matrizes.matriz, player.player_direita_um, player.player_y_um, player.player_x_um)

        if player.player_vivo_dois == True:
            # estrutura de condição para decidir qual angulo do player deve ser desenhado na tela
            if angulo_player_dois == "baixo":
                player.desenhar_player(matrizes.matriz, player.player_baixo_dois, player.player_y_dois, player.player_x_dois)
            elif angulo_player_dois == "cima":
                player.desenhar_player(matrizes.matriz, player.player_cima_dois, player.player_y_dois, player.player_x_dois)
            elif angulo_player_dois == "esquerda":
                player.desenhar_player(matrizes.matriz, player.player_esquerda_dois, player.player_y_dois, player.player_x_dois)
            elif angulo_player_dois == "direita":
                player.desenhar_player(matrizes.matriz, player.player_direita_dois, player.player_y_dois, player.player_x_dois)

        # estrutura para colocar a bomba para o lado que o player esta direcionad

        if ativar_bomba_um:

            if bomba.tempo_ativação_bomba_um is None:
                bomba.tempo_ativação_bomba_um = time.time()


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
            tempo_decorrido = time.time() - bomba.tempo_ativação_bomba_um

            # Desenhar e explodir a bomba
            if existe_bomba_um and tempo_decorrido < bomba.tempo_duracao_bomba_advanced:
                bomba.desenhar_bomba(matrizes.matriz, bomba.bomba_y_um, bomba.bomba_x_um)
            elif existe_bomba_um and tempo_decorrido < bomba.tempo_duracao_bomba_advanced + bomba.tempo_explosão_bomba:
                bomba.desenhar_explosao(matrizes.matriz, bomba.bomba_y_um, bomba.bomba_x_um)
                menu.explosion_sound.play()
            elif existe_bomba_um and tempo_decorrido >= bomba.tempo_duracao_bomba_advanced + bomba.tempo_explosão_bomba:
                # Resetar o estado após a explosão
                existe_bomba_um = False
                ativar_bomba_um = False

                bomba.tempo_ativação_bomba_um = None

        # estrutura para colocar a bomba para o lado que o player está direcionado

        if ativar_bomba_dois:

            if bomba.tempo_ativação_bomba_dois is None:
                bomba.tempo_ativação_bomba_dois = time.time()


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
            tempo_decorrido = time.time() - bomba.tempo_ativação_bomba_dois

            # Lógica para desenhar e explodir a bomba
            if existe_bomba_dois and tempo_decorrido < bomba.tempo_duracao_bomba_advanced:
                bomba.desenhar_bomba(matrizes.matriz, bomba.bomba_y_dois, bomba.bomba_x_dois)
            elif (
                    existe_bomba_dois and tempo_decorrido < bomba.tempo_duracao_bomba_advanced + bomba.tempo_explosão_bomba):
                bomba.desenhar_explosao(matrizes.matriz, bomba.bomba_y_dois, bomba.bomba_x_dois)
                menu.explosion_sound.play()
            elif existe_bomba_dois and tempo_decorrido >= bomba.tempo_duracao_bomba_advanced + bomba.tempo_explosão_bomba:
                # Resetar o estado após a explosão
                existe_bomba_dois = False
                ativar_bomba_dois = False
                bomba.tempo_ativação_bomba_dois = None  # Indicar que a bomba não está ativa

        matrizes.desenhar_tela(matrizes.matriz_y, matrizes.matriz_x, matrizes.matriz)

        if WConio2.kbhit():
            value, symbol = WConio2.getch()

            # movimenta e muda de angulo o player
            if symbol in 'aA' and player.verificar_colisao(matrizes.matriz, player.player_y_um, player.player_x_um - 1, "esquerda"):
                player.player_x_um -= 1
                angulo_player_um = "esquerda"
            elif symbol in 'dD' and player.verificar_colisao(matrizes.matriz, player.player_y_um, player.player_x_um + 1, "direita"):
                player.player_x_um += 1
                angulo_player_um = "direita"
            elif symbol in 'wW' and player.verificar_colisao(matrizes.matriz, player.player_y_um - 1, player.player_x_um, "cima"):
                player.player_y_um -= 1
                angulo_player_um = "cima"
            elif symbol in 'sS' and player.verificar_colisao(matrizes.matriz, player.player_y_um + 1, player.player_x_um, "baixo"):
                player.player_y_um += 1
                angulo_player_um = "baixo"

            # player coloca a bomba no mapa
            elif symbol in 'fF':
                if angulo_player_um == "esquerda" and bomba.verificar_colisao(matrizes.matriz, player.player_y_um, player.player_x_um - dimensao_jogo):
                    ativar_bomba_um = True
                elif angulo_player_um == "direita" and bomba.verificar_colisao(matrizes.matriz, player.player_y_um, player.player_x_um + dimensao_jogo):
                    ativar_bomba_um = True
                elif angulo_player_um == "cima" and bomba.verificar_colisao(matrizes.matriz, player.player_y_um - dimensao_jogo, player.player_x_um):
                    ativar_bomba_um = True
                elif angulo_player_um == "baixo" and bomba.verificar_colisao(matrizes.matriz, player.player_y_um + dimensao_jogo, player.player_x_um):
                    ativar_bomba_um = True

            # movimenta e muda de angulo o player
            if symbol in '4' and player.verificar_colisao(matrizes.matriz, player.player_y_dois, player.player_x_dois - 1, "esquerda"):
                player.player_x_dois -= 1
                angulo_player_dois = "esquerda"
            elif symbol in '6' and player.verificar_colisao(matrizes.matriz, player.player_y_dois, player.player_x_dois + 1, "direita"):
                player.player_x_dois += 1
                angulo_player_dois = "direita"
            elif symbol in '8' and player.verificar_colisao(matrizes.matriz, player.player_y_dois - 1, player.player_x_dois, "cima"):
                player.player_y_dois -= 1
                angulo_player_dois = "cima"
            elif symbol in '5' and player.verificar_colisao(matrizes.matriz, player.player_y_dois + 1, player.player_x_dois, "baixo"):
                player.player_y_dois += 1
                angulo_player_dois = "baixo"

            # Player coloca a bomba no mapa
            elif symbol in 'mM':
                if angulo_player_dois == "esquerda" and bomba.verificar_colisao(matrizes.matriz, player.player_y_dois, player.player_x_dois - dimensao_jogo):
                    ativar_bomba_dois = True
                elif angulo_player_dois == "direita" and bomba.verificar_colisao(matrizes.matriz, player.player_y_dois, player.player_x_dois + dimensao_jogo):
                    ativar_bomba_dois = True
                elif angulo_player_dois == "cima" and bomba.verificar_colisao(matrizes.matriz, player.player_y_dois - dimensao_jogo, player.player_x_dois):
                    ativar_bomba_dois = True
                elif angulo_player_dois == "baixo" and bomba.verificar_colisao(matrizes.matriz, player.player_y_dois + dimensao_jogo, player.player_x_dois):
                    ativar_bomba_dois = True