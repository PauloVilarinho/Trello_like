

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

    def adicionar_quadros(self,quadro):
        self.quadros.append(quadro)

    def delete_quadro(self,quadro):
        if quadro in self.quadros:
            index = self.quadros.index(quadro)
            self.quadros.pop(index)
            return True
        else :
            return False
