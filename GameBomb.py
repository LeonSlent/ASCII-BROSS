import os
import WConio2
import cursor


VAZIO = " "
maxY = 30
maxX = 120
relogio = 0
matriz = []

#Player_um
delay_um = 0
bichoCabeca_um = "$"

#Player_dois
delay_dois = 0
bichoCabeca_dois = "%"

obsUm = "░"

bomb = "@"
#Ativar a bomba
bomb_active = False
#Verificar se existe outra bomba
bomb_exist = False
relogioExplode = 0
bombX = 0
bombY = 0
explosioSym = "#"

bichoY_um = 1
bichoX_um = 10
bichoY_dois = 1
bichoX_dois = 30


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

def verificar_colisao(novo_y, novo_x, matriz):
    '''
        Verifica se uma posição na matriz está disponível para movimentação.
        Retorna True se a posição está livre e False se há colisão.
    '''
    # Garantir que a posição está dentro dos limites da matriz
    if 0 <= novo_y < maxY and 0 <= novo_x < maxX:
        return matriz[novo_y][novo_x] == VAZIO  # Retorna True se está vazio
    return False  # Fora dos limites, não pode se mover


#Parte principal do programa
if __name__ == '__main__':
    os.system('cls')
    cursor.hide()


    #inicialiando a matriz de controle
    for y in range(maxY):
        matriz.append([])
        for x in range(maxX):
            matriz[y].append(VAZIO)
   
    while(True):
        #posicionando cursor da tela sempre no mesmo lugar
        WConio2.gotoxy(0,0)


        #limpando a matriz antes de desenhar nela
        limparTela(matriz)


        #colocar personagens dentro da matriz
        matriz[bichoY_um][bichoX_um] = bichoCabeca_um

        
        matriz[bichoY_dois][bichoX_dois] = bichoCabeca_dois


        matriz[10][10] = obsUm

        if bomb_active == True and relogioExplode <= 1000:
            if bomb_exist == False:
                bombX = bichoX_um + 2
                bombY = bichoY_um + 1 
                matriz[bombY][bombX] = bomb
                relogioExplode += 1
                bomb_exist = True
            elif bomb_exist == True and relogioExplode < 500:
                matriz[bombY][bombX] = bomb
                relogioExplode += 1
            elif relogioExplode >= 500 and relogioExplode <= 1000 and bomb_exist == True:
                matriz[bombY+1][bombX] = explosioSym
                matriz[bombY+2][bombX] = explosioSym
                matriz[bombY-1][bombX] = explosioSym
                matriz[bombY-2][bombX] = explosioSym
                matriz[bombY][bombX+1] = explosioSym
                matriz[bombY][bombX+2] = explosioSym
                matriz[bombY][bombX-1] = explosioSym
                matriz[bombY][bombX-2] = explosioSym
                relogioExplode += 1
                if relogioExplode == 1000 and bomb_exist == True:
                    relogioExplode = 0
                    bomb_active = False
                    bomb_exist = False
                            


        #impressão na tela
        desenhaTela(matriz)

        #controlando personages
        if WConio2.kbhit():
            value, symbol = WConio2.getch()

            if symbol == 'a' and verificar_colisao(bichoY_um, bichoX_um - 1, matriz):
                bichoX_um -= 1
            elif symbol == 'd' and verificar_colisao(bichoY_um, bichoX_um + 1, matriz):
                bichoX_um += 1
            elif symbol == 'w' and verificar_colisao(bichoY_um - 1, bichoX_um, matriz):
                bichoY_um -= 1
            elif symbol == 's' and verificar_colisao(bichoY_um + 1, bichoX_um, matriz):
                bichoY_um += 1
            elif symbol == 'f':
                bomb_active = True

            if symbol == 'j' and verificar_colisao(bichoY_dois, bichoX_dois - 1, matriz):
                bichoX_dois -= 1
            elif symbol == 'l' and verificar_colisao(bichoY_dois, bichoX_dois + 1, matriz):
                bichoX_dois += 1
            elif symbol == 'i' and verificar_colisao(bichoY_dois - 1, bichoX_dois, matriz):
                bichoY_dois -= 1
            elif symbol == 'k' and verificar_colisao(bichoY_dois + 1, bichoX_dois, matriz):
                bichoY_dois += 1
            elif symbol == 'h':
                bomb_active = True


