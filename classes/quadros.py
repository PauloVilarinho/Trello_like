from classes.lista import Lista

class Quadro:

    def __init__(self,id,titulo,membros,tipo = "pa",listas=[]):
        self.id = id
        self.titulo = titulo
        self.tipo = tipo
        self.membros = membros
        self.listas = listas

    def adcionar_lista(self,id,titulo):
        lista = Lista(id,titulo)
        self.listas.append(lista)
        return lista

    def mover_lista(self,titulo,id):
        lista_movida = None
        for lista in self.listas:
            if lista.titulo == titulo:
                lista_movida = lista
                break
        if lista_movida == None :
            return False
        index = self.listas.index(lista_movida)
        self.listas.pop(index)
        self.listas.insert(id,lista_movida)
        return True


    def __str__(self):
        return "Quadro : %s" %self.titulo
