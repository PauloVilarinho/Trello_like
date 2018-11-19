from classes.usuario import Usuario

class Sistema:


    def __init__ (self):
        self.usuarios = []
        self.times = []
        self.usuario_logado = None


    def criar_usuario(self,nome,email,senha):
        #TODO validação de nome e email disponiveis
        usuario = Usuario(nome,email,senha)
        self.usuarios.append(usuario)
        self.usuario_logado = usuario
        return True

    def logar_usuario(self,email,senha):
        for usario in self.usuarios :
            if usario.validacao(email,senha):
                self.usuario_logado = usuario
                return True
        return False
