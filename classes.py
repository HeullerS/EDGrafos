from funcoes import *
#Classe que representa um grafo lido do arquivo
class Grafo(object):
	def __init__(self,listaVertices, listaArestas, ehDirecionado, ehPonderado):
		self.vertices = listaVertices
		listaArestas.sort()		
		self.arestas = listaArestas
		self.direcionado = ehDirecionado
		self.ponderado = ehPonderado

class MatrizAdj(Grafo):
	def __init__(self, listaVertices, listaArestas, ehDirecionado, ehPonderado, grafos):
		Grafo.__init__(self,listaVertices, listaArestas, ehDirecionado, ehPonderado)
		self.matriz = geraMA(grafo)

	def obtemVizinhos(vertice):
		if(verificacaoParametrosObtem(vertice)):
			vizinhos = []
			for i in range (len(self.vertices)):
				if((self.matriz[vertice][i] != '0') or (self.matriz[i][vertice] != '0')):
					vizinhos.append(str(i))
			return vizinhos
		else:
			return "O vertice escolhido não pertence ao grafo"
	
	def verificacaoParametrosObtem(vertice):
		qntVertices = len(self.vertices)
		if(not vertice in self.vertices[0:qntVertices]):
			return False
		else:
			return True

