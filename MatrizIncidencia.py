from Grafo import *
import funcoes
class MatrizInc(object):
	def __init__(self, listaVertices, listaArestas, ehDirecionado, ehPonderado, grafo):
		Grafo.__init__(self,listaVertices, listaArestas, ehDirecionado, ehPonderado)
		self.grafo = grafo
		self.matriz = funcoes.geraMI(grafo)

	def obtemVizinhos(self, vertice):
		if(self.verificacaoParametrosObtem(vertice)):
			vizinhos = []
			listaJaInseridos = []
			for i in range (len(self.arestas)):
				ehLoop = True
				if(self.matriz[i][vertice] != '0'):
					for j in range(len(self.vertices)):
						if(self.matriz[i][j] != '0') and (j != vertice):
							ehLoop = False
							if(str(j) not in vizinhos):
								vizinhos.append(str(j))
					if(ehLoop):
						vizinhos.append(str(vertice))
			vizinhos.sort()
			return vizinhos
		else:
			return "O vertice escolhido não pertence ao grafo"
	
	def verificacaoParametrosObtem(self, vertice):
		qntVertices = len(self.vertices)
		if(not vertice in self.vertices[0:qntVertices]):
			return False
		else:
			return True
