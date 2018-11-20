
class Cartao:

    def __init__(self,id,titulo,descricao = "",data = "",etiquetas = [],comentarios =[]):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.data = data
        self.etiquetas = etiquetas
        self.comentarios = comentarios
        self.arquivado = False

    def dados(self):
        dados = ""
        dados += "Titulo : %s \n" %self.titulo
        dados += "Descrição : %s\n" %self.descricao
        dados += "Etiquetas : "
        for etiqueta in self.etiquetas :
            dados += "%s \n" %etiqueta
        dados += "Comentarios : "
        for comentario in self.comentarios :
            dados += "%s \n" %comentario

        return dados

    def adicionar_descricao(self,descricao):
        self.descricao = descricao

    def adicionar_data(self,data):
        self.data = data

    def adicionar_etiqueta(self,etiqueta):
        self.etiquetas.append(etiqueta)

    def adicionar_comentario(self,comentario):
        self.comentarios.append(comentario)

    def arquivar(self):
        self.arquivado = True

    def desarquivar(self):
        self.desarquivado = True


    def __str__(self):
        return "Cartão : %s \nDescrição : %s" %(self.titulo,self.descricao)
