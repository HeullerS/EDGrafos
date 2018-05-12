from Grafo import *
import funcoes
class MatrizInc(object): # Classe que representa Matriz de incidência
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
				if(self.matriz[i][posicaoVertice] != '0'):# Para cada linha verifica se a coluna do vertice é diferente de 0
					for j in self.vertices:
						posicaoJ = self.vertices.index(j)
						if(self.matriz[i][posicaoJ] != '0') and (posicaoJ != posicaoVertice): # se na mesma linha ouver outra coluna não nula, os vertices sao vizinhos
							ehLoop = False #sendo duas colunas diferentes não nulas temos uma aresta que não forma loop
							if(str(j) not in vizinhos):
								vizinhos.append(str(j)) # adiciona o vertice vizinho , caso não tenha sido adicionado antes
					if(ehLoop):
						vizinhos.append(str(vertice)) # se a aresta foi detectada como loop o próprio vertice é inserido como seu vizinho
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
				if(self.matriz[i][posicaoVertice] > '0'): # Para cada linha verifica se a coluna do vertice é maior que 0, isto é, se ele é antecessor naquela aresta
					for j in self.vertices:
						posicaoJ = self.vertices.index(j)
						if(self.matriz[i][posicaoJ] < '0') and (posicaoJ != posicaoVertice): # se na mesma linha ouver outra coluna menor que 0, este vertice é sucessor
							ehLoop = False #sendo duas colunas diferentes não nulas temos uma aresta que não forma loop
							listaSuc.append(str(j))
					if(ehLoop):
						listaSuc.append(str(vertice)) # se a aresta foi detectada como loop o próprio vertice é inserido como seu sucessor
			return listaSuc
		else:
			return "O vertice escolhido não pertence ao grafo"

	def obtemPred(self, vertice):
		if(self.verificacaoParametrosObtem(vertice)):
			listaPred = []
			posicaoVertice = self.vertices.index(vertice)
			for i in range(len(self.arestas)):
				if(self.matriz[i][posicaoVertice] < '0'): # Para cada linha verifica se a coluna do vertice é menor que 0, isto é, se ele é sucessor naquela aresta
					for j in self.vertices:
						posicaoJ = self.vertices.index(j)
						if(self.matriz[i][posicaoJ] > '0') and (posicaoJ != posicaoVertice):# se na mesma linha ouver outra coluna maior que 0, este vertice é predecessor
							listaPred.append(str(j))
				elif(self.matriz[i][posicaoVertice] > '0'): # Se o vertice for maior que 0 tem a chance de ser um loop
					ehLoop = True 
					for j in self.vertices:
						posicaoJ = self.vertices.index(j)
						if(self.matriz[i][posicaoJ] != '0') and (posicaoJ != posicaoVertice):
							ehLoop = False #sendo duas colunas diferentes não nulas temos uma aresta que não forma loop
					if(ehLoop):
						listaPred.append(str(vertice)) # se a aresta foi detectada como loop o próprio vertice é inserido como seu predessor
				
			return listaPred
		else:
			return "O vertice escolhido não pertence ao grafo"

	def ehVizinho(self, vertice1 , vertice2):
		if(self.verificacaoParametrosEh(vertice1 , vertice2)):
			indice1 = self.vertices.index(vertice1)
			indice2 = self.vertices.index(vertice2)
			ehVizinho = False
			for i in range(len(self.arestas)):
				if (self.matriz[i][indice2] != '0') and (self.matriz[i][indice1] != '0'): # Se a coluna dos dois vertices é não nula na mesma linha, então são vizinhos
					ehVizinho = True		
			return ehVizinho
		else:
			return "O vertice escolhido não pertence ao grafo"

	def ehPredecessor(self, vertice1, vertice2):
		if(self.verificacaoParametrosEh(vertice1 , vertice2)):
			indice1 = self.vertices.index(vertice1)
			indice2 = self.vertices.index(vertice2)
			ehPred = False
			for i in range(len(self.arestas)):
				if (self.matriz[i][indice2] > '0') and (self.matriz[i][indice1] < '0'):  # Se a coluna dos dois vertices é não nula na mesma linha a primeira tendo valor positivo
					print("Linha: ",i, self.matriz[i][indice1],self.matriz[i][indice2])  # e a segunta negativo, entao o segundo é predecessor do primeiro
					ehPred = True	
				#fazer caso do loop	
			return ehPred
		else:
			return "O vertice escolhido não pertence ao grafo"

	def ehSucessor(self, vertice1, vertice2):
		if(self.verificacaoParametrosEh(vertice1 , vertice2)):
			indice1 = self.vertices.index(vertice1)
			indice2 = self.vertices.index(vertice2)
			ehVizinho = False
			for i in range(len(self.arestas)):
				if (self.matriz[i][indice2] < '0') and (self.matriz[i][indice1] > '0'): # Se a coluna dos dois vertices é não nula na mesma linha a primeira tendo valor negativo
					print("Linha: ",i, self.matriz[i][indice1],self.matriz[i][indice2]) # e a segunta positivo, entao o segundo é predecessor do primeiro
					ehVizinho = True	
				#fazer caso do loop
			return ehVizinho
		else:
			return "O vertice escolhido não pertence ao grafo" 

	def verificacaoParametrosObtem(self, vertice):
		qntVertices = len(self.vertices)
		if(not vertice in self.vertices[0:qntVertices]): # Vefica se o vertice de entrada faz parte dos vertices do grafo
			return False
		else:
			return True

	def verificacaoParametrosEh(self, vertice1, vertice2):
			qntVertices = len(self.vertices)
			if((not vertice1 in self.vertices[0:qntVertices]) or (not vertice2 in self.vertices[0:qntVertices])): #Vefica se os vertices de entrada fazem parte dos vertices do grafo
				return False
			else:
				return True

	def delAresta(self, vertice1, vertice2):
		if(self.verificacaoParametrosEh(vertice1,vertice2)):
			listaIndices = []
			for i in range(len(self.arestas)):
				if(str(vertice1) == self.arestas[i][0] and str(vertice2) == self.arestas[i][1]): # Verifica se a aresta de entrada faz parte das arestas do grafo
					listaIndices.append(int(i))
			for i in listaIndices:
				self.matriz.pop(i) #Deletando a Linha correspondente à aresta
				self.arestas.pop(i)#Deletando a aresta na lista de arestas do grafo
		else:
			return "O vertice escolhido não pertence ao grafo"

	def delVertice(self,vertice):
		if(self.verificacaoParametrosObtem(vertice)):
			indiceVertice = self.vertices.index(vertice)
			for i in range(len(self.arestas)):
				self.matriz[i].pop(indiceVertice)
			self.vertices.pop(indiceVertice)
			i = 0			
			while(i < len(self.arestas)):
				if((str(vertice) in self.arestas[i][0:2])):
					self.arestas.pop(i)
					i = i - 1
				i = i + 1
		else:
			return "O vertice escolhido não pertence ao grafo"

	def geraSubgrafoIA(self, conjuntoArestas):
		listaVertices = []
		for arestaDel in conjuntoArestas:
			print("Deletou: ",arestaDel)
			self.delAresta(arestaDel[0],arestaDel[1])
		for vertice in self.vertices: #Trata o caso do vertice ficar isolado
			deletouAresta = False
			sobrouAresta = False
			i = 0
			while(i < len(self.vertices)):
				if vertice in arestaDel[0:2]:#Verifica se o vertice esta na lista de arestas deletadas
					deletouAresta = True
					print("FAZ PARTE DELETOU", vertice, arestaDel)
				for arestaSobrou in self.arestas:
					print("SOBROU",arestaSobrou)
					if vertice in arestaSobrou[0:2]:#Verifica se o vertice esta na lista de arestas que sobraram
						sobrouAresta = True
						print("FAZ PARTE SORBOU")
				if(deletouAresta == True) and (sobrouAresta == True):# Se o vertice esta na lista de arestas deletadas e nao sobrou arestas com o vertice, ele é deletado
					self.delVertice(self.vertices[i])
					i = i - 1
				i = i + 1
'''
	def geraSubgrafoIV(self, conjuntoVertices):
		for i in conjuntoVertices:
			self.delVertice(i)

'''