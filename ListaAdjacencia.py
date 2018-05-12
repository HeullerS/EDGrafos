from Grafo import *
import funcoes
class ListaAdj(Grafo):
	def __init__(self, listaVertices, listaArestas, ehDirecionado, ehPonderado, grafo):
		Grafo.__init__(self,listaVertices, listaArestas, ehDirecionado, ehPonderado)
		self.grafo = grafo
		self.lista = funcoes.geraLA(grafo)

	def obtemVizinhos(self, vertice): 
		if(self.verificacaoParametrosObtem(vertice)): #vizinhos são obtidos por meio de seus sucessores e predecessores
			sucessores = self.obtemSuc(vertice)
			predecessores = self.obtemPred(vertice)
			vizinhos = sucessores + predecessores 
			vizinhos = list(set(vizinhos)) #caso haja vértices que são sucessores e predecessores, esses são removidos
			vizinhos.sort()
			
			return vizinhos
		else:
			return "O vertice escolhido não pertence ao grafo"
			
	def obtemSuc(self, vertice):
		if(self.verificacaoParametrosObtem(vertice)):
			sucessores = []
			posicaoVertice = self.lista[vertice] # é achado a posição do vértice de acordo com a chave
			
			contador = 0
			for i in posicaoVertice:
				sucessores.append(posicaoVertice[contador][0]) #caso haja uma ligação em que o "vertice" de entrada se liga a outro, esse será adicionado a lista de sucessores
				contador += 1
		
		return sucessores

	def obtemPred(self, vertice):
		if(self.verificacaoParametrosObtem(vertice)):
			predecessores = []
			for i in self.lista:
				posicaoI = self.lista[i]
				for j in range(len(posicaoI)):
					if(posicaoI[j][0] == str(vertice)): #caso haja uma ligação em que o um vértice se liga ao "vertice" de entrada, esse será adicionado a lista de predecessores
						predecessores.append(str(i))
		
			return predecessores
		
		else:
			return "O vertice escolhido não pertence ao grafo"
	


	def ehVizinho(self, vertice1 , vertice2):
		if(self.verificacaoParametrosEh(vertice1 , vertice2)):
			vizinhosDeUm = self.obtemVizinhos(vertice1)
			vizinhosDeDois = self.obtemVizinhos(vertice2)
			
			ehVizinhos = False
			for i in vizinhosDeUm: #verifica pra cada vértice a sua lista de conexões com outros vértices, se esse estiver incluso, portanto são vizinhos
				if(str(vertice2) == i): 
					ehVizinhos = True

			for i in vizinhosDeDois:#também é verificado as ligações do segundo vértice, visto que para serem vizinhos basta que haja um caminho de um para o outro
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

			while(i < len(predecessoresDeUm) and ehPredec == False): #percorre-se a lista de predecessores do vértice 1 para verificar se o vértice 2 consta nela.
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
			while(i < len(sucessoresDeUm) and ehSuces == False): #percorre-se a lista de sucessores do vértice 1 para verificar se o vértice 2 consta nela.
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
				if((str(vertice) in self.arestas[i][0:2])): #se o vértice possuir ligações, serão deletadas
					self.arestas.pop(i)
					i = i - 1
				i = i + 1
			del(self.lista[vertice]) #deleta-se o vértice na lista de adjacência
			indice = self.vertices.index(vertice) 
			self.vertices.pop(indice) #remove-se o vértice na lista de vértices
		
		else:
			return "O vertice escolhido não pertence ao grafo"

	def delAresta(self,vertice1, vertice2):
		if(self.verificacaoParametrosEh(vertice1,vertice2)):
			i = 0
			while(i < len(self.arestas)):
				if((str(vertice1) in self.arestas[i][0]) and (str(vertice2) in self.arestas[i][1])): 
					self.arestas.pop(i)# remoção da aresta na lista de arestas
					i = i - 1
				i = i + 1
			
			sucessores = self.obtemSuc(vertice1)
			existe = False
			for i in range(len(sucessores)): # a partir dos sucessores verifica a aresta de ligação, caso haja, no próximo passo será deletado a aresta referente a chave
				if(sucessores[i] == str(vertice2)):
					existe = True

			if(existe):
				contador = 0
				for i in self.lista[vertice1]:	
					if(str(vertice2) == self.lista[vertice1][contador][0]):
						self.lista[vertice1].pop(contador)
					contador += 1
	
	def geraSubgrafoIV(self, conjuntoVertices):
		for i in conjuntoVertices:
			self.delVertice(i) #dado um conjunto de vértices ela remove cada vértice e suas respectivas arestas conforme a função delVertice

	def geraSubgrafoIA(self, conjuntoVertices):
		listaVertices = []
		for i in conjuntoVertices:
			self.delAresta(i[0],i[1])
		
		listaDosNaoRemove = funcoes.listarDesconexos(self.grafo) #lista na qual elementos presentes nela não serão removidos, ela recebe inicialmente os vértices desconexos, pois mesmo com um subgrafo induzido por arestas, vértices inicialmente desconexos permanecem

		for i in self.vertices:
			for j in range(len(self.arestas)):
				if self.arestas[j][0] == str(i): 
					listaDosNaoRemove.append(str(i))
		
		listaDosNaoRemoveSR = list(set(listaDosNaoRemove)) 

		achei = False
		for i in self.vertices:
			for j in range (len(listaDosNaoRemoveSR)):
				if(str(i) == listaDosNaoRemoveSR[j]):
					achei = True
			
			if(not achei):
				self.delVertice(i) #é deletado os vértices que ficaram desconexos após a remoção de arestas
			achei = False
			
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
