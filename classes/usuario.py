

class Usuario:

    def __init__(self,id,nome,email,senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.quadros = []

    def validacao(self,email,senha):
        if self.email == email and self.senha == senha :
            return True
        else :
            return False
