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
			posicaoVertice = self.vertices.index(vertice)
			for i in (self.vertices):
				posicaoI = self.vertices.index(i)
				if((self.matriz[posicaoVertice][posicaoI] != '0') or (self.matriz[posicaoI][posicaoVertice] != '0')):
					vizinhos.append(str(i))
			return vizinhos
		else:
			return "O vertice escolhido não pertence ao grafo"


def verificacaoParametrosObtem(self, vertice):
		qntVertices = len(self.vertices)
		if(not vertice in self.vertices[0:qntVertices]):
			return False
		else:
			return True
