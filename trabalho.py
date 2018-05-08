from funcoes import *
from classes import *

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
print(listaA)
print(listaV)
imprimirMatriz(geraMA(grafo))
#print(obtemSucMA(grafo, 4))

print(obtemVizinhosMA(grafo, 2))

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
