from funcoes import *
from classes import *

nomeArquivo = input("Digite o nome do arquivo: ")
direcionado = ehDirecionado(nomeArquivo)
#lista = listarLigacoes(nomeArquivo)
#print(lista)


listaA = listarArestas(nomeArquivo)
#print(listaA)
listaV = listarVertices(nomeArquivo)
grafo = Grafo(nomeArquivo)
print('Vertices: ', grafo.vertices)
print('Arestas: ', grafo.arestas)
#print(ehPonderado(nomeArquivo))
print("Matriz:\n")
matriz = geraMI(grafo)
imprimirMatriz(matriz)
#n5_dir_unwgt_comb0.txt
#n10_dir_wgt_comb3.txt
