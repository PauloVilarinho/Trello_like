class Banco_Dados :

    def __init__(self,usuarios= [], times = [],quadros = [],listas = [],cartoes = []):
        self.usuarios = usuarios
        self.times = times
        self.quadros = quadros
        self.listas = listas
        self.cartoes = cartoes

    def quantidade_usuarios(self):
        return len(self.usuarios)

    def quantidade_times(self):
        return len(self.times)

    def quantidade_quadros(self):
        return len(self.quadros)

    def quantidade_listas(self):
        return len(self.listas)

    def quantidade_cartoes(self):
        return len(self.cartoes)

    def armazenar_usuario(self,usuario):
        self.usuarios.append(usuario)

    def armazenar_time(self,time):
        self.times.append(time)

    def armazenar_quadro(self,quadro):
        self.quadros.append(quadro)

    def armazenar_lista(self,lista):
        self.listas.append(lista)

    def armazenar_cartao(self,cartao):
        self.cartoes.append(cartao)
