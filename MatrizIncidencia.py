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
			posicaoVertice = self.vertices.index(vertice)
			for i in range (len(self.arestas)):
				ehLoop = True
				if(self.matriz[i][posicaoVertice] != '0'):
					for j in self.vertices:
						posicaoJ = self.vertices.index(j)
						if(self.matriz[i][posicaoJ] != '0') and (posicaoJ != posicaoVertice):
							ehLoop = False
							if(str(j) not in vizinhos):
								vizinhos.append(str(j))
					if(ehLoop):
						vizinhos.append(str(vertice))
			vizinhos.sort()
			return vizinhos
		else:
			return "O vertice escolhido não pertence ao grafo"

	def obtemSuc(self,vertice):
		if(self.verificacaoParametrosObtem(vertice)):
			listaSuc = []
			posicaoVertice = self.vertices.index(vertice)
			for i in range(len(self.arestas)):
				ehLoop = True
				if(self.matriz[i][posicaoVertice] > '0'):
					for j in self.vertices:
						posicaoJ = self.vertices.index(j)
						if(self.matriz[i][posicaoJ] < '0') and (posicaoJ != posicaoVertice):
							ehLoop = False
							listaSuc.append(str(j))
					if(ehLoop):
						listaSuc.append(str(vertice))
			return listaSuc
		else:
			return "O vertice escolhido não pertence ao grafo"

	def obtemPred(self, vertice):
		if(self.verificacaoParametrosObtem(vertice)):
			listaPred = []
			posicaoVertice = self.vertices.index(vertice)
			for i in range(len(self.arestas)):
				if(self.matriz[i][posicaoVertice] < '0'):
					for j in self.vertices:
						posicaoJ = self.vertices.index(j)
						if(self.matriz[i][posicaoJ] > '0') and (posicaoJ != posicaoVertice):
							listaPred.append(str(j))
				elif(self.matriz[i][posicaoVertice] > '0'):
					ehLoop = True
					for j in self.vertices:
						posicaoJ = self.vertices.index(j)
						if(self.matriz[i][posicaoJ] != '0') and (posicaoJ != posicaoVertice):
							ehLoop = False
					if(ehLoop):
						listaPred.append(str(vertice))
					
			return listaPred
		else:
			return "O vertice escolhido não pertence ao grafo"


	def verificacaoParametrosObtem(self, vertice):
		qntVertices = len(self.vertices)
		if(not vertice in self.vertices[0:qntVertices]):
			return False
		else:
			return True

