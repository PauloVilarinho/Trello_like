from classes.usuario import Usuario
from classes.time import Time
from classes.quadros import Quadro
from classes.dados import Banco_Dados

class Sistema:


    def __init__ (self):
        self.banco = Banco_Dados()
        self.usuario_logado = None
        self.time_usando = None
        self.quadro_usando = None

    def criar_usuario(self,nome,email,senha):
        #TODO validação de nome e email disponiveis
        usuario = Usuario(nome,self.banco.quantidade_usuarios(),email,senha)
        self.banco.armazenar_usuario(usuario)
        self.usuario_logado = usuario
        return True

    def logar_usuario(self,email,senha):
        for usuario in self.banco.usuarios :
            if usuario.validacao(email,senha):
                self.usuario_logado = usuario
                return True
        return False

    def deslogar(self):
        self.usuario_logado = None

    def criar_time(self,nome):
        time = Time(self.banco.quantidade_times(),self.usuario_logado,nome)
        self.banco.armazenar_time(time)
        self.time_usando = time

    def criar_quadro(self,titulo):
        quadro = Quadro(self.banco.quantidade_quadros,titulo,self.usuario_logado)
        self.banco.armazenar_quadro(quadro)
        self.usuario_logado.adicionar_quadros(quadro)
        self.quadro_usando = quadro

    def listar_times(self):
        times_parte = []
        for time in self.banco.times :
            if self.usuario_logado in time.usuarios :
                times_parte.append(time)
        return times_parte

    def listar_quadros(self):
        times_parte = self.listar_times()
        quadros = self.usuario_logado.quadros
        for time in times_parte:
            quadros.append(time.quadros)
        return quadros

    def apagar_quadro(self,titulo):
        for quadro in self.usuario_logado.quadros :
            if quadro.titulo == titulo:
                return self.usuario_logado.delete_quadro(quadro)
        return False

    def acessar_quadro(self,titulo):
        for quadro in self.listar_quadros():
            if quadro.titulo == titulo :
                self.quadro_usando = quadro
                return True
        return False

    def acessar_time(self,titulo):
        for time in self.listar_times():
            if time.titulo == titulo :
                self.time_usando = time
                return True
        return False

    def sair_quadro(self):
        self.quadro_usando = None

    def adcionar_lista(self,titulo):
        lista = self.quadro_usando.adcionar_lista(self.banco.quantidade_listas,titulo)
        self.banco.armazenar_lista(lista)
        self.lista_usando = lista

    def apagar_lista(self,titulo):
        for lista in self.quadro_usando.listar_listas():
            if lista.titulo == titulo:
                return self.quadro_usando.apagar_lista(lista)
        return False

    def mover_lista(self,titulo,index):
        return self.quadro_usando.mover_lista(titulo,index)

    def listar_listas(self):
        return self.quadro_usando.listar_listas()

    def acessar_lista(self,titulo):
        if self.quadro_usando.acessar_lista(titulo)[0]:
            self.lista_usando = self.quadro_usando.acessar_lista(titulo)[1]
            return True
        return False

    def sair_lista(self):
        self.lista_usando = None

    def criar_cartao(self,titulo):
         cartao = self.lista_usando.criar_cartao(self.banco.quantidade_cartoes,titulo)
         self.banco.armazenar_cartao(cartao)

    def listar_cartoes(self):
        return self.lista_usando.listar_cartoes()

    def mover_cartao(self,titulo_lista,titulo):
        if self.quadro_usando.acessar_lista(titulo_lista)[0]:
            lista = self.quadro_usando.acessar_lista(titulo_lista)[1]
            cartao = self.lista_usando.apagar_cartao(titulo)
            if cartao != None:
                lista.adcionar_cartao(cartao)
                return True
            else :
                return False
        else :
            return False

    def apagar_cartao(self,titulo):
        cartao = self.lista_usando.apagar_cartao(titulo)
        if cartao != None :
            return True
        else :
            return False

    def adicionar_descricao(self,titulo,descricao):
        if self.lista_usando.adicionar_descricao(titulo,descricao):
            return True
        else:
            return False

    def adicionar_comentario(self,titulo,comentario):
        if self.lista_usando.adicionar_comentario(titulo,comentario):
            return True
        else:
            return False

    def adicionar_etiqueta(self,titulo,etiqueta):
        if self.lista_usando.adicionar_etiqueta(titulo,etiqueta):
            return True
        else:
            return False

    def mostrar_cartao(self,titulo):
        return self.lista_usando.mostrar_cartao(titulo)
