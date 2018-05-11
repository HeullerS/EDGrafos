from Grafo import *
import funcoes
class ListaAdj(Grafo):
	def __init__(self, listaVertices, listaArestas, ehDirecionado, ehPonderado, grafo):
		Grafo.__init__(self,listaVertices, listaArestas, ehDirecionado, ehPonderado)
		self.grafo = grafo
		self.lista = funcoes.geraLA(grafo)

	def obtemVizinhos(self, vertice):
		if(self.verificacaoParametrosObtem(vertice)):
			vizinhos = []
			posicaoVertice = self.lista[vertice]
			
			print(posicaoVertice)
			contador = 0
			for i in posicaoVertice:
				print(posicaoVertice[contador][0])
				vizinhos.append(posicaoVertice[contador][0])
				contador += 1
		return vizinhos
			
	def verificacaoParametrosObtem(self, vertice):
			qntVertices = len(self.vertices)
			if(not vertice in self.vertices[0:qntVertices]):
				return False
			else:
				return True
