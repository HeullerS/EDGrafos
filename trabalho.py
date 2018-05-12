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

print("Matriz Original")
imprimirMatriz(matriz.matriz)
print("Vertices:", matriz.vertices)
print("Arestas:",matriz.arestas)
matriz.geraSubgrafoIA([[1,2],[3,4],[0,3]])




print("Nova Matriz:")
imprimirMatriz(matriz.matriz)
print("Vertices:", matriz.vertices)
print("Arestas:",matriz.arestas)
#n5_dir_unwgt_comb0.txt
#n10_dir_wgt_comb3.txt
#n20_undir_wgt_comb3.txt