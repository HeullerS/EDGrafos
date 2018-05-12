from funcoes import *
from Grafo import *
from MatrizAdjacencia import *

from ListaAdjacencia import *

from MatrizIncidencia import *



nomeArquivo = input("Digite o nome do arquivo: ")
listaA = listarArestas(nomeArquivo)
listaV = listarValoresVertices(nomeArquivo)
qntVertices = len(listarValoresVertices(nomeArquivo))
direcionado = ehDirecionado(nomeArquivo)
ponderado = ehPonderado(nomeArquivo)
grafo = Grafo(listaV, listaA, direcionado, ponderado)

lista = ListaAdj(grafo.vertices, grafo.arestas, grafo.direcionado,grafo.ponderado, grafo)

imprimirMatriz(lista.lista)





#n5_dir_unwgt_comb0.txt
