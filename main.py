import os
import WConio2
import cursor
import matrizes
import menu
import player
import bomba
import mapa
import game

if __name__ == '__main__':
    os.system('cls')
    cursor.hide()

    matrizes.iniciar_matriz(matrizes.matriz_y, matrizes.matriz_x, matrizes.vazio, matrizes.matriz)

    while (True):


        # posicionando cursor da tela sempre no mesmo lugar
        WConio2.gotoxy(0, 0)

        # limpando a matriz antes de desenhar nela
        matrizes.limpar_tela(matrizes.matriz_y, matrizes.matriz_x, matrizes.vazio, matrizes.matriz)

        menu.desenhar_logo(matrizes.matriz_x, matrizes.matriz, menu.logo)
        menu.desenhar_opcoes(matrizes.matriz_x, matrizes.matriz)

        # impressão da tela
        matrizes.desenhar_tela(matrizes.matriz_y, matrizes.matriz_x, matrizes.matriz)
        
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
                menu.menu_pontuacao()

            elif symbol in 'Tt':
                menu.tecla_sound.play()
                menu.menu_tutorial()


            elif symbol in 'Cc':
                menu.tecla_sound.play()
                exit()