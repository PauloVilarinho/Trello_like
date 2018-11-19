from classes.lista import Lista

class Quadros:

    def __init__(self,id,titulo,membros):
        self.id = id
        self.titulo = titulo
        self.tipo = "pa"
        self.membros = membros
        self.listas = [Lista("Em andamento"),Lista("A fazer"),Lista("Concluído")]
