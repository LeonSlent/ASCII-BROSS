def score ():
    return 0

def jogo ():
    return 0

def save():
    return 0

def menu ():
    while True:
        print ("####################")
        print ("1 - Jogar")
        print ("2 - Hightscore")
        print ("3 - Sair")
        print ("####################")

        try:
            opcao = int (input ("Digite a opção escolhida: "))
            if opcao == 1:
                jogo()
            elif opcao == 2:
                score()
            elif opcao == 3:
                save()
                print ("Jogo salvo, nao demore a voltar!")
                break
            else:
                print ("Por favor digite uma opção valida!")
        except ValueError:
            print ("Por favor digite um número")
def main():
    print("Bem-vindo ao jogo!")
    menu()

if __name__ == "__main__":
    main()