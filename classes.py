from funcoes import *
#Classe que representa um grafo lido do arquivo
class Grafo(object):
	def __init__(self, listaArestas, ehDirecionado, ehPonderado, qntVertices):
		listaArestas.sort()
		self.vertices = []		
		self.arestas = listaArestas
		self.direcionado = ehDirecionado
		self.ponderado = ehPonderado
		self.quantidadeVertices = qntVertices

	def setVertices(self, listaV):
		self.vertices = listaV

class Vertice(object):
	def __init__(self, valor, grafo):
		self.valor = valor
		self.grafo = grafo
