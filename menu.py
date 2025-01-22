import WConio2
import matrizes
import player
import pygame
import os
import bomba
pygame.init()
pygame.mixer.init()
#sons
pasta_atual = os.path.dirname(os.path.abspath(__file__))

pygame.mixer.music.load(os.path.join(pasta_atual, "Sons", "Fundo.wav"))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

explosion_sound = pygame.mixer.Sound(os.path.join(pasta_atual, "Sons", "Bomba.wav"))
explosion_sound.set_volume(0.7)

tecla_sound = pygame.mixer.Sound(os.path.join(pasta_atual, "Sons", "Tecla.mp3"))
tecla_sound.set_volume(0.7)

contador = 1
relogio = 0
player_perdeu = 0

logo = [
    " ██████╗  █████╗ ███╗   ███╗███████╗   ██████╗  ██████╗ ███╗   ███╗██████╗ ",
    "██╔════╝ ██╔══██╗████╗ ████║██╔════╝   ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗",
    "██║  ███╗███████║██╔████╔██║█████╗     ██████╔╝██║   ██║██╔████╔██║██████╔╝",
    "██║   ██║██╔══██║██║╚██╔╝██║██╔══╝     ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗",
    "╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗   ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝",
    " ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝   ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ "
]

PONTUACAO = [
    "██████╗  ██████╗ ███╗   ██╗████████╗██╗   ██╗ █████╗  ██████╗ █████╗  ██████╗" ,
    "██╔══██╗██╔═══██╗████╗  ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝██╔══██╗██╔═══██╗",
    "██████╔╝██║   ██║██╔██╗ ██║   ██║   ██║   ██║███████║██║     ███████║██║   ██║",
    "██╔═══╝ ██║   ██║██║╚██╗██║   ██║   ██║   ██║██╔══██║██║     ██╔══██║██║   ██║",
    "██║     ╚██████╔╝██║ ╚████║   ██║   ╚██████╔╝██║  ██║╚██████╗██║  ██║╚██████╔╝",
    "╚═╝      ╚═════╝ ╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝"
]

game_over = [
    " ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ ",
    "██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗",
    "██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝",
    "██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗",
    "╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║",
    " ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝",
]

opcoes = [
    "[Z] JOGAR MODO NORMAL  ",
    "[A] JOGAR MODO AVANÇADO",
    "[P] PONTUAÇÃO          ",
    "[C] SAIR               "
]
opcoes_pontuacao = [
    "[P] VOLTAR MENU",
    "[R] RESETAR PONTUAÇÃO"
]

bomba_transicao = [
        "             . . .             " ,
        "              \|/              " ,
        "            `--+--'            " ,
        "              /|\              " ,
        "             ' | '             " ,
        "           ,--'#`--.           " ,
        "           |#######|           " ,
        "        _.-'#######`-._        " ,
        "     ,-'###############`-.     " ,
        "   ,'#####################`,   " ,
        "  /#########################\  " ,
        " |###########################| " ,
        "|#############################|" ,
        "|#############################|" ,
        "|#############################|" ,
        "|#############################|" ,
        " |###########################| " ,
        "  \#########################/  " ,
        "   `.#####################,'   " ,
        "     `._###############_,'     " ,
        "         `--..#####..--'       " 
]

explosao_fim = [
                "               ________________                ",
                "          ____/ (  (    )   )  \___            ",
                "         /( (  (  )   _    ))  )   )\          ",
                "       ((     (   )(    )  )   (   )  )        ",
                "     ((/  ( _(   )   (   _) ) (  () )  )       ",
                "    ( (  ( (_)   ((    (   )  .((_ ) .  )_     ",
                "   ( (  )    (      (  )    )   ) . ) (   )    ",
                "  (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )   ",
                " ( (  (   ) (  )   (  ))     ) _)(   )  )  )   ",
                " ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )  ",
                " (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )  ",
                " ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )  ",
                "  ((  (   )(    (     _    )   _) _(_ (  (_ )  ",
                "   (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)   ",
                "   ((__)        \\||lll|l||///          \_))   ",
                "            (   /(/ (  )  ) )\   )             ",
                "          (    ( ( ( | | ) ) )\   )            ",
                "           (   /(| / ( )) ) ) )) )             ",
                "         (     ( ((((_(|)_)))))     )          ",
                "          (      ||\(|(|)|/||     )            ",
                "        (        |(||(||)||||        )         ",
                "          (     //|/l|||)|\\ \     )           ",
                "        (/ / //  /|//||||\\  \ \  \ _)         "
]


bomba_pontuacao = [
            "               ****  ",
            "              *****  ",
            "             █* **** ",
            "            █▌       ",
            "           █▌        ",
            "        █▀▀▀▀█       ",
            "        █    █       ",
            "     ▐██████████▌    ",
            "   ▐██         #██▌  ",
            "  ▐█   ██        #█▌ ",
            " ▐█   ██           █▌",
            " █   ██            #█",
            " █                ##█",
            " ▐█  ██          ##█▌",
            "  ▐█#         ####█▌ ",
            "   ▐█#####  #####█▌  ",
            "    ▐███######███▌   ",
            "        ██████       "
]


def menu_pontuacao():
    while True:
        WConio2.gotoxy(0, 0)
        matrizes.limpar_tela(matrizes.matriz_y, matrizes.matriz_x, matrizes.vazio, matrizes.matriz)

        desenhar_PONTUACAO(matrizes.matriz_x, matrizes.matriz)
        player.desenhar_pontuacoes(matrizes.matriz)
        desenhar_bomba_pontuacao(matrizes.matriz)
        desenhar_opcoes_pontuacao(matrizes.matriz)
        player.desenhar_player(matrizes.matriz, player.player_baixo_um, 20, 15)
        player.desenhar_player(matrizes.matriz, player.player_baixo_dois, 20, 74)

        matrizes.desenhar_tela(matrizes.matriz_y, matrizes.matriz_x, matrizes.matriz)


        if WConio2.kbhit():
            value, symbol = WConio2.getch()
            if symbol in 'pP':
                tecla_sound.play()
                return

def desenhar_bomba_pontuacao(matriz):
    centro = int((matrizes.matriz_x - len(bomba_pontuacao[0])) / 2) #encontra o índice da lista que deixará a logo no centro
    for i, linha in enumerate(bomba_pontuacao):
        for j, caractere in enumerate(linha):
                matriz[12 + i][centro + j] = caractere



def desenhar_opcoes_pontuacao(matriz):
    '''
        função que imprime a matriz das opções do menu na tela
    '''
    
    for i, linha in enumerate(opcoes_pontuacao):
        for j, caractere in enumerate(linha):
            if i == 0:
                matriz[33 + i][3 + j] = caractere
            if i == 1:
                matriz[32 + i][71 + j] = caractere

#Adicionei o parametro "imagem" para que possa ser usado em outros textos
def desenhar_logo(matriz_x, matriz, imagem):
    '''
        função que imprime a matriz da logo na tela
    '''
    centro = int((matriz_x - len(imagem[0])) / 2) #encontra o índice da lista que deixará a logo no centro

    for i, linha in enumerate(imagem):
        for j, caractere in enumerate(linha):
            matriz[5 + i][centro + j] = caractere

def desenhar_PONTUACAO(matriz_x, matriz):
    '''
        função que imprime a matriz da pontuação na tela
    '''
    centro = int((matriz_x - len(PONTUACAO[0])) / 2)

    for i, linha in enumerate(PONTUACAO):
        for j, caractere in enumerate(linha):
            matriz[5 + i][centro + j] = caractere

def desenhar_opcoes(matriz_x, matriz):
    '''
        função que imprime a matriz das opções do menu na tela
    '''
    centro = int((matriz_x - len(opcoes[0])) / 2) #encontra o índice da lista que deixará a matriz das opções do menu no centro

    for i, linha in enumerate(opcoes):
        for j, caractere in enumerate(linha):
            matriz[15 + i][centro + j] = caractere

def desenhar_bomba(matriz_y, matriz_x, matriz, contador):
    '''
        função que desenha uma bomba passando na tela como transição de cena
    '''
    posicao = matriz_y - contador #encontra o índice Y que a bomba deve aparecer e vai atualizando o valor para gerar movimento
    centro = int((matriz_x - len(bomba_transicao[0])) / 2) #encontra o índice da lista que deixará a matriz da _desenho no centro da tela
    for i, linha in enumerate(bomba_transicao):
        for j, caractere in enumerate(linha):
            if posicao + i > -1: #quando a posicao chegar a maior que -1 ela deve parar de ser desenhada, pois já completou uma volta pela tela
                matriz[posicao + i][centro + j] = caractere

        if posicao + i == matriz_y - 1: # impede que a bomba seja desenhada em um índice errado da matriz
            break

def transicao_tela(contador, relogio):
    while True:
        # posicionando cursor da tela sempre no mesmo lugar
        WConio2.gotoxy(0, 0)
        matrizes.limpar_tela(matrizes.matriz_y, matrizes.matriz_x, matrizes.vazio, matrizes.matriz)

        # é aqui que você altera o que aparece no fundo da transição
        if contador < 27: # quando o contador chegar a 30, a bomba ja passou pelas opções e logo, então não precisa mais mostra-las
            desenhar_logo(matrizes.matriz_x, matrizes.matriz, logo)
            desenhar_opcoes(matrizes.matriz_x, matrizes.matriz)

        desenhar_bomba(matrizes.matriz_y, matrizes.matriz_x, matrizes.matriz, contador)

        matrizes.desenhar_tela(matrizes.matriz_y, matrizes.matriz_x, matrizes.matriz)
        
        relogio = relogio + 1

        if relogio % 50 == 0: # logica para diminuir a velocidade que a bomba percorre a tela
            contador = contador + 2 # quando o valor do contador é aumentado, a bomba se movimenta na matriz
        
        if contador > 50: # condição de parada do loop para retornar as variaveis de controle ao seu valor iniciar para que outro transição de tela aconteça
            contador = 1
            relogio = 0
            break

def fim_jogo_player(matriz_x, matriz):
    '''
        função que desenha o player que perdeu e a bomba
    '''
    centro = int((matriz_x - len(player.player_baixo[0])) / 2) #encontra o índice da lista que deixará a matriz das opções do menu no centro

    if player.player_vivo_um == False and player.player_vivo_dois == True:
        player.player_baixo_um = player.colorir_player(player.player_baixo, 1)
        for i, linha in enumerate(player.player_baixo_um):
            for j, caractere in enumerate(linha):
                matriz[15 + i][centro + j] = caractere

    elif player.player_vivo_dois == False and player.player_vivo_um == True:
        player.player_baixo_dois = player.colorir_player(player.player_baixo, 2)
        for i, linha in enumerate(player.player_baixo_dois):
            for j, caractere in enumerate(linha):
                matriz[15 + i][centro + j] = caractere
    
    elif player.player_vivo_dois == False and player.player_vivo_um == False:
        player.player_baixo_um = player.colorir_player(player.player_baixo, 1)
        for i, linha in enumerate(player.player_baixo_um):
            for j, caractere in enumerate(linha):
                matriz[15 + i][5 + centro + j] = caractere

        player.player_baixo_dois = player.colorir_player(player.player_baixo, 2)
        for i, linha in enumerate(player.player_baixo_dois):
            for j, caractere in enumerate(linha):
                matriz[15 + i][centro + j - 5] = caractere
        

    centro = int((matriz_x - len(bomba.bomba[0])) / 2) #encontra o índice da lista que deixará a matriz das opções do menu no centro

    for i, linha in enumerate(bomba.bomba):
        for j, caractere in enumerate(linha):
            matriz[20 + i][centro + j] = caractere

def fim_jogo_explosao(matriz_x, matriz):
    '''
        função que desenha a explosao
    '''
    centro = int((matriz_x - len(explosao_fim[0])) / 2) #encontra o índice da lista que deixará a matriz das opções do menu no centro
    
    for i, linha in enumerate(explosao_fim):
        for j, caractere in enumerate(linha):
            matriz[11 + i][centro + j] = caractere

def menu_fim(time):
    while True:
        if time < 1500:
            WConio2.gotoxy(0, 0)
            matrizes.limpar_tela(matrizes.matriz_y, matrizes.matriz_x, matrizes.vazio, matrizes.matriz)
            fim_jogo_player(matrizes.matriz_x, matrizes.matriz)
            desenhar_logo(matrizes.matriz_x, matrizes.matriz, game_over)
            matrizes.desenhar_tela(matrizes.matriz_y, matrizes.matriz_x, matrizes.matriz)
        elif 1000 <= time < 2500:
            WConio2.gotoxy(0, 0)
            matrizes.limpar_tela(matrizes.matriz_y, matrizes.matriz_x, matrizes.vazio, matrizes.matriz)
            fim_jogo_explosao(matrizes.matriz_x, matrizes.matriz)
            desenhar_logo(matrizes.matriz_x, matrizes.matriz, game_over)
            matrizes.desenhar_tela(matrizes.matriz_y, matrizes.matriz_x, matrizes.matriz)
        elif time >= 2500:
            time = 0
            break
        time += 1