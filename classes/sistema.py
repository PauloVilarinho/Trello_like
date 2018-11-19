from classes.usuario import Usuario
from classes.time import Time
from classes.dados import Banco_Dados

class Sistema:


    def __init__ (self):
        self.banco = Banco_Dados()
        self.usuario_logado = None
        self.time_usando = None

    def criar_usuario(self,nome,email,senha):
        #TODO validação de nome e email disponiveis
        usuario = Usuario(nome,self.banco.quantidade_usuarios,email,senha)
        self.banco.armazenar_usuario(usuario)
        self.usuario_logado = usuario
        return True

    def logar_usuario(self,email,senha):
        for usario in self.banco.usuarios :
            if usario.validacao(email,senha):
                self.usuario_logado = usuario
                return True
        return False

    def criar_time(self,nome):
        time = Time(self.banco.quantidade_times,nome)
        self.banco.armazenar_time(time)
