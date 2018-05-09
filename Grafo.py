#Classe que representa um grafo lido do arquivo
class Grafo(object):
	def __init__(self,listaVertices, listaArestas, ehDirecionado, ehPonderado):
		self.vertices = listaVertices
		listaArestas.sort()		
		self.arestas = listaArestas
		self.direcionado = ehDirecionado
		self.ponderado = ehPonderado


