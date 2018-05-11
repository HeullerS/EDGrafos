from funcoes import *
from Grafo import *
from MatrizAdjacencia import *
from ListaAdjacencia import *

nomeArquivo = input("Digite o nome do arquivo: ")
listaA = listarArestas(nomeArquivo)
listaV = listarVertices(nomeArquivo)
direcionado = ehDirecionado(nomeArquivo)
ponderado = ehPonderado(nomeArquivo)
grafo = Grafo(listaV, listaA, direcionado, ponderado)
lista = ListaAdj(grafo.vertices, grafo.arestas, grafo.direcionado,grafo.ponderado, grafo)

print(lista.lista)
print(lista.obtemVizinhos(0))


#n5_dir_unwgt_comb0.txt
#n10_dir_wgt_comb3.txt
#n20_undir_wgt_comb3.txt
