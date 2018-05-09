from funcoes import *
#Classe que representa um grafo lido do arquivo
class Grafo(object):
	def __init__(self, listaVertices, listaArestas, ehDirecionado, ehPonderado):
		self.verticesObj = []	
		self.vertices = listaVertices
		listaArestas.sort()	
		self.arestas = listaArestas
		self.direcionado = ehDirecionado
		self.ponderado = ehPonderado
		self.quantidadeVertices = len(listaVertices)


	def setVertices(self, listaV):
		self.verticesObj = listaV

class Vertice(object):
	def __init__(self, valor, grafo):
		self.valor = valor
		self.grafo = grafo
