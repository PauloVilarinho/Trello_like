from classes.lista import Lista

class Quadros:

    def __init__(self,titulo,membros):
        self.titulo = titulo
        self.tipo = "pa"
        self.membros = membros
        self.listas = [Lista("Em andamento"),Lista("A fazer"),Lista("Concluído")]
