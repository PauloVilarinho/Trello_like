class Time:

    def __init__ (self,id,lider,titulo):
        self.id = id
        self.titulo = titulo
        self.lider = lider
        self.usuarios = [lider]
        self.quadros = []

    def __str__(self):
        return "Time : %s" %self.titulo
