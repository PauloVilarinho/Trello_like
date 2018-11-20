class Lista:

    def __init__(self,id,titulo):
        self.id = id
        self.titulo = titulo
        self.cartoes = []

    def __str__(self):
        return "Titulo : %s" %self.titulo
