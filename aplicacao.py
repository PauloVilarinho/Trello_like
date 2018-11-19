from classes.sistema import Sistema

def main():
    sistema = Sistema()
    print(start)
    opcao = 1
    while opcao != 0 :
        opcao = int(input(menu_unlogged))
        if opcao == 1 :
            nome = input("Digite o nome do Usuário:  ")
            email = input("Digite o email do Usuário:  ")
            senha = input("Digite a senha do Usuário:  " )
            if sistema.criar_usuario(nome,email,senha):
                iniciar_sessao(sistema)
            else :
                print("email ou nome de usuário já utilizado.")
        if opcao == 2:
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
    opcao = 1
    while opcao != 0:
        opcao = int(input(menu_logged))
        if opcao == 0 :
            sistema.deslogar() 
        if opcao == 1 :
            nome = input("Digite o nome do Time: ")
            sistema.criar_time(nome)
            #tela_time(sistema)
        if opcao == 2 :
            titulo = input("Digite o Nome do Quadro: ")
            sistema.criar_quadro(titulo)
            #tela_quadro(sistema)
        if opcao == 3 :
            quadros = sistema.listar_quadros()
            for quadro in quadros:
                print(quadro)
            titulo = input("Qual quadro deseja visualizar? (digite igual ao nome do quadro) ")
            if sistema.acessar_quadro(titulo):
                pass
                #tela_quadro(sistema)
            else :
                print("Quadro não existente ou não disponivel ao usuário atual")












menu_logged = """Bem vindo
O que deseja fazer?
1 - Criar Time
2 - Criar Quadro
3 - Acessar seus Quadros
4 - Acessar seus Times
0 - Deslogar

"""






if __name__ == '__main__':
    main()
