from funcoes import *
from Grafo import *
from MatrizAdjacencia import *

'''
matriz = []
for i in range(x):
	linha = []
	for j in range(x):
		linha.append(valor)
	matriz.append(linha)

'''


'''
#IMPRESSÃO
for i in matriz:
	for j in i:
		print(j, end = ' ')
	print("\n")
'''

nomeArquivo = input("Digite o nome do arquivo: ")
listaA = listarArestas(nomeArquivo)
listaV = listarVertices(nomeArquivo)
direcionado = ehDirecionado(nomeArquivo)
ponderado = ehPonderado(nomeArquivo)
grafo = Grafo(listaV, listaA, direcionado, ponderado)
matriz = MatrizAdj(grafo.vertices, grafo.arestas, grafo.direcionado,grafo.ponderado, grafo)
print(listaA)
imprimirMatriz(matriz.matriz)
#print(matriz.obtemVizinhos(2))
#print(matriz.obtemSuc(0))
#print(matriz.obtemPred(0))
#print(matriz.ehVizinho(1,2))
#print(matriz.ehPredecessor(2,1))
#print(matriz.ehSucessor(1,2))

#print(ehSucessorMA(grafo, 0, 3))


#print(obtemSucMA(grafo, 4))

#print(ehVizinhoMA(grafo, 1,4))

#n5_dir_unwgt_comb2.txt
#n5_dir_unwgt_comb0.txt


'''
direcionado = ehDirecionado(nomeArquivo)
#lista = listarLigacoes(nomeArquivo)
#print(lista)

ponderado = ehPonderado(nomeArquivo)
listaA = listarArestas(nomeArquivo)
#print(listaA)
listaV = listarVertices(nomeArquivo)
grafo = Grafo(listaV, listaA, direcionado, ponderado)
print('Vertices: ', grafo.vertices)
print('Arestas: ', grafo.arestas)
print("----------- MATRIZ DE ADJ ------------------")
matrizMA = geraMA(grafo)
imprimirMatriz(matrizMA)
print("----------- MATRIZ DE INC ------------------")
matrizMI = geraMI(grafo)
imprimirMatriz(matrizMI)
print("------------- MI PARA MA ----------------")
#print(converteMIParaMA(geraMI(grafo), direcionado, ponderado))
imprimirMatriz(converteMIParaMA(matrizMI, direcionado, ponderado))
print("----------- MA PARA MI ------------------")
imprimirMatriz(converteMAParaMI(matrizMA, direcionado, ponderado))
'''

'''
matrizMA = geraMA(grafo)
imprimirMatriz(matrizMA)
print()
matrizMI = converteMAParaMI(matrizMA,grafo.direcionado, grafo.ponderado)
imprimirMatriz(matrizMI)

#print(ehPonderado(nomeArquivo))
#print("Matriz:\n")
#matriz = geraMI(grafo)
#imprimirMatriz(matriz)
'''
#n5_dir_unwgt_comb0.txt
#n10_dir_wgt_comb3.txt
#n20_undir_wgt_comb3.txt
