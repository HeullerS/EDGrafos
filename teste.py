class Vertice:
    nome = None
    vizinhos = None
    
    def __init__(self, nome):
        self.nome = nome
        self.vizinhos = {}
        
    def addVizinho(self, vizinho):
        self.vizinhos[vizinho.nome] = vizinho


class Lista:
    vertices = None
    
    def __init__(self):
        self.vertices = {}
        
    def addVertice(self, v):
        self.vertices[v.nome] = v
    
    def addVizinho(self, v1, v2):
        if(v1.nome in self.vertices and v2.nome in self.vertices):
            if(v2.nome not in self.vertices[v1.nome].vizinhos):
               self.vertices[v1.nome].addVizinho(v2)
               
               
def main():
    lista = Lista()
    
    v0 = Vertice(0)
    lista.addVertice(v0)
    
    v1 = Vertice(1)
    lista.addVertice(v1)
    
    v2 = Vertice(2)
    lista.addVertice(v2)
    
    v3 = Vertice(3)
    lista.addVertice(v3)
    
    
    lista.addVizinho(v0, v1)
    lista.addVizinho(v0, v2)
    lista.addVizinho(v3, v3)
    
    saida = ""
    
    for key in lista.vertices:
        saida += str(key) + ": "
        for viz in lista.vertices[key].vizinhos:
            saida += str(viz) + ", "
        saida += "\n"
            
    print(saida)
    
    
    
    
main()
