from funcoes import *
from Grafo import *
from MatrizAdjacencia import *
from MatrizIncidencia import *


nomeArquivo = input("Digite o nome do arquivo: ")
listaA = listarArestas(nomeArquivo)
listaV = listarValoresVertices(nomeArquivo)
qntVertices = len(listarValoresVertices(nomeArquivo))
direcionado = ehDirecionado(nomeArquivo)
ponderado = ehPonderado(nomeArquivo)
grafo = Grafo(listaV, listaA, direcionado, ponderado)

matriz = MatrizInc(grafo.vertices, grafo.arestas, grafo.direcionado,grafo.ponderado, grafo)
print(listaA)
imprimirMatriz(matriz.matriz)

print("VIZINHOS: ",matriz.obtemVizinhos(1))
print("SUCESSORES :",matriz.obtemSuc(1))
print("PREDECESSORES: ",matriz.obtemPred(1))
print("EHVIZINHO :", matriz.ehVizinho(1,4))
print("EHPREDECESSOR :",matriz.ehPredecessor(1,3))
print("EHSUCESSOR :", matriz.ehSucessor(1,2))
matriz.delAresta(1,2)
imprimirMatriz(matriz.matriz)
print("ARESTAS: ",matriz.arestas)
matriz.delVertice(1)
imprimirMatriz(matriz.matriz)
print("VERTICES: ",matriz.vertices)
#print(grafo.vertices)
#print(grafo.vertices[0].valor)
#vertice = Vertice(0, grafo)

#n5_dir_unwgt_comb0.txt
#n10_dir_wgt_comb3.txt
#n20_undir_wgt_comb3.txt
