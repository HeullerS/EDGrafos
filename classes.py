from funcoes import *
#Classe que representa um grafo lido do arquivo
class Grafo(object):
	def __init__(self, arq):
		self.vertices = listarVertices(arq)
		self.arestas = listarArestas(arq)
		self.direcionado = ehDirecionado(arq)
		self.ponderado = ehPonderado(arq)
