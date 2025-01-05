import os
import sys
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
bichoY_um = 2
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

# Função para desenhar o mapa no terminal utilizando ANSI
def desenhaTelaANSI(matriz):
    for y in range(len(matriz)):
        sys.stdout.write("\033[%d;0H" % (y + 1))  # Move o cursor para a linha correta
        sys.stdout.write(''.join(matriz[y]))
    sys.stdout.flush()

# Representação do mapa como uma mapa_jogavel
MAPA = [
    list("████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████"), 
    list("█                                         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                 █"), 
    list("█               ▓▓▓▓▓▓▓▓▓▓▓▓▓      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            █"), 
    list("█               ▓▓▓▓▓▓▓▓▓▓▓▓▓      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    █"), 
    list("█                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       ▓▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    █"),     
    list("█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█"), 
    list("█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█"),         
    list("█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█"),     
    list("█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ▓▓▓█"),         
    list("█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█"),     
    list("█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█"), 
    list("█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓▓▓▓▓█"), 
    list("█▓▓▓▓▓▓▓▓▓▓                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█"), 
    list("█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█"), 
    list("█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█"),         
    list("█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█"), 
    list("█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█"),
    list("█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█"),     
    list("█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ▓█"), 
    list("█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ▓▓▓▓▓▓▓▓▓▓▓█"), 
    list("█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓           ▓█"),
    list("█▓▓▓▓▓          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█"),         
    list("█▓▓▓▓▓▓▓▓▓▓▓▓▓          ▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█"),     
    list("█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ █"), 
    list("█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓           ▓█"), 
    list("█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█"),     
    list("█     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█"), 
    list("█     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓█"),         
    list("█              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█"), 
    list("█                 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ █"), 
    list("████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")
]

mapa_jogavel = [linha[:] for linha in MAPA]

def limparTela(mapa_jogavel):
    '''
        função que limpa a tela do jogo apagando todos os valores
        da mapa_jogavel de controle
    '''
    for y in range(maxY):
        for x in range(maxX):
            mapa_jogavel[y][x] = VAZIO


def verificar_colisao(novo_y, novo_x, mapa_jogavel):
    '''
        Verifica se uma posição na mapa_jogavel está disponível para movimentação.
        Retorna True se a posição está livre e False se há colisão.
    '''
    # Garantir que a posição está dentro dos limites da mapa_jogavel
    if 0 <= novo_y < maxY and 0 <= novo_x < maxX:
        # Retorna True se está vazio ou se é uma explosão
        return mapa_jogavel[novo_y][novo_x] == VAZIO or mapa_jogavel[novo_y][novo_x] == explosioSym
    return False  # Fora dos limites, não pode se mover

#Parte principal do programa
if __name__ == '__main__':
    os.system('cls')
    cursor.hide()
   
    while(True):
        #posicionando cursor da tela sempre no mesmo lugar
        WConio2.gotoxy(0,0)

        #colocar personagens dentro da mapa_jogavel
        mapa_jogavel[bichoY_um][bichoX_um] = bichoCabeca_um

        
        mapa_jogavel[bichoY_dois][bichoX_dois] = bichoCabeca_dois


        mapa_jogavel[10][10] = obsUm

        if bomb_active_um == True and relogioExplode_um <= 1000:
            if bomb_exist_um == False:
                bombX_um = bichoX_um + 2
                bombY_um = bichoY_um  
                mapa_jogavel[bombY_um][bombX_um] = bomb
                relogioExplode_um += 1
                bomb_exist_um = True
            elif bomb_exist_um == True and relogioExplode_um < 500:
                mapa_jogavel[bombY_um][bombX_um] = bomb
                relogioExplode_um += 1
            elif relogioExplode_um >= 500 and relogioExplode_um <= 1000 and bomb_exist_um == True:
                mapa_jogavel[bombY_um+1][bombX_um] = explosioSym
                mapa_jogavel[bombY_um+2][bombX_um] = explosioSym
                mapa_jogavel[bombY_um-1][bombX_um] = explosioSym
                mapa_jogavel[bombY_um-2][bombX_um] = explosioSym
                mapa_jogavel[bombY_um][bombX_um+1] = explosioSym
                mapa_jogavel[bombY_um][bombX_um+2] = explosioSym
                mapa_jogavel[bombY_um][bombX_um-1] = explosioSym
                mapa_jogavel[bombY_um][bombX_um-2] = explosioSym
                relogioExplode_um += 1
                if relogioExplode_um == 1000 and bomb_exist_um == True:
                    relogioExplode_um = 0
                    bomb_active_um = False
                    bomb_exist_um = False
                    mapa_jogavel[bombY_um][bombX_um] = VAZIO
                    mapa_jogavel[bombY_um+1][bombX_um] = VAZIO
                    mapa_jogavel[bombY_um+2][bombX_um] = VAZIO
                    mapa_jogavel[bombY_um-1][bombX_um] = VAZIO
                    mapa_jogavel[bombY_um-2][bombX_um] = VAZIO
                    mapa_jogavel[bombY_um][bombX_um+1] = VAZIO
                    mapa_jogavel[bombY_um][bombX_um+2] = VAZIO
                    mapa_jogavel[bombY_um][bombX_um-1] = VAZIO
                    mapa_jogavel[bombY_um][bombX_um-2] = VAZIO
                    
        if bomb_active_dois == True and relogioExplode_dois <= 1000:
            if bomb_exist_dois == False:
                bombX_dois = bichoX_dois + 2
                bombY_dois = bichoY_dois  
                mapa_jogavel[bombY_dois][bombX_dois] = bomb
                relogioExplode_dois += 1
                bomb_exist_dois = True
            elif bomb_exist_dois == True and relogioExplode_dois < 500:
                mapa_jogavel[bombY_dois][bombX_dois] = bomb
                relogioExplode_dois += 1
            elif relogioExplode_dois >= 500 and relogioExplode_dois <= 1000 and bomb_exist_dois == True:
                mapa_jogavel[bombY_dois+1][bombX_dois] = explosioSym
                mapa_jogavel[bombY_dois+2][bombX_dois] = explosioSym
                mapa_jogavel[bombY_dois-1][bombX_dois] = explosioSym
                mapa_jogavel[bombY_dois-2][bombX_dois] = explosioSym
                mapa_jogavel[bombY_dois][bombX_dois+1] = explosioSym
                mapa_jogavel[bombY_dois][bombX_dois+2] = explosioSym
                mapa_jogavel[bombY_dois][bombX_dois-1] = explosioSym
                mapa_jogavel[bombY_dois][bombX_dois-2] = explosioSym
                relogioExplode_dois += 1
                if relogioExplode_dois == 1000 and bomb_exist_dois == True:
                    relogioExplode_dois = 0
                    bomb_active_dois = False
                    bomb_exist_dois = False
                    mapa_jogavel[bombY_dois][bombX_dois] = VAZIO
                    mapa_jogavel[bombY_dois+1][bombX_dois] = VAZIO
                    mapa_jogavel[bombY_dois+2][bombX_dois] = VAZIO
                    mapa_jogavel[bombY_dois-1][bombX_dois] = VAZIO
                    mapa_jogavel[bombY_dois-2][bombX_dois] = VAZIO
                    mapa_jogavel[bombY_dois][bombX_dois+1] = VAZIO
                    mapa_jogavel[bombY_dois][bombX_dois+2] = VAZIO
                    mapa_jogavel[bombY_dois][bombX_dois-1] = VAZIO
                    mapa_jogavel[bombY_dois][bombX_dois-2] = VAZIO
        
        #verificar se a bomba acertou o player                    
        if mapa_jogavel[bichoY_um][bichoX_um] == explosioSym:
            bichoCabeca_um = VAZIO
        elif mapa_jogavel[bichoY_dois][bichoX_dois] == explosioSym:
            bichoCabeca_dois = VAZIO

        #impressão na tela
        desenhaTelaANSI(mapa_jogavel)

        #controlando personages
        if WConio2.kbhit():
            value, symbol = WConio2.getch()
            
            if bichoCabeca_um == "$":
                if symbol == 'a' and verificar_colisao(bichoY_um, bichoX_um - 1, mapa_jogavel):
                    mapa_jogavel[bichoY_um][bichoX_um] = VAZIO
                    bichoX_um -= 1
                elif symbol == 'd' and verificar_colisao(bichoY_um, bichoX_um + 1, mapa_jogavel):
                    mapa_jogavel[bichoY_um][bichoX_um] = VAZIO
                    bichoX_um += 1
                elif symbol == 'w' and verificar_colisao(bichoY_um - 1, bichoX_um, mapa_jogavel):
                    mapa_jogavel[bichoY_um][bichoX_um] = VAZIO
                    bichoY_um -= 1
                elif symbol == 's' and verificar_colisao(bichoY_um + 1, bichoX_um, mapa_jogavel):
                    mapa_jogavel[bichoY_um][bichoX_um] = VAZIO
                    bichoY_um += 1
                elif symbol == 'f':
                    bomb_active_um = True

            if bichoCabeca_dois == "%":
                if symbol == 'j' and verificar_colisao(bichoY_dois, bichoX_dois - 1, mapa_jogavel):
                    mapa_jogavel[bichoY_dois][bichoX_dois] = VAZIO
                    bichoX_dois -= 1
                elif symbol == 'l' and verificar_colisao(bichoY_dois, bichoX_dois + 1, mapa_jogavel):
                    mapa_jogavel[bichoY_dois][bichoX_dois] = VAZIO
                    bichoX_dois += 1
                elif symbol == 'i' and verificar_colisao(bichoY_dois - 1, bichoX_dois, mapa_jogavel):
                    mapa_jogavel[bichoY_dois][bichoX_dois] = VAZIO
                    bichoY_dois -= 1
                elif symbol == 'k' and verificar_colisao(bichoY_dois + 1, bichoX_dois, mapa_jogavel):
                    mapa_jogavel[bichoY_dois][bichoX_dois] = VAZIO
                    bichoY_dois += 1
                elif symbol == 'h':
                    bomb_active_dois = True        