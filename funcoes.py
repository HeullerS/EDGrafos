from classes import *
#Função que verifica se o grafo é direcionado 
#ou não-direcionado por meio da leitura da primeira linha do arquivo
def ehDirecionado(arq):
	caminhoArquivo = "instances/Padrao_Txt/" + arq
	arquivo = open(caminhoArquivo,'r')
	direcao = arquivo.readline()
	direcao = direcao.rstrip()
	arquivo.close()
	if direcao == 'DIRECTED':
		return True
	else:
		return False

#Função que verifica se o grafo é ponderado ou não
def ehPonderado(arq):
	caminhoArquivo = "instances/Padrao_Txt/" + arq
	arquivo = open(caminhoArquivo,'r')
	arquivo.readline()
	segundaLinha = arquivo.readline().split()
	arquivo.close()
	if(len(segundaLinha) > 2):# Se possui mais um valor alem dos vértices da aresta o grafo é ponderado
		return True
	else:
		return False

#Função que cria uma lista em que cada elemento dessa lista 
#é a ligação de um vértice
def listarArestas(arq):
	caminhoArquivo = "instances/Padrao_Txt/" + arq
	arquivo = open(caminhoArquivo,'r')
	arquivo.readline()
	lista = []
	#Para cada linha do arquivo cria uma lista com os vértices pertencentes
	#à aresta. Ao final  temos como retorno uma lista de listas 
	#Cada elemento da lista final possui 3 valores(u, v, p) em que
	#u e v são vértices e p representa o peso da aresta.
	if(ehPonderado(arq)): 	
		for linha in arquivo:
			lista.append(linha.split())
	else:
		for linha in arquivo:
			linha += str(1)		
			lista.append(linha.split())
	arquivo.close()
	return lista


#Função que cria uma lista em que cada elemento dessa lista 
#é um vértice
def listarVertices(arq):
	qntdVertices  = ""
	indice = 1
	while(arq[indice] != "_"): #Extrai a quantidade de vértices do nme do arquivo
		qntdVertices = qntdVertices + arq[indice]
		indice = indice + 1
	listaVertices = list(range(int(qntdVertices)))
	return listaVertices

#Função que gera uma matriz de incidência a partir de um grafo
def geraMI(grafo):
	lin = len(grafo.arestas)
	col = len(grafo.vertices)
	matriz = []
	for i in range(lin): #Percorrendo cada aresta
		linha = []
		for j in range(col): #Percorrendo cada vertice
			if str(j) in grafo.arestas[i][:2]: # Verifica se o vertice pertence àquela ligação(aresta, dois primeiros termos (u,v))
				if grafo.direcionado == False: # Se o grafo for não direcionado os pesos são simplesmente inseridos na matriz
					linha.append(grafo.arestas[i][2])
				elif str(j) == grafo.arestas[i][0]: #O peso do vértice de saída do arco se mantêm
					linha.append(grafo.arestas[i][2])
				else:
					linha.append('-' + grafo.arestas[i][2]) # Adiciona sinal negativo ao vértice de chegada do arco
			else:
				linha.append('0') # Insere 0 nas colunas dos vértices que não fazem parte da linha(aresta) analisada
		matriz.append(linha) # Insere cada linha na matriz	
	return matriz


#Função que converte uma Matriz de adjacência em uma Matriz de incidência
def converteMAParaMI(matriz,ehDirecionado, ehPonderado):
	tamanho = len(matriz)
	listaVertices = list(range(tamanho))
	listaArestas = []
	listaJaInseridos = []
	for i in range(tamanho):#Para cada posição da matriz verifica se tem uma ligação entre os vértices da posicção i e j
		for j in range(tamanho):
			if not ehDirecionado:#Verifica se o grafo é não direcionado
				if matriz[i][j] != '0' and [str(j),str(i),matriz[i][j]] not in listaJaInseridos:#Verifica se há uma ligação entre os vértices i e j, e se já foi inserida anteriormente 					
					listaArestas.append([str(i),str(j),matriz[i][j]]) #Insere na lista de arestas no formato (u,v,p)
					listaJaInseridos.append([str(i),str(j),matriz[i][j]])#Insere na lista as arestas já inseridas, para evitar a repetição de arestas
			elif matriz[i][j] != '0': #Verifica se tem uma ligação entre os vértices da posição i e j
					listaArestas.append([str(i),str(j),matriz[i][j]]) #Insere na lista de arestas no formato (u,v,p), sem verificação se a aresta já foi inserida(grafo direcionado)
	grafo = Grafo(listaVertices, listaArestas, ehDirecionado, ehPonderado) #Cria grafo auxiliar que será a entrada da geraMI
	return geraMI(grafo)


def geraMA(grafo):
	tamanhoListaVertices = len(grafo.vertices)
	tamanhoListaArestas = len(grafo.arestas)
	matriz = []
	#criação de uma matriz quadrada nula, sendo que seu tamanho é estabelecido pela quantidade de vértices
	for i in range(tamanhoListaVertices): 
		linha = []
		for j in range(tamanhoListaVertices):
			linha.append('0')
		matriz.append(linha)
	

	for i in range(tamanhoListaVertices): #percorrendo lista de vértices
		linha = []
		for j in range(tamanhoListaArestas): #percorrendo lista de arestas 
			if(str(i) == grafo.arestas[j][0]): #verifica se o vértice pertence a uma ligação de arestas
				for k in range(tamanhoListaVertices): #caso a afirmativa anterior seja verdadeira é feito um for para achar o segundo vértice da ligação 
					if(str(k) == grafo.arestas[j][1]): #se k é igual segundo vértice da ligação
					#achado os vértices da ligação, em que "i" é a linha da matriz e "k" a coluna, insere-se o peso da aresta na matriz
						matriz[i][k] = grafo.arestas[j][2]
						if(not grafo.direcionado):#se o grafo não é direcionado, é preciso inserir em dois locais
							matriz[k][i] = grafo.arestas[j][2]
	return matriz

#Função que imprime as Matrizes de Adjacência/Incidência
def imprimirMatriz(matriz):
	linhas = len(matriz)
	colunas = len(matriz[0])
	for i in range(linhas):
		for j in range(colunas):
			print(matriz[i][j]," ",end = "")
		print()

#n5_dir_unwgt_comb0.txt
#n10_dir_wgt_comb3.txt


def converteMIParaMA(matriz, ehDirecionado, ehPonderado):
	qntArestas = len(matriz)
	qntVertices = len(matriz[0])
	listaArestas = []
	listaVertices = list(range(qntVertices))
	jaAcheiPrimeiro = False
	for i in range(qntArestas):
		for j in range(qntVertices):
			if(matriz[i][j] != '0'):
				if(ehDirecionado):
					if(matriz[i][j] > '0'):
						posicaoSaindo = j
						peso = matriz[i][j]
					else:
						posicaoChegando = j	
					
				else:
					if(jaAcheiPrimeiro):
						segundaPosicao = j
					else:
						primeiraPosicao = j
						peso = matriz[i][j]
						jaAcheiPrimeiro = True
					
		jaAcheiPrimeiro = False
		if(ehDirecionado):
			listaArestas.append([str(posicaoSaindo), str(posicaoChegando), peso])
		else:
			listaArestas.append([str(primeiraPosicao), str(segundaPosicao), peso])
	grafo = Grafo(listaVertices, listaArestas, ehDirecionado, ehPonderado)	
	return geraMA(grafo)


def obtemVizinhosMA(grafo, vertice):
	qntVertices = len(grafo.vertices)
	if(not vertice in grafo.vertices[0:qntVertices]):
		print("O vertice escolhido não pertence ao grafo")
	else:
		matrizAdj = geraMA(grafo)
		vizinhos = []

		for i in range(qntVertices):
			if((matrizAdj[vertice][i] != '0') or (matrizAdj[i][vertice] != '0')):
				vizinhos.append(str(i))
		return vizinhos

def obtemPredMA(grafo, vertice):
	qntVertices = len(grafo.vertices)
	if(not vertice in grafo.vertices[0:qntVertices]):
		print("O vertice escolhido não pertence ao grafo")
	else:	
		tamanhoMatriz = len(grafo.vertices)
		matrizAdj = geraMA(grafo)
		#imprimirMatriz(geraMA(grafo))
		listaPred = []
		for i in range (tamanhoMatriz):
			if((matrizAdj[i][vertice] != '0')):
				listaPred.append(i)
						
	return listaPred		
		

def obtemSucMA(grafo, vertice):
	qntVertices = len(grafo.vertices)
	if(not vertice in grafo.vertices[0:qntVertices]):
		print("O vertice escolhido não pertence ao grafo")
	else:
		listaSuc = []
		tamanhoMatriz = len(grafo.vertices)
		matrizAdj = geraMA(grafo)
		for i in range(tamanhoMatriz):
			if(matrizAdj[vertice][i] != '0'):
				listaSuc.append(i)
			
	return listaSuc


def ehVizinhoMA(grafo, vertice1 , vertice2):
	if((not vertice1 in grafo.vertices[0:qntVertices]) or (not vertice2 in grafo.vertices[0:qntVertices])):
		print("O vertice escolhido não pertence ao grafo")
	else:
		matrizAdj = geraMA(grafo)
		if(matrizAdj[vertice1][vertice2] != '0'):	
			return True		
		else:
			return False

'''
def ehPredecessorMA(grafo, vertice1, vertice2):
	if((not vertice1 in grafo.vertices[0:qntVertices]) or (not vertice2 in grafo.vertices[0:qntVertices])):
		print("O vertice escolhido não pertence ao grafo")
	else:
		eh
'''
'''
def ehSucessor(grafo, vertice1, vertice2):
	qntVertices = len(grafo.vertices)
	if((not vertice1 in grafo.vertices[0:qntVertices]) or (not vertice2 in grafo.vertices[0:qntVertices])):
		print("O vertice escolhido não pertence ao grafo")
	else:
		ehSucessor = False
		matrizAdj = geraMA(grafo)
		if(matrizAdj[])
'''








