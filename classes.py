from funcoes import *
#Classe que representa um grafo lido do arquivo
class Grafo(object):
	def __init__(self, listaVertices, listaArestas, ehDirecionado, ehPonderado):	
		self.vertices = listaVertices
		listaArestas.sort()	
		self.arestas = listaArestas
		self.direcionado = ehDirecionado
		self.ponderado = ehPonderado
		self.quantidadeVertices = len(listaVertices)
		self.verticesObj = self.setVertices()


	def setVertices(self):
		listaVertices = []
		for i in range(self.quantidadeVertices):
			vertice = Vertice(str(i), self)
			listaVertices.append(vertice)
		
		return listaVertices
		

class Vertice(object):
	def __init__(self, valor, grafo):
		self.valor = valor
		self.grafo = grafo
