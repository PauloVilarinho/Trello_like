from usuario import Usuario

class Sistema:

    self.usuarios = []
    self.times = []


    def criar_usuario(self,nome,email,senha):
        usuario = Usuario(nome,email,senha)
        self.usuarios.append(usuario)
