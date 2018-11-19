from classes.usuario import Usuario

class Sistema:


    def __init__ (self):
        self.usuarios = []
        self.times = []
        self.usuario_logado = None
        self.usuario_criados = 0
        self.times_criados = 0
        self.quadros_criados = 0
        self.listas_criadas = 0
        self.cartoes_criados = 0


    def criar_usuario(self,nome,email,senha):
        #TODO validação de nome e email disponiveis
        usuario = Usuario(nome,self.usuario_criados,email,senha)
        self.usuarios.append(usuario)
        self.usuario_logado = usuario
        self.usuario_criados += 1
        return True

    def logar_usuario(self,email,senha):
        for usario in self.usuarios :
            if usario.validacao(email,senha):
                self.usuario_logado = usuario
                return True
        return False
