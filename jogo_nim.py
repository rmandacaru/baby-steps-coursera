#python3 jogo_nim.py

def computador_escolhe_jogada(n,m):
    
    if n <= m:
        return n
    else:
        if n % (m+1) > 0:
            return n % (m+1)
        return m


def usuario_escolhe_jogada(n,m):
    
    x = int(input("Quantas peças você quer tirar?"))
    
    while x>m or x == 0 or x<0 or x>n:
        print ("Jogada inválida! Tente de novo.")
        x = int(input("Quantas peças você quer tirar?"))
        
    return x

def partida():

    
    n= int(input("Defina a quantidade de peças:"))

    while n<=1:
        print("O número de peças deve ser maior que 1!")
        n= int(input("Defina a quantidade de peças:"))
        1
        
    m= int(input("Defina o limite retirada de peças por jogada:"))
    
    while m>n:
        print("A quantidade de peças por jogada de ser menor ou igual as peças totais")
        m=int(input("Defina o limite retirada de peças por jogada:"))

    valor=0
    jogada=0

    if n%(m+1)==0:
        print("Você começa!")
        jogada = 1
        while n>0:
            if jogada==1:
                valor= usuario_escolhe_jogada(n,m)
                print("\nVocê tirou", valor, "peça(s).")
                n=n-valor
                print("Agora restam",n, "peças no tabuleiro")
                jogada=2
            else:
                valor= computador_escolhe_jogada(n,m)
                print("\nO computador tirou", valor, "peça(s).")
                n=n-valor
                print("Agora restam",n, "peças no tabuleiro")
                jogada=1
                
        if jogada == 1:
            print("Fim do jogo! O computador ganhou!\n")
            return 2
        else:
            print("Fim do jogo! O você ganhou!\n")
            return 1
                
    else:
        print("\nComputador começa!")
        jogada = 2 
        while n > 0:
            if jogada == 2:
                valor = computador_escolhe_jogada(n, m)
                print("\nO computador tirou", valor, "peça(s)")
                n = n - valor
                print("Agora restam", n, "peças no tabuleiro.")
                jogada = 1
            else:
                valor = usuario_escolhe_jogada(n, m)
                print("\nVocê tirou", valor, "peça(s).")
                n = n - valor
                print("Agora restam", n, "peças no tabuleiro.")
                jogada = 2
                
        if jogada == 1:
            print("Fim do jogo! O computador ganhou!\n")
            return 2 
        else:
            print("Fim do jogo! O você ganhou!\n")
            return 1

def campeonato():
    quantidade_partida = 1
    placar_computador = placar_usuario = 0
    
    while quantidade_partida < 4:
        print("**** Rodada", quantidade_partida ,"****\n")
        if partida() == 1:
            placar_usuario = placar_usuario + 1
        else:
            placar_computador = placar_computador + 1
        quantidade_partida = quantidade_partida + 1
        
    print("**** Final do campeonato! ****\n")
    print("Placar: Você", placar_usuario, "X", placar_computador, "Computador")

def main():
    print("Bem-vindo ao jogo do NIM!")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    
    escolha = int(input("Escolha: "))    
    while escolha != 1 and escolha != 2:
        print("Escolha uma opção válida!")
        escolha = int(input("Escolha: "))
        
    if escolha == 1:
        print("\nVocê escolheu uma partida isolada!\n")
        partida()
    else:
        if escolha == 2:
            print("\nVocê escolheu um campeonato!\n")
            campeonato()

main()


        

        




