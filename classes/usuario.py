

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

    def __str__(self):
        return "{'id':%d; 'nome':%s; 'email':%s; 'senha':%s; 'quadros':%s }" %(self.id,self.nome,self.email,self.senha,str(self.quadros))
