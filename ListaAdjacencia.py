from Grafo import *
import funcoes
class ListaAdj(Grafo):
	def __init__(self, listaVertices, listaArestas, ehDirecionado, ehPonderado, grafo):
		Grafo.__init__(self,listaVertices, listaArestas, ehDirecionado, ehPonderado)
		self.grafo = grafo
		self.lista = funcoes.geraLA(grafo)

	def obtemVizinhos(self, vertice):
		if(self.verificacaoParametrosObtem(vertice)):
			sucessores = self.obtemSuc(vertice)
			predecessores = self.obtemPred(vertice)
			vizinhos = sucessores + predecessores
			vizinhos = list(set(vizinhos))
			vizinhos.sort()
			
			return vizinhos
			
	def obtemSuc(self, vertice):
		if(self.verificacaoParametrosObtem(vertice)):
			sucessores = []
			posicaoVertice = self.lista[vertice]
			
			contador = 0
			for i in posicaoVertice:
				sucessores.append(posicaoVertice[contador][0])
				verticeLigado = posicaoVertice[contador][0]
				contador += 1
		
		
		return sucessores

	def obtemPred(self, vertice):
		if(self.verificacaoParametrosObtem(vertice)):
			predecessores = []
			#posicaoVertice = self.lista[vertice]
			
			#contador = 0
			for i in self.lista:
				posicaoI = self.lista[i]
				for j in range(len(posicaoI)):
					if(posicaoI[j][0] == str(vertice)):
						predecessores.append(str(i))
		
		return predecessores
	
	
		
			
	def verificacaoParametrosObtem(self, vertice):
			qntVertices = len(self.vertices)
			if(not vertice in self.vertices[0:qntVertices]):
				return False
			else:
				return True
