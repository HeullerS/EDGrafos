from Grafo import *
import funcoes
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

	def obtemSuc(self,vertice):
		if(self.verificacaoParametrosObtem(vertice)):
			listaSuc = []
			for i in range(len(self.vertices)):
				if(self.matriz[vertice][i] != '0'):
					listaSuc.append(i)
			return listaSuc
		else:
			return "O vertice escolhido não pertence ao grafo"

	def obtemPred(self, vertice):
		if(self.verificacaoParametrosObtem(vertice)):
			listaPred = []
			for i in range (len(self.vertices)):
				if((self.matriz[i][vertice] != '0')):
					listaPred.append(i)
			return listaPred
		else:	
			return "O vertice escolhido não pertence ao grafo"
	
	def ehVizinho(self, vertice1 , vertice2):
		if(self.verificacaoParametrosEh(vertice1 , vertice2)):
			if((self.matriz[vertice1][vertice2] != '0') or (self.matriz[vertice2][vertice1] != '0')):	
				return True		
			else:
				return False
		else:
			return "O vertice escolhido não pertence ao grafo"

	def ehPredecessor(self, vertice1, vertice2):
		if(self.verificacaoParametrosEh(vertice1, vertice2)):
			if(self.matriz[vertice2][vertice1] != '0'):
				return True
			else:
				return False
		else:
			return "O vertice escolhido não pertence ao grafo"

	def ehSucessor(self, vertice1, vertice2):
		if(self.verificacaoParametrosEh(vertice1, vertice2)):
			if(self.matriz[vertice1][vertice2] != '0'):
				return True
			else:
				return False
		else:
			return "O vertice escolhido não pertence ao grafo"
	
	def verificacaoParametrosObtem(self, vertice):
		qntVertices = len(self.vertices)
		if(not vertice in self.vertices[0:qntVertices]):
			return False
		else:
			return True

	def verificacaoParametrosEh(self, vertice1, vertice2):
		qntVertices = len(self.vertices)
		if((not vertice1 in self.vertices[0:qntVertices]) or (not vertice2 in self.vertices[0:qntVertices])):
			return False
		else:
			return True
