
class Cartao:

    def __init__(self,id,titulo,descricao = "",data = "",etiquetas = [],comentarios =[]):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.etiquetas = etiquetas
        self.comentarios = comentarios

    def __str__(self):
        return "{'id':%d; 'titulo':%s; 'descricao':%s; 'data':%s; 'etiquetas':%s; 'comentarios':%s}" %(self.id,self.titulo,self.descricao,self.data,str(self.etiquetas),str(self.comentarios))
        
