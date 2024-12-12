import os
import WConio2
import cursor

VAZIO = " "
maxY = 30
maxX = 120
matriz = []

contador = 1
relogio = 0
controle = False

logo = [
    " ██████╗  █████╗ ███╗   ███╗███████╗   ██████╗  ██████╗ ███╗   ███╗██████╗ ",
    "██╔════╝ ██╔══██╗████╗ ████║██╔════╝   ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗",
    "██║  ███╗███████║██╔████╔██║█████╗     ██████╔╝██║   ██║██╔████╔██║██████╔╝",
    "██║   ██║██╔══██║██║╚██╔╝██║██╔══╝     ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗",
    "╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗   ██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝",
    " ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝   ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ "
]

menu = [
    "[Z] JOGAR    ",
    "[X] PONTUAÇÃO",
    "[C] SAIR     "
]

bomba = [
         " " * 44 + "             . . .             " + 45 * " ",
         " " * 44 + "              \|/              " + 45 * " ",
         " " * 44 + "            `--+--'            " + 45 * " ",
         " " * 44 + "              /|\              " + 45 * " ",
         " " * 44 + "             ' | '             " + 45 * " ",
         " " * 44 + "           ,--'#`--.           " + 45 * " ",
         " " * 44 + "           |#######|           " + 45 * " ",
         " " * 44 + "        _.-'#######`-._        " + 45 * " ",
         " " * 44 + "     ,-'###############`-.     " + 45 * " ",
         " " * 44 + "   ,'#####################`,   " + 45 * " ",
         " " * 44 + "  /#########################\  " + 45 * " ",
         " " * 44 + " |###########################| " + 45 * " ",
         " " * 44 + "|#############################|" + 45 * " ",
         " " * 44 + "|#############################|" + 45 * " ",
         " " * 44 + "|#############################|" + 45 * " ",
         " " * 44 + "|#############################|" + 45 * " ",
         " " * 44 + " |###########################| " + 45 * " ",
         " " * 44 + "  \#########################/  " + 45 * " ",
         " " * 44 + "   `.#####################,'   " + 45 * " ",
         " " * 44 + "     `._###############_,'     " + 45 * " ",
         " " * 44 + "         `--..#####..--'       " + 45 * " "
]


def desenhaBomba(matriz):
    #transição de tela
    inicio = maxY - contador
    centro = int((maxX - len(bomba[0])) / 2)
    for i, linha in enumerate(bomba):
        for j, caractere in enumerate(linha):
            if inicio + i > -1:
                matriz[inicio + i][centro + j] = caractere

        if inicio + i == maxY - 1:
            break




def desenhaLogo(matriz):
    centro = int((maxX - len(logo[0])) / 2)

    for i, linha in enumerate(logo):
        for j, caractere in enumerate(linha):
            matriz[5 + i][centro + j] = caractere

def desenhaMenu(matriz):
    centro = int((maxX - len(menu[0])) / 2) 
    for i, linha in enumerate(menu):
        for j, caractere in enumerate(linha):
            matriz[15 + i][centro + j] = caractere




def limparTela(matriz):
    '''
        função que limpa a tela do jogo apagando todos os valores
        da matriz de controle
    '''
    for y in range(maxY):
        for x in range(maxX):
            matriz[y][x] = VAZIO


def desenhaTela(matriz):
    '''
        função que desenha a tela do jogo imprimindo uma sequencia de
        linhas de strings com conteúdo da matriz de controle do jogo
    '''
    separador = "#" * (maxX + 2)  # Ajusta o separador para incluir as paredes
    print(separador)
    tela = ''
    for y in range(maxY):
        linha = '#'  # Adiciona a parede esquerda
        for x in range(maxX):
            linha += matriz[y][x]
        linha += '#'  # Adiciona a parede direita
        tela += linha + '\n'
    print(tela, end="")
    print(separador)



# Parte principal do programa
if __name__ == '__main__':
    os.system('cls')
    cursor.hide()

    # inicialiando a matriz de controle
    for y in range(maxY):
        matriz.append([])
        for x in range(maxX):
            matriz[y].append(VAZIO)

    while (True):


        # posicionando cursor da tela sempre no mesmo lugar
        WConio2.gotoxy(0, 0)

        # limpando a matriz antes de desenhar nela
        limparTela(matriz)

        desenhaLogo(matriz)

        desenhaMenu(matriz)


        
        # impressão na tela
        desenhaTela(matriz)

        if WConio2.kbhit():
            value, symbol = WConio2.getch()

            if symbol in 'zZ':
                pass
            elif symbol in 'xX':
                pass
            elif symbol in 'Cc':
                while True:
                    WConio2.gotoxy(0, 0)
                    limparTela(matriz)
                    if contador < 30:
                        desenhaLogo(matriz)
                        desenhaMenu(matriz)
                    desenhaBomba(matriz)

                    if relogio % 50 == 0:
                        contador = contador + 1

                    relogio = relogio + 1
                    desenhaTela(matriz)