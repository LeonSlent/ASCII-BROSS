import os
import WConio2
import cursor

VAZIO = " "
maxY = 30
maxX = 120
matriz = []


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

bomba = [r"             . . .             "
         r"              \|/              "
         r"            `--+--'            "
         r"              /|\              "
         r"             ' | '             "
         r"           ,--'#`--.           "
         r"           |#######|           "
         r"        _.-'#######`-._        "
         r"     ,-'###############`-.     "
         r"   ,'#####################`,   "
         r"  /#########################\  "
         r" |###########################| "
         r"|#############################|"
         r"|#############################|"
         r"|#############################|"
         r"|#############################|"
         r" |###########################| "
         r"  \#########################/  "
         r"   `.#####################,'   "
         r"     `._###############_,'     "
         r"         `--..#####..--'       "
         ]




def desenhaLogo(matriz):
    inicioLogo = int((maxX - len(logo[0])) / 2)

    for i, linha in enumerate(logo):
        for j, caractere in enumerate(linha):
            matriz[5 + i][inicioLogo + j] = caractere

def desenharMenu(matriz):
    for i, linha in enumerate(menu):
        for j, caractere in enumerate(linha):
            matriz[15 + i][53 + j] = caractere


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

        desenharMenu(matriz)

        # impressão na tela
        desenhaTela(matriz)

        if WConio2.kbhit():
            value, symbol = WConio2.getch()

            if symbol in 'zZ':
                pass
            elif symbol in 'xX':
                pass
            elif symbol in 'Cc':
                exit()
                
