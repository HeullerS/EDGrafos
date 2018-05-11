## EDGrafos

<h1>ESTRUTURA DE DADOS</h1>

	• Matriz de adjacências ✔
	
		FUNÇÕES DE VISUALIZAÇÃO
			obtemVizinhos: ✔ 
			obtemPred: ✔ 
			obtemSuc: ✔ 
			ehVizinho: ✔ 
			ehPredecessor: ✔ 
			ehSucessor: ✔ 
		FUNÇÕES DE MANIPULAÇÃO
			delVertice: ✔ 
			delAresta: ✔ 
			geraSubgrafoIV: ✔
			geraSubgrafoIA: ✔

	• Lista de adjacências X
	
		FUNÇÕES DE VISUALIZAÇÃO
			obtemVizinhos: X
			obtemPred: X
			obtemSuc: X
			ehVizinho: X
			ehPredecessor: X
			ehSucessor: X
		FUNÇÕES DE MANIPULAÇÃO
			delVertice: X
			delAresta: X
			geraSubgrafoIV: X
			geraSubgrafoIA: X

	• Matriz de incidências ✔
	
		FUNÇÕES DE VISUALIZAÇÃO
			obtemVizinhos: ✔
			obtemPred: ✔
			obtemSuc: ✔
			ehVizinho: ✔
			ehPredecessor: ✔
			ehSucessor: ✔
		FUNÇÕES DE MANIPULAÇÃO
			delVertice: X
			delAresta: X
			geraSubgrafoIV: X
			geraSubgrafoIA: X

<h1>CONVERSÕES</h1>
				
	• Converte matriz de adjacência em lista de adjacência: X
	• Converte matriz de adjacência em matriz de incidência: ✔
	• Converte lista de adjacência em matriz de adjacência: X
	• Converte lista de adjacência em matriz de incidência: X
	• Converte matriz de incidência em lista de adjacência: X
	• Converte matriz de incidência em matriz de adjacência ✔


<h1>OBSERVAÇÕES</h1>
	• Olhar casos de loop nas funções da MatrizIncidencia
	• Olhar casos de grafos direcionado nas funções "eh"
	• Olhar casos de loop na geraMI
	• Corrigir casos do indice do vertice nas funções "obtem"

