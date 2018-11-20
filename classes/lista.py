from classes.cartao import Cartao

class Lista:

    def __init__(self,id,titulo):
        self.id = id
        self.titulo = titulo
        self.cartoes = []

    def criar_cartao(self,id,titulo):
        cartao = Cartao(id,titulo)
        self.cartoes.append(cartao)
        return cartao

    def listar_cartoes(self):
        return self.cartoes

    def mover_cartao(self,id,titulo):
        cartao_movido = self.achar_cartao(titulo)
        if cartao_movido != None :
            index = self.cartoes.index(cartao_movido)
            self.cartoes.pop(index)
            self.cartoes.insert(id,cartao_movido)
            return True
        return False

    def adicionar_comentario(self,titulo,comentario):
        cartao_coment = self.achar_cartao(titulo)
        if cartao_coment != None :
            cartao_coment.adicionar_comentario(comentario)
            return True
        return False

    def adicionar_descricao(self,titulo,descricao):
        cartao_desc = self.achar_cartao(titulo)
        if cartao_desc != None :
            cartao_desc.adicionar_descricao(descricao)
            return True
        return False

    def adicionar_etiqueta(self,titulo,etiqueta):
        cartao_desc = self.achar_cartao(titulo)
        if cartao_desc != None :
            cartao_desc.adicionar_etiqueta(etiqueta)
            return True
        return False

    def mostrar_cartao(self,titulo):
        cartao = self.achar_cartao(titulo)
        if cartao != None :
            return True,cartao.dados()



    def achar_cartao(self,titulo):
        cartao_achado = None
        for cartao in self.cartoes:
            if cartao.titulo == titulo:
                cartao_achado = cartao
                break
        return cartao_achado

    def __str__(self):
        return "Titulo : %s" %self.titulo
