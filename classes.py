from funcoes import *
#Classe que representa um grafo lido do arquivo
class Grafo(object):
	def __init__(self,listaVertices, listaArestas, ehDirecionado, ehPonderado):
		self.vertices = listaVertices
		self.arestas = listaArestas
		self.direcionado = ehDirecionado
		self.ponderado = ehPonderado
