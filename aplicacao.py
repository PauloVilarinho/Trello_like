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



def iniciar_sessao(sistema):
    print(menu_logged, format(sistema.usuario_logado.nome))







start = """T)tttttt R)rrrrr  E)eeeeee L)       L)        O)oooo
   T)    R)    rr E)       L)       L)       O)    oo
   T)    R)  rrr  E)eeeee  L)       L)       O)    oo
   T)    R) rr    E)       L)       L)       O)    oo
   T)    R)   rr  E)       L)       L)       O)    oo
   T)    R)    rr E)eeeeee L)llllll L)llllll  O)oooo
                                                        """
menu_unlogged = """"Bem vindo ao Trello
digite a opção que deseja usuar
1 - Criar Conta
2 - Acessar Conta
0 - Sair do Programa"""

menu_logged = "Bem vindo {} \n "\
"O que deseja fazer hoje?"






if __name__ == '__main__':
    main()
