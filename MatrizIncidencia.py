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
		#FAZER CASO PARA VER SE O GRAFO E' DIRECIONADO
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
		#FAZER CASO PARA VER SE O GRAFO E' DIRECIONADO
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

	def ehVizinho(self, vertice1 , vertice2):
		if(self.verificacaoParametrosEh(vertice1 , vertice2)):
			indice1 = self.vertices.index(vertice1)
			indice2 = self.vertices.index(vertice2)
			ehVizinho = False
			for i in range(len(self.arestas)):
				if (self.matriz[i][indice2] != '0') and (self.matriz[i][indice1] != '0'):
					print("Linha: ",i, self.matriz[i][indice1],self.matriz[i][indice2])
					ehVizinho = True		
			return ehVizinho
		else:
			return "O vertice escolhido não pertence ao grafo"

	def ehPredecessor(self, vertice1, vertice2):
		#FAZER CASO PARA VER SE O GRAFO E' DIRECIONADO
		if(self.verificacaoParametrosEh(vertice1 , vertice2)):
			indice1 = self.vertices.index(vertice1)
			indice2 = self.vertices.index(vertice2)
			ehPred = False
			for i in range(len(self.arestas)):
				if (self.matriz[i][indice2] > '0') and (self.matriz[i][indice1] < '0'):
					print("Linha: ",i, self.matriz[i][indice1],self.matriz[i][indice2])
					ehPred = True	
				#fazer caso do loop	
			return ehPred
		else:
			return "O vertice escolhido não pertence ao grafo"

	def ehSucessor(self, vertice1, vertice2):
		#FAZER CASO PARA VER SE O GRAFO E' DIRECIONADO
		if(self.verificacaoParametrosEh(vertice1 , vertice2)):
			indice1 = self.vertices.index(vertice1)
			indice2 = self.vertices.index(vertice2)
			ehVizinho = False
			for i in range(len(self.arestas)):
				if (self.matriz[i][indice2] < '0') and (self.matriz[i][indice1] > '0'):
					print("Linha: ",i, self.matriz[i][indice1],self.matriz[i][indice2])
					ehVizinho = True	
				#fazer caso do loop

			return ehVizinho
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

	def delAresta(self, vertice1, vertice2):
		for i in range(len(self.arestas)):
			if(str(vertice1) == self.arestas[i][0] and str(vertice2) == self.arestas[i][1]):
				self.arestas.pop(i)
				print("OIII")
				return
	#ver como faz void, nao ta funcionando

''' def delVertice(self,vertice):
		if(self.verificacaoParametrosObtem(vertice)):
			i = 0
			while(i < len(self.arestas)):
				if((str(vertice) in self.arestas[i][0:2])):
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
	
	def delAresta(self,vertice1, vertice2):
		if(self.verificacaoParametrosEh(vertice1,vertice2)):
			tem = False
			i = 0
			while(i < len(self.arestas)):
				if((str(vertice1) in self.arestas[i][0]) and (str(vertice2) in self.arestas[i][1])):
					self.arestas.pop(i)
					i = i - 1
					tem = True
				i = i + 1					
			if(not tem):
				print ("A aresta escolhida não pertence ao grafo")

		else:
			print("A aresta escolhida não pertence ao grafo")
'''
