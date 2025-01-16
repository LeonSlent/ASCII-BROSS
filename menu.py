import WConio2
import matrizes

contador = 1
relogio = 0

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


opcoes = [
    "[Z] JOGAR    ",
    "[X] PONTUAÇÃO",
    "[C] SAIR     "
]

bomba = [
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

def desenhar_logo(matriz_x, matriz):
    '''
        função que imprime a matriz da logo na tela
    '''
    centro = int((matriz_x - len(logo[0])) / 2) #encontra o índice da lista que deixará a logo no centro

    for i, linha in enumerate(logo):
        for j, caractere in enumerate(linha):
            matriz[5 + i][centro + j] = caractere


def desenhar_pontuacao(matriz_x, matriz):
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
    centro = int((matriz_x - len(bomba[0])) / 2) #encontra o índice da lista que deixará a matriz da bomba no centro da tela
    for i, linha in enumerate(bomba):
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
            desenhar_logo(matrizes.matriz_x, matrizes.matriz)
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
