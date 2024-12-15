import os
import WConio2
import cursor


VAZIO = " "
maxY = 30
maxX = 120
relogio = 0
matriz = []

bomb = "@"
explosioSym = "#"
obsUm = "░"

#Player_um
delay_um = 0
bichoCabeca_um = "$"
bichoY_um = 1
bichoX_um = 10
#Ativar a bomba_um
bomb_active_um = False
#Verificar se existe outra bomba_um
bomb_exist_um = False
relogioExplode_um = 0
bombX_um = 0
bombY_um = 0


#Player_dois
delay_dois = 0
bichoCabeca_dois = "%"
bichoY_dois = 1
bichoX_dois = 30
#Ativar a bomba_dois
bomb_active_dois = False
#Verificar se existe outra bomba_dois
bomb_exist_dois = False
relogioExplode_dois = 0
bombX_dois = 0
bombY_dois = 0



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
        # Retorna True se está vazio ou se é uma explosão
        return matriz[novo_y][novo_x] == VAZIO or matriz[novo_y][novo_x] == explosioSym
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

        if bomb_active_um == True and relogioExplode_um <= 1000:
            if bomb_exist_um == False:
                bombX_um = bichoX_um + 2
                bombY_um = bichoY_um + 1 
                matriz[bombY_um][bombX_um] = bomb
                relogioExplode_um += 1
                bomb_exist_um = True
            elif bomb_exist_um == True and relogioExplode_um < 500:
                matriz[bombY_um][bombX_um] = bomb
                relogioExplode_um += 1
            elif relogioExplode_um >= 500 and relogioExplode_um <= 1000 and bomb_exist_um == True:
                matriz[bombY_um+1][bombX_um] = explosioSym
                matriz[bombY_um+2][bombX_um] = explosioSym
                matriz[bombY_um-1][bombX_um] = explosioSym
                matriz[bombY_um-2][bombX_um] = explosioSym
                matriz[bombY_um][bombX_um+1] = explosioSym
                matriz[bombY_um][bombX_um+2] = explosioSym
                matriz[bombY_um][bombX_um-1] = explosioSym
                matriz[bombY_um][bombX_um-2] = explosioSym
                relogioExplode_um += 1
                if relogioExplode_um == 1000 and bomb_exist_um == True:
                    relogioExplode_um = 0
                    bomb_active_um = False
                    bomb_exist_um = False
                    
        if bomb_active_dois == True and relogioExplode_dois <= 1000:
            if bomb_exist_dois == False:
                bombX_dois = bichoX_dois + 2
                bombY_dois = bichoY_dois + 1 
                matriz[bombY_dois][bombX_dois] = bomb
                relogioExplode_dois += 1
                bomb_exist_dois = True
            elif bomb_exist_dois == True and relogioExplode_dois < 500:
                matriz[bombY_dois][bombX_dois] = bomb
                relogioExplode_dois += 1
            elif relogioExplode_dois >= 500 and relogioExplode_dois <= 1000 and bomb_exist_dois == True:
                matriz[bombY_dois+1][bombX_dois] = explosioSym
                matriz[bombY_dois+2][bombX_dois] = explosioSym
                matriz[bombY_dois-1][bombX_dois] = explosioSym
                matriz[bombY_dois-2][bombX_dois] = explosioSym
                matriz[bombY_dois][bombX_dois+1] = explosioSym
                matriz[bombY_dois][bombX_dois+2] = explosioSym
                matriz[bombY_dois][bombX_dois-1] = explosioSym
                matriz[bombY_dois][bombX_dois-2] = explosioSym
                relogioExplode_dois += 1
                if relogioExplode_dois == 1000 and bomb_exist_dois == True:
                    relogioExplode_dois = 0
                    bomb_active_dois = False
                    bomb_exist_dois = False
        
        #verificar se a bomba acertou o player                    
        if matriz[bichoY_um][bichoX_um] == explosioSym:
            bichoCabeca_um = VAZIO
        elif matriz[bichoY_dois][bichoX_dois] == explosioSym:
            bichoCabeca_dois = VAZIO    

        #impressão na tela
        desenhaTela(matriz)

        #controlando personages
        if WConio2.kbhit():
            value, symbol = WConio2.getch()
            
            if bichoCabeca_um == "$":
                if symbol == 'a' and verificar_colisao(bichoY_um, bichoX_um - 1, matriz):
                    bichoX_um -= 1
                elif symbol == 'd' and verificar_colisao(bichoY_um, bichoX_um + 1, matriz):
                    bichoX_um += 1
                elif symbol == 'w' and verificar_colisao(bichoY_um - 1, bichoX_um, matriz):
                    bichoY_um -= 1
                elif symbol == 's' and verificar_colisao(bichoY_um + 1, bichoX_um, matriz):
                    bichoY_um += 1
                elif symbol == 'f':
                    bomb_active_um = True

            if bichoCabeca_dois == "%":
                if symbol == 'j' and verificar_colisao(bichoY_dois, bichoX_dois - 1, matriz):
                    bichoX_dois -= 1
                elif symbol == 'l' and verificar_colisao(bichoY_dois, bichoX_dois + 1, matriz):
                    bichoX_dois += 1
                elif symbol == 'i' and verificar_colisao(bichoY_dois - 1, bichoX_dois, matriz):
                    bichoY_dois -= 1
                elif symbol == 'k' and verificar_colisao(bichoY_dois + 1, bichoX_dois, matriz):
                    bichoY_dois += 1
                elif symbol == 'h':
                    bomb_active_dois = True


