import funcoes
#Classe que representa um grafo lido do arquivo
class Grafo(object):
	def __init__(self,listaVertices, listaArestas, ehDirecionado, ehPonderado):
		self.vertices = listaVertices
		listaArestas.sort()		
		self.arestas = listaArestas
		self.direcionado = ehDirecionado
		self.ponderado = ehPonderado

class MatrizAdj(Grafo):
	def __init__(self, listaVertices, listaArestas, ehDirecionado, ehPonderado, grafo):
		Grafo.__init__(self,listaVertices, listaArestas, ehDirecionado, ehPonderado)
		self.grafo = grafo
		self.matriz = funcoes.geraMA(grafo)

	def obtemVizinhos(self, vertice):
		if(self.verificacaoParametrosObtem(vertice)):
			vizinhos = []
			for i in range (len(self.vertices)):
				if((self.matriz[vertice][i] != '0') or (self.matriz[i][vertice] != '0')):
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

