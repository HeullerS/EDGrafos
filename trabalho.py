from funcoes import *
from classes import *



nomeArquivo = input("Digite o nome do arquivo: ")
listaA = listarArestas(nomeArquivo)
listaV = listarValoresVertices(nomeArquivo)
qntVertices = len(listarValoresVertices(nomeArquivo))
direcionado = ehDirecionado(nomeArquivo)
ponderado = ehPonderado(nomeArquivo)
grafo = Grafo(listaV, listaA, direcionado, ponderado)
vertice1 = grafo.verticesObj[0]
vertice2 = grafo.verticesObj[2]

#vertice2 = grafo.verticesObj[1]

print(listaA)
print(ehSucessor(vertice1, vertice2))



#print(grafo.vertices)
#print(grafo.vertices[0].valor)
#vertice = Vertice(0, grafo)





#n5_dir_unwgt_comb0.txt
#n10_dir_wgt_comb3.txt
#n20_undir_wgt_comb3.txt
