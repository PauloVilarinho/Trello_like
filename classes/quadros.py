from classes.lista import Lista

class Quadro:

    def __init__(self,id,titulo,membros,tipo = "pa",listas = [Lista("Em andamento"),Lista("A fazer"),Lista("Concluído")]):
        self.id = id
        self.titulo = titulo
        self.tipo = tipo
        self.membros = membros
        self.listas = listas


    def __str__(self):
        return "{'id':%d; 'titulo':%s; 'tipo':%s; 'membros':%s; 'listas':%s}" %(self.id,self.titutlo,self.tipo,str(self.membros),str(self.listas))
