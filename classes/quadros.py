
class Quadro:

    def __init__(self,id,titulo,membros,tipo = "pa",listas=[]):
        self.id = id
        self.titulo = titulo
        self.tipo = tipo
        self.membros = membros
        self.listas = listas


    def __str__(self):
        return "Quadro : %s" %self.titulo
