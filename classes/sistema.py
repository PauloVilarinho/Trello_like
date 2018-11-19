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
        for usario in self.banco.usuarios :
            if usario.validacao(email,senha):
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
        self.usuario_logado.quadros.append(quadro)
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

    def acessar_quadro(self,titulo):
        for quadro in self.listar_quadros():
            if quadro.titulo == titulo :
                self.quadro_usando = quadro
                return True
        return False
