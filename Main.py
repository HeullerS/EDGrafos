from funcoes import *
from Grafo import *
from MatrizAdjacencia import *
from MatrizIncidencia import *

print("Bem vindo ao manipulador de grafos")
nomeArquivo = input("Digite o nome do arquivo: ")
print()
listaA = listarArestas(nomeArquivo)
listaV = listarValoresVertices(nomeArquivo)
qntVertices = len(listarValoresVertices(nomeArquivo))
direcionado = ehDirecionado(nomeArquivo)
ponderado = ehPonderado(nomeArquivo)
grafo = Grafo(listaV, listaA, direcionado, ponderado)
print("Escolha uma das Estrutura de Dados a seguir para representar o Grafo")
print("Digite o número correspondente:")
print("1. Matriz de Adjacência")
print("2. Matriz de Incidência")
print("3. Lista de Adjacência")
opcaoEst = input()
if opcaoEst == '1':
	matrizAdj = MatrizAdj(grafo.vertices, grafo.arestas, grafo.direcionado,grafo.ponderado, grafo)

elif opcaoEst == '2':
	matrizInc = MatrizInc(grafo.vertices, grafo.arestas, grafo.direcionado,grafo.ponderado, grafo)

elif opcaoEst == '3':
	listaAdj = ListaAdj(grafo.vertices, grafo.arestas, grafo.direcionado,grafo.ponderado, grafo)
opcaoFunc = '0'
while(opcaoFunc != '13'):
	print()
	print("Escolha uma das seguintes opções para a Estrutura escolhida")
	print()
	print("  1. Imprimir")
	print("  2. Obter Vizinhos")
	print("  3. Obter Predecessores")
	print("  4. Obter Sucessores")
	print("  5. É Vizinho")
	print("  6. É Predecessor")
	print("  7. É Sucessor")
	print("  8. Deletar Vértice")
	print("  9. Deletar Aresta")
	print("  10. Gera Subgrafo Induzido por Arestas")
	print("  11. Gera Subgrafo Induzido por Vertices")
	print("  12. Converter")	
	print("  13. Encerrar execução")
	opcaoFunc = input()
	if opcaoFunc == '1':#Imprimir
		if opcaoEst == '1':
			print("Matriz de Adjacência:")
			imprimirMatriz(matrizAdj.matriz)
		elif opcaoEst == '2':
			print("Matriz de Incidência:")
			imprimirMatriz(matrizInc.matriz)
		elif opcaoEst == '3':
			print("Lista de Incidência:")
			imprimirLista(listaAdj.lista)
	

	if opcaoFunc == '2':#Obter Vizinhos
		vertice = int(input("Insira o Vértice: "))
		if opcaoEst == '1':
			print("Vizinhos: ",matrizAdj.obtemVizinhos(vertice))
		elif opcaoEst == '2':
			print("Vizinhos: ",matrizAdj.obtemVizinhos(vertice))
		elif opcaoEst == '3':
			print("Vizinhos: ",listaAdj.obtemVizinhos(vertice))
	

	if opcaoFunc == '3':#Obter Predecessores
		vertice = int(input("Insira o Vértice: "))
		if opcaoEst == '1':
			print("Predecessores: ",matrizAdj.obtemPred(vertice))
		elif opcaoEst == '2':
			print("Predecessores: ",matrizAdj.obtemPred(vertice))
		elif opcaoEst == '3':
			print("Predecessores: ",matrizAdj.obtemPred(vertice))
	

	if opcaoFunc == '4':#Obter Sucessores
		vertice = int(input("Insira o Vértice: "))
		if opcaoEst == '1':
			print("Sucessores: ",matrizAdj.obtemSuc(vertice))
		elif opcaoEst == '2':
			print("Sucessores: ",matrizAdj.obtemSuc(vertice))
		elif opcaoEst == '3':
			print("Sucessores: ",matrizAdj.obtemSuc(vertice))
	

	if opcaoFunc == '5':#É Vizinho
		vertice1 = int(input("Insira o Vértice 1: "))
		vertice2 = int(input("Insira o Vertice 2: "))
		if opcaoEst == '1':
			print("Vizinho: ",matrizAdj.ehVizinho(vertice1,vertice2))
		elif opcaoEst == '2':
			print("Vizinho: ",matrizAdj.ehVizinho(vertice1,vertice2))
		elif opcaoEst == '3':
			print("Vizinho: ",matrizAdj.ehVizinho(vertice1,vertice2))


	if opcaoFunc == '6':#É Predecessor
		vertice1 = int(input("Insira o Vértice 1: "))
		vertice2 = int(input("Insira o Vertice 2: "))
		if opcaoEst == '1':
			print("Predecessor: ",matrizAdj.ehPredecessor(vertice1,vertice2))
		elif opcaoEst == '2':
			print("Predecessor: ",matrizAdj.ehPredecessor(vertice1,vertice2))
		elif opcaoEst == '3':
			print("Predecessor: ",matrizAdj.ehPredecessor(vertice1,vertice2))
	

	if opcaoFunc == '7':#É Sucessor
		vertice1 = int(input("Insira o Vértice 1: "))
		vertice2 = int(input("Insira o Vertice 2: "))
		if opcaoEst == '1':
			print("Sucessor: ",matrizAdj.ehSucessor(vertice1,vertice2))
		elif opcaoEst == '2':
			print("Sucessor: ",matrizAdj.ehSucessor(vertice1,vertice2))
		elif opcaoEst == '3':
			print("Sucessor: ",matrizAdj.ehSucessor(vertice1,vertice2))
	

	if opcaoFunc == '8':#Deletar Vértice
		vertice = int(input("Insira o Vértice"))
		if opcaoEst == '1':
			print(" Nova Matriz de Adjacência:")
			matrizAdj.delVertice(vertice)
			imprimirMatriz(matrizAdj.matriz)
		elif opcaoEst == '2':
			print("Nova Matriz de Incidência:")
			matrizInc.delVertice(vertice)
			imprimirMatriz(matrizInc.matriz)
		elif opcaoEst == '3':
			print("Nova Lista de Incidência:")
			listaAdj.delVertice(vertice)
			imprimirLista(listaAdj.lista)


	if opcaoFunc == '9':#Deletar Aresta
		vertice1 = int(input("Insira o primeiro Vértice da aresta: "))
		vertice2 = int(input("Insira o segundo Vértice da aresta: "))
		if opcaoEst == '1':
			print(" Nova Matriz de Adjacência:")
			matrizAdj.delAresta(vertice1, vertice2)
			imprimirMatriz(matrizAdj.matriz)
		elif opcaoEst == '2':
			print("Nova Matriz de Incidência:")
			matrizInc.delAresta(vertice1, vertice2)
			imprimirMatriz(matrizInc.matriz)
		elif opcaoEst == '3':
			print("Nova Lista de Incidência:")
			listaAdj.delAresta(vertice1, vertice2)
			imprimirLista(listaAdj.lista)

	
	if opcaoFunc == '10':#Gera Subgrafo Induzido por Arestas
		quantidadeArestas = int(input("Quantidade de Arestas a serem deletadas"))
		listaArestas = []
		for i in range(quantidadeArestas):
			print("Insira a aresta: ")
			vertice1 = int(input("   Primeiro vértice: "))
			vertice2 = int(input("   Segundo vértice: "))
			listaArestas.append([vertice1,vertice2])
		if opcaoEst == '1':
			print(" Nova Matriz de Adjacência:")
			matrizAdj.geraSubgrafoIA(listaArestas))
			imprimirMatriz(matrizAdj.matriz)
		elif opcaoEst == '2':
			print("Nova Matriz de Incidência:")
			matrizInc.geraSubgrafoIA(listaArestas)) # CONFERIRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
			imprimirMatriz(matrizInc.matriz)
		elif opcaoEst == '3':
			print("Nova Lista de Incidência:")
			listaAdj.geraSubgrafoIA(listaArestas))
			imprimirLista(listaAdj.lista)
	
	
	if opcaoFunc == '11':#Gera Subgrafo Induzido por Vértices
		quantidadeVertices = int(input("Quantidade de Vértices a serem deletados"))
			listaVertices = []
		for i in range(quantidadeVertices):
			vertice = int(input("Insira o vértice"))
			listaVertices.append(vertice)
		if opcaoEst == '1':
			print(" Nova Matriz de Adjacência:")
			matrizAdj.geraSubgrafoIV(listaVertices))
			imprimirMatriz(matrizAdj.matriz)
		elif opcaoEst == '2':
			print("Nova Matriz de Incidência:")
			matrizInc.geraSubgrafoIV(listaVertices)) # CONFERIRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
			imprimirMatriz(matrizInc.matriz)
		elif opcaoEst == '3':
			print("Nova Lista de Incidência:")
			listaAdj.geraSubgrafoIV(listaVertices))
			imprimirLista(listaAdj.lista)

	if opcaoFunc == '12':
		print("As opções de conversão para essa estrutura são as seguintes")
		
		if opcaoEst == '1':
			print("   1. Converter Matriz de Adjacência para Matriz de Incidência")
			print("   2. Converter Matriz de Adjacência para Lista de Adjacência")
			opcaoConv = input()
			if opcaoConv == '1':
				matrizInc = converteMAparaMI(matrizAdj.matriz,matrizAdj.direcionado,matrizAdj.ponderado)
				opcaoFunc = '2'
			elif opcaoConv == '2':
				listaAdj = converteMAparaLA(matrizAdj.matriz,matrizAdj.direcionado,matrizAdj.ponderado)
				opcaoFunc = '3'
		if opcaoEst == '2':
			print("   1. Converter Matriz de Incidência para Matriz de Adjacência")
			print("   2. Converter Matriz de Incidência para Lista de Adjacência")
			opcaoConv = input()
			if opcaoConv == '1':
				matrizAdj = converteMIparaMA(matrizInc.matriz,matrizInc.direcionado,matrizInc.ponderado)
				opcaoFunc = '1'
			elif opcaoConv == '2':
				listaAdj = converteMIparaLA(matrizInc.matriz,matrizInc.direcionado,matrizInc.ponderado)
				opcaoFunc = '3'
		if opcaoEst == '3':
			print("   1. Converter Lista de Adjacência para Matriz de Incidência")
			print("   2. Converter Lista de Adjacência para Matriz de Adjacência")
			opcaoConv = input()
			if opcaoConv == '1':
				matrizInc = converteLAparaMI(listaAdj.lista,listaAdj.direcionado,listaAdj.ponderado)
				opcaoFunc = '2'
			elif opcaoConv == '2':
				matrizAdj = converteLAparaMA(listaAdj.lista,listaAdj.direcionado,listaAdj.ponderado)
				opcaoFunc = '1'
		
print()
print("Execução Encerrada")			
#n5_dir_unwgt_comb0.txt
