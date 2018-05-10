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
			posicaoVertice = self.vertices.index(vertice)
			for i in (self.vertices):
				posicaoI = self.vertices.index(i)
				if((self.matriz[posicaoVertice][posicaoI] != '0') or (self.matriz[posicaoI][posicaoVertice] != '0')):
					vizinhos.append(str(i))
			return vizinhos
		else:
			return "O vertice escolhido não pertence ao grafo"

	def obtemSuc(self,vertice):
		if(self.verificacaoParametrosObtem(vertice)):
			listaSuc = []
			indice = self.vertices.index(vertice)
			for i in range(len(self.vertices)):
				posicaoI = self.vertices.index(i)
				if(self.matriz[indice][posicaoI] != '0'):
					listaSuc.append(str(i))
			return listaSuc
		else:
			return "O vertice escolhido não pertence ao grafo"

	def obtemPred(self, vertice):
		if(self.verificacaoParametrosObtem(vertice)):
			listaPred = []
			indice = self.vertices.index(vertice)
			for i in range (len(self.vertices)):
				posicaoI = self.vertices.index(i)
				if((self.matriz[posicaoI][indice] != '0')):
					listaPred.append(str(i))
			return listaPred
		else:	
			return "O vertice escolhido não pertence ao grafo"
	
	def ehVizinho(self, vertice1 , vertice2):
		if(self.verificacaoParametrosEh(vertice1 , vertice2)):
			indice1 = self.vertices.index(vertice1)
			indice2 = self.vertices.index(vertice2)
			if((self.matriz[indice1][indice2] != '0') or (self.matriz[indice2][indice1] != '0')):	
				return True		
			else:
				return False
		else:
			return "O vertice escolhido não pertence ao grafo"

	def ehPredecessor(self, vertice1, vertice2):
		if(self.verificacaoParametrosEh(vertice1, vertice2)):
			indice1 = self.vertices.index(vertice1)
			indice2 = self.vertices.index(vertice2)
			if(self.matriz[indice2][indice1] != '0'):
				return True
			else:
				return False
		else:
			return "O vertice escolhido não pertence ao grafo"

	def ehSucessor(self, vertice1, vertice2):
		if(self.verificacaoParametrosEh(vertice1, vertice2)):
			indice1 = self.vertices.index(vertice1)
			indice2 = self.vertices.index(vertice2)
			if(self.matriz[indice1][indice2] != '0'):
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

	def delVertice(self,vertice):
		if(self.verificacaoParametrosObtem(vertice)):
			i = 0
			while(i < len(self.arestas)):
				if((str(vertice) in self.arestas[i][0:2])):
					print("Vertice: ", vertice)
					print(self.arestas[i][0])
					print(self.arestas[i][1])
					self.arestas.pop(i)
					i = i - 1
				i = i + 1
			indice = self.vertices.index(vertice)
			self.vertices.pop(indice)
			self.matriz.pop(indice)
			for i in range (len(self.vertices)):
				self.matriz[i].pop(indice)
		
		else:
			return "O vertice escolhido não pertence ao grafo"
























