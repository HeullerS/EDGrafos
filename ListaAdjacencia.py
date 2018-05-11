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
		else:
			return "O vertice escolhido não pertence ao grafo"
			
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
		
		else:
			return "O vertice escolhido não pertence ao grafo"
	


	def ehVizinho(self, vertice1 , vertice2):
		if(self.verificacaoParametrosEh(vertice1 , vertice2)):
			

			vizinhosDeUm = self.obtemVizinhos(vertice1)
			vizinhosDeDois = self.obtemVizinhos(vertice2)
			print(vizinhosDeUm)
			print(vizinhosDeDois)
			
			ehVizinhos = False
			for i in vizinhosDeUm:
				if(str(vertice2) == i):
					ehVizinhos = True

			for i in vizinhosDeDois:
				if(str(vertice1) == i):
					ehVizinhos = True
			return ehVizinhos
		else:
			return "O vertice escolhido não pertence ao grafo"


	def ehPredecessor(self, vertice1 , vertice2):
		if(self.verificacaoParametrosEh(vertice1 , vertice2)):
			
			predecessoresDeUm = self.obtemPred(vertice1)
			ehPredec = False
			i = 0

			while(i < len(predecessoresDeUm) and ehPredec == False):
				if((str(vertice2) == predecessoresDeUm[i])):
					ehPredec = True
				else:
					ehPredec = False
				i = i + 1
				
			return ehPredec
		else:
			return "O vertice escolhido não pertence ao grafo"

	def ehSucessor(self, vertice1 , vertice2):
		if(self.verificacaoParametrosEh(vertice1 , vertice2)):
			sucessoresDeUm = self.obtemSuc(vertice1)
			ehSuces = False
			i = 0
			#while(ehSuces == False and i < len(sucessoresDeUm):
			while(i < len(sucessoresDeUm) and ehSuces == False):
				if((str(vertice2) == sucessoresDeUm[i])):
					ehSuces = True
				else:
					ehSuces = False
				i = i + 1
				
			return ehSuces
					
			

		else:
			return "O vertice escolhido não pertence ao grafo"

	
	def delVertice(self,vertice):
		if(self.verificacaoParametrosObtem(vertice)):
			i = 0
			while(i < len(self.arestas)):
				if((str(vertice) in self.arestas[i][0:2])):
					self.arestas.pop(i)
					i = i - 1
				i = i + 1
			del(self.lista[vertice])
			indice = self.vertices.index(vertice)
			self.vertices.pop(indice)
		
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
