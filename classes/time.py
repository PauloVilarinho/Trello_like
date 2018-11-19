class Time:

    def __init__ (self,id,lider,titulo):
        self.id = id
        self.titulo = titulo
        self.lider = lider
        self.usuarios = [lider]
        self.quadros = []

    def __str__(self):
        return "{'id':%d; 'titulo':%s; 'lider':%d; 'usuarios':%s; 'quadros':%s}" %(self.id,self.titulo,self.lides,str(self.usuarios),str(self.quadros))
