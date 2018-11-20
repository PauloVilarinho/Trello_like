from classes.sistema import Sistema

def main():
    sistema = Sistema()
    print(start)
    opcao = ""
    while opcao != "0" :
        opcao = input(menu_unlogged)
        if opcao == "1" :
            nome = input("Digite o nome do Usuário:  ")
            email = input("Digite o email do Usuário:  ")
            senha = input("Digite a senha do Usuário:  " )
            if sistema.criar_usuario(nome,email,senha):
                iniciar_sessao(sistema)
            else :
                print("email ou nome de usuário já utilizado.")
        if opcao == "2":
            email = input("Digite o email do Usuário:  ")
            senha = input("Digite a senha do Usuário:  ")
            if sistema.logar_usuario(email,senha):
                iniciar_sessao(sistema)
            else :
                print("email ou senha invalidas")

start = """T)tttttt R)rrrrr  E)eeeeee L)       L)        O)oooo
   T)    R)    rr E)       L)       L)       O)    oo
   T)    R)  rrr  E)eeeee  L)       L)       O)    oo
   T)    R) rr    E)       L)       L)       O)    oo
   T)    R)   rr  E)       L)       L)       O)    oo
   T)    R)    rr E)eeeeee L)llllll L)llllll  O)oooo
                                                        """
menu_unlogged = """Bem vindo ao Trello
digite a opção que deseja usuar
1 - Criar Conta
2 - Acessar Conta
0 - Sair do Programa

"""




def iniciar_sessao(sistema):
    opcao = ""
    while opcao != "0":
        opcao = input(menu_logged)
        if opcao == "0" :
            sistema.deslogar()
        if opcao == "1" :
            nome = input("Digite o nome do Time: ")
            sistema.criar_time(nome)
            #tela_time(sistema)
        if opcao == "2" :
            titulo = input("Digite o Nome do Quadro: ")
            sistema.criar_quadro(titulo)
            tela_quadro(sistema)
        if opcao == "3" :
            quadros = sistema.listar_quadros()
            for quadro in quadros:
                print(quadro)
            titulo = input("Qual quadro deseja visualizar? (digite igual ao nome do quadro) ")
            if sistema.acessar_quadro(titulo):
                pass
                tela_quadro(sistema)
            else :
                print("Quadro não existente ou não disponivel ao usuário atual")
        if opcao == "4" :
            times = sistema.listar_times()
            for time in times:
                print(time)
            titulo = input("Qual time deseja vizualizar? (digite igual ao nome do time) ")
            if sistema.acessar_time(titulo):
                pass
                #tela_time(sistema)
            else :
                print("Time não existente ou não disponivem ao usuário atual")

menu_logged = """Bem vindo
O que deseja fazer?
1 - Criar Time
2 - Criar Quadro
3 - Acessar seus Quadros
4 - Acessar seus Times
0 - Deslogar

"""

def tela_quadro(sistema):
    opcao = 1
    while opcao != "0" :
        opcao = input(menu_quadro)
        if opcao == "0":
            sistema.sair_quadro()
        elif opcao == "1" :
            titulo = input("Digite o Nome da Lista a ser Criada: ")
            sistema.adcionar_lista(titulo)
            #tela_lista(sistema)
        elif opcao == "2" :
            titulo = input("Digite o nome da lista a ser movida: ")
            posicao = input("Para qual posição deseja mover  a lista?  ")
            if sistema.mover_lista(titulo):
                print("lista movida com sucesso")
            else:
                print("lista não existe no Quadro")
        elif opcao == "3" :
            listas = sistema.listar_listas()
            for lista in listas :
                print(lista)
            titulo = input("Digite o Nome da Lista a ser Acessada: ")
            if sistema.acessar_lista(titulo):
                tela_lista(sistema)
            else :
                print("Lista com esse nome não existe nesse quadro")
        else :
            print("Operação não existente")


menu_quadro = """O que deseja fazer?
1 - Adcionar lista
2 - Mover lista
3 - Acessar lista
0 - Sair do Quadro"""


def tela_lista(sistema):
    pass





if __name__ == '__main__':
    main()
