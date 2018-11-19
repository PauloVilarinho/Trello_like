from classes.usuario import Usuario
from classes.dados import Banco_Dados

class Sistema:


    def __init__ (self):
        self.banco = Banco_Dados()
        self.usuario_logado = None

    def criar_usuario(self,nome,email,senha):
        #TODO validação de nome e email disponiveis
        usuario = Usuario(nome,self.banco.quantidade_usuarios,email,senha)
        self.banco.armazenar_usuario(usuario)
        self.usuario_logado = usuario
        self.usuario_criados += 1
        return True

    def logar_usuario(self,email,senha):
        for usario in self.banco.usuarios :
            if usario.validacao(email,senha):
                self.usuario_logado = usuario
                return True
        return False
