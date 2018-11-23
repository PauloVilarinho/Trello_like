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
        elif opcao == "2":
            email = input("Digite o email do Usuário:  ")
            senha = input("Digite a senha do Usuário:  ")
            if sistema.logar_usuario(email,senha):
                iniciar_sessao(sistema)
            else :
                print("email ou senha invalidas")
        elif opcao != "0" :
            print("Operação não existente")
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
        # elif opcao == "1" :
        #     nome = input("Digite o nome do Time: ")
        #     sistema.criar_time(nome)
        #     #tela_time(sistema)
        elif opcao == "1" :
            titulo = input("Digite o Nome do Quadro: ")
            sistema.criar_quadro(titulo)
        elif opcao == "2" :
            quadros = sistema.listar_quadros()
            for quadro in quadros:
                print(quadro)
            titulo = input("Qual quadro deseja visualizar? (digite igual ao nome do quadro) ")
            if sistema.acessar_quadro(titulo):
                tela_quadro(sistema)
            else :
                print("Quadro não existente ou não disponivel ao usuário atual")
        elif opcao == "3":
            quadros = sistema.listar_quadros()
            for quadro in quadros:
                print(quadro)
            titulo = input("Qual quadro deseja apagar? (digite igual ao nome do quadro) ")
            if sistema.apagar_quadro(titulo):
                print("Quadro apagado")
            else :
                print("Quadro não disponivel para você ou não existe")
        # elif opcao == "4" :
        #     times = sistema.listar_times()
        #     for time in times:
        #         print(time)
        #     titulo = input("Qual time deseja vizualizar? (digite igual ao nome do time) ")
        #     if sistema.acessar_time(titulo):
        #         pass
        #         #tela_time(sistema)
        #     else :
        #        print("Time não existente ou não disponivem ao usuário atual")
        else :
            print("Operação não existente")


menu_logged = """Bem vindo
O que deseja fazer?
1 - Criar Quadro
2 - Acessar seus Quadros
3 - Apagar Quadros
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
        elif opcao == "2" :
            titulo = input("Digite o nome da lista a ser movida: ")
            posicao = int(input("Para qual posição deseja mover  a lista?  "))
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
        elif opcao == "4" :
            listas = sistema.listar_listas()
            for lista in listas :
                print(lista)
            titulo = input("Digite o Nome da Lista a ser Apagada: ")
            if sistema.apagar_lista(titulo):
                print("Lista apagada com sucesso")
            else :
                print("Lista com esse nome não existe nesse quadro")
        else :
            print("Operação não existente")


menu_quadro = """O que deseja fazer?
1 - Adcionar lista
2 - Mover lista
3 - Acessar lista
4 - Apagar lista
0 - Sair do Quadro"""


def tela_lista(sistema):
    opcao = ""
    while opcao != "0":
        opcao = input(menu_lista)
        if opcao == "0" :
            sistema.sair_lista()
        elif opcao == "1" :
            titulo = input("Digite o titulo cartão: ")
            sistema.criar_cartao(titulo)
        elif opcao == "2":
            cartoes = sistema.listar_cartoes()
            for cartao in cartoes:
                print(cartao)
        elif opcao == "3":
            cartoes = sistema.listar_cartoes()
            for cartao in cartoes:
                print(cartao)
            titulo = input("Qual cartão voce quer mover?  ")
            listas = sistema.listar_listas()
            for lista in listas :
                print(lista)
            titulo_lista = input("para qual lista? ")
            if sistema.mover_cartao(titulo_lista,titulo):
                print("cartão movido com  sucesso")
            else :
                print("cartão não existe nessa lista,ou lista não existe")
        elif  opcao == "4":
            cartoes = sistema.listar_cartoes()
            for cartao in cartoes:
                print(cartao)
            titulo = input("Qual cartão voce quer deletar?  ")
            if sistema.apagar_cartao(titulo):
                print("cartão apagado com sucesso. ")
            else :
                print("cartão não existe nessa lista")
        elif opcao == "5":
            cartoes = sistema.listar_cartoes()
            for cartao in cartoes:
                print(cartao)
            titulo = input("Qual cartão voce quer descrever?  ")
            descricao = input("Qual descricao: ")
            if sistema.adicionar_descricao(titulo,descricao):
                print("operação com  sucesso")
            else :
                print("cartão não existe nessa lista")
        elif opcao == "6":
            cartoes = sistema.listar_cartoes()
            for cartao in cartoes:
                print(cartao)
            titulo = input("Qual cartão voce quer comentar?  ")
            comentario = input("Qual comentario: ")
            if sistema.adicionar_comentario(titulo,comentario):
                print("operação com  sucesso")
            else :
                print("cartão não existe nessa lista")
        elif opcao == "7":
            cartoes = sistema.listar_cartoes()
            for cartao in cartoes:
                print(cartao)
            titulo = input("Qual cartão voce quer etiquetar?  ")
            etiqueta = input("Qual etiqueta: ")
            if sistema.adicionar_etiqueta(titulo,etiqueta):
                print("operação com  sucesso")
            else :
                print("cartão não existe nessa lista")
        elif opcao == "8":
            cartoes = sistema.listar_cartoes()
            for cartao in cartoes:
                print(cartao)
            titulo = input("Qual cartão voce quer observar?  ")

            if sistema.mostrar_cartao(titulo)[0]:
                dados = sistema.mostrar_cartao(titulo)[1]
                print(dados)
                print("operação com  sucesso")
            else :
                print("cartão não existe nessa lista")
        else :
            print("Operação não existente")



menu_lista = """O que deseja fazer?
1 - Criar Cartão
2 - Listar Cartões
3 - Mover Cartão
4 - Apagar Cartão
5 - Adicionar Descrição
6 - Adicionar Comentarios
7 - Adicionar Etiqueta
8 - Visualizar dados do cartão
0 - Voltar para o Quadro
"""




if __name__ == '__main__':
    main()
