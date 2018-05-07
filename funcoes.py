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
	listaVertices = list(range(int(arq[1])))
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
	for i in range(tamanho):
		for j in range(tamanho):
			if matriz[i][j] != '0': #Para cada posição da matriz verifica se tem uma ligação entre os vértices da posicção i e j
				listaArestas.append([str(i),str(j),matriz[i][j]]) #Insere na lista de arestas no formato (u,v,p)
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

#Função que imprimi as Matrizes de Adjacência/Incidência
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
	print("tey")
	
