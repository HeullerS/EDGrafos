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
			posicaoVertice = self.vertices.index(vertice) # a posicão do vértice será dada de acordo com seu valor
			for i in (self.vertices): #percorre a linha do vértice na matriz para achar as suas ligações  
				posicaoI = self.vertices.index(i) 
				if((self.matriz[posicaoVertice][posicaoI] != '0') or (self.matriz[posicaoI][posicaoVertice] != '0')): #na implementação foi considerado que em um grafo direcionado, se A possui um caminho até B, e B não possui caminho até A, e vice-versa, ambos continuam sendo vizinhos
					vizinhos.append(str(i)) #se foi encontrado uma aresta que liga o vértice da entrada a outro,  esse é adicionado a lista de vizinhos.
			return vizinhos
		else:
			return "O vertice escolhido não pertence ao grafo"

	def obtemSuc(self,vertice):
		if(self.verificacaoParametrosObtem(vertice)):
			listaSuc = []
			indice = self.vertices.index(vertice) # a posicão do vértice será dada de acordo com seu valor
			for i in range(len(self.vertices)):
				posicaoI = self.vertices.index(i)
				if(self.matriz[indice][posicaoI] != '0'): #percorre-se a linha do vértice na matriz e se houver uma ligacao de "vertice" para outro vértice, esse é adicionado à lista de sucessores.
					listaSuc.append(str(i))
			return listaSuc
		else:
			return "O vertice escolhido não pertence ao grafo"

	def obtemPred(self, vertice):
		if(self.verificacaoParametrosObtem(vertice)):
			listaPred = []
			indice = self.vertices.index(vertice) # a posicão do vértice será dada de acordo com seu valor
			for i in range (len(self.vertices)):
				posicaoI = self.vertices.index(i)
				if((self.matriz[posicaoI][indice] != '0')): # aqui faz o oposto, percorre-se a coluna na matriz a fim de achar o predecessor. Se houver um vértice que liga ao "vertice" de entrada, esse será seu predecessor
					listaPred.append(str(i))
			return listaPred
		else:	
			return "O vertice escolhido não pertence ao grafo"
	
	def ehVizinho(self, vertice1 , vertice2):
		if(self.verificacaoParametrosEh(vertice1 , vertice2)):
			indice1 = self.vertices.index(vertice1)
			indice2 = self.vertices.index(vertice2)
			if((self.matriz[indice1][indice2] != '0') or (self.matriz[indice2][indice1] != '0')):	#verifica-se em duas posições
				return True		
			else:
				return False
		else:
			return "O vertice escolhido não pertence ao grafo"

	def ehPredecessor(self, vertice1, vertice2):
		if(self.verificacaoParametrosEh(vertice1, vertice2)):
			indice1 = self.vertices.index(vertice1)
			indice2 = self.vertices.index(vertice2)
			if(self.matriz[indice2][indice1] != '0'): #verifica se o vértice 2 possui alguma aresta com o vértice 1, caso afirmativo o vértice 2 é predecessor do vértice 1
				return True
			else:
				return False
		else:
			return "O vertice escolhido não pertence ao grafo"

	def ehSucessor(self, vertice1, vertice2):
		if(self.verificacaoParametrosEh(vertice1, vertice2)):
			indice1 = self.vertices.index(vertice1)
			indice2 = self.vertices.index(vertice2)
			if(self.matriz[indice1][indice2] != '0'): #verifica se o vértice 1 possui alguma aresta com o vértice 2, caso afirmativo o vértice 2 é sucessor do vértice 1
				return True
			else:
				return False
		else:
			return "O vertice escolhido não pertence ao grafo"
	
	def verificacaoParametrosObtem(self, vertice): #função que verifica se o vértice passado como parâmetro está dentro dos vértices do grafo.
		qntVertices = len(self.vertices)
		if(not vertice in self.vertices[0:qntVertices]):
			return False
		else:
			return True

	def verificacaoParametrosEh(self, vertice1, vertice2): #função que verifica se os vértices passados como parâmetro estão dentro dos vértices do grafo.
		qntVertices = len(self.vertices)
		if((not vertice1 in self.vertices[0:qntVertices]) or (not vertice2 in self.vertices[0:qntVertices])):
			return False
		else:
			return True

	def delVertice(self,vertice):
		if(self.verificacaoParametrosObtem(vertice)):
			i = 0
			while(i < len(self.arestas)):
				if((str(vertice) in self.arestas[i][0:2])): #percorre as arestas do grafo e olha nas duas primeiras posições, que são os dois vértices que possuem ligação, e caso o "vertice" de entrada seja igual a um desses valores, a aresta é removida
					self.arestas.pop(i)
					i = i - 1
				i = i + 1
			indice = self.vertices.index(vertice)
			self.vertices.pop(indice) # remoção do vértice na lista de vértices
			self.matriz.pop(indice) # remoção da linha cujo vértice pertencia
			for i in range (len(self.vertices)):
				self.matriz[i].pop(indice) #remoçao da coluna desse vértice
		
		else:
			return "O vertice escolhido não pertence ao grafo"
	
	def delAresta(self,vertice1, vertice2):
		if(self.verificacaoParametrosEh(vertice1,vertice2)):
			tem = False
			i = 0
			while(i < len(self.arestas)):
				if((str(vertice1) in self.arestas[i][0]) and (str(vertice2) in self.arestas[i][1])): #percorre as arestas do vértice e verifica se existe a aresta que foi passada como parâmetro, caso exista ela é removida 
					self.arestas.pop(i)
					i = i - 1
					tem = True
				i = i + 1
			
			indice1 = self.vertices.index(vertice1)		
			indice2 = self.vertices.index(vertice2)	
		
			self.matriz[indice1][indice2] = '0' #o valor correspondente a aresta na matriz passa a ser 0
			
			#if(not tem):
				#print ("A aresta escolhida não pertence ao grafo")

		#else:
			#print("A aresta escolhida não pertence ao grafo")

	def geraSubgrafoIA(self, conjuntoArestas):
		listaVertices = []
		for i in conjuntoArestas:
			self.delAresta(i[0],i[1]) #é deletada as arestas pertencentes ao conjunto de arestas passadas como parâmetro
		
		listaDosNaoRemove = funcoes.listarDesconexos(self.grafo) #lista na qual elementos presentes nela não serão removidos, ela recebe inicialmente os vértices desconexos, pois mesmo com um subgrafo induzido por arestas, vértices inicialmente desconexos permanecem

		for i in self.vertices:
			for j in range(len(self.arestas)):
				if((self.arestas[j][0] == str(i)) or (self.arestas[j][1] == str(i))): #verificação dos vértices que ainda possuem ligação mesmo após remoção de arestas
					listaDosNaoRemove.append(str(i))
		
		listaDosNaoRemoveSR = list(set(listaDosNaoRemove))
		
		achei = False
		for i in self.vertices:
			for j in range (len(listaDosNaoRemoveSR)):
				if(str(i) == listaDosNaoRemoveSR[j]):
					achei = True
			if(not achei):
				self.delVertice(i) #vértices que ficaram desconexos ao grafo, são removidos.
			achei = False
		

	def geraSubgrafoIV(self, conjuntoVertices):
		for i in conjuntoVertices: #dado um conjunto de vértices ela remove cada vértice e suas respectivas arestas conforme a função delVertice
			self.delVertice(i)


