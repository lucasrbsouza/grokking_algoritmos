# Algortimo de Dijkstra
o algoritmo de Dijkstra (vou chamar de djk) encontra o caminho mais rápido em um grafo
ele possui 4 etapas
o algoritmo de djk atribuimos um peso a cada segmento e ele encontra o caminho com o menor peso total
peso é o numero associado a uma aresta de um grafo
um grafo com peso é chamado de grafo ponderado 
e um grafo sem peso é chamado de grafo não ponderado
para calcular o caminho minimo de um grafo não ponderado utilizamo a pesquisa em largura
para calcular o caminho minimo de um grafo ponderado utilizamos o algoritmo de djk
um ciclo em um grafo indica que é possivel começar em um vertice e terminar nele
e por isso um ciclo jamais fornecera um caminho minino em um grafo ponderado
um grafo não direcionado indica que dois vertices podem apontar um para o outro, e um grafo não direcionado em um ciclo
o algortimo de djk funciona em um grafo aciclico dirigido(DAG)
não podemos utilizar o algortimo de djk em um grafo com arestas com pesos negativas
para isso podemos utilizar o algortimo de Bellman-Ford
o algoritmo de djk tem 4 etapas:
1) Encontrar o vertice mais "barato". É o vertice em que podemos consgeuir chegar no menor tempo possivel
2) verifciar se há um caminho mais barato para os vizinhos desse vertice. caso exista atualize os custos deles
3) repita até que podemos ter feito isso para cada vertice do grafo
4) calcule o caminho final