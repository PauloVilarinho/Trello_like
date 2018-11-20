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

    def listar_listas(self):
        return self.listas

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

    def acessar_lista(self,titulo):
        lista_acessada = None
        for lista in self.listas:
            if lista.titulo == titulo:
                lista_acessada = lista
                return True,lista_acessada
        return False,None


    def __str__(self):
        return "Quadro : %s" %self.titulo
