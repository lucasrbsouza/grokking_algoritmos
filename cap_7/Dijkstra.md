# Algoritmo de Dijkstra

O algoritmo de Dijkstra (que vamos chamar de **DJK**) é usado para encontrar o caminho mais curto entre dois pontos em um **grafo ponderado** (ou seja, um grafo em que cada aresta tem um peso, que normalmente representa distância, tempo ou custo).

Ele funciona em **4 etapas principais** e é muito útil em problemas como encontrar a rota mais rápida em um mapa.

## Conceitos importantes

* **Peso**: é um número associado a uma aresta (ligação entre dois vértices) que indica o custo de percorrer aquele caminho.
* **Grafo ponderado**: é um grafo onde todas as arestas têm pesos definidos.
* **Grafo não ponderado**: é um grafo onde as arestas não possuem pesos.
* Para encontrar o caminho mais curto em um **grafo não ponderado**, usamos a **busca em largura**.
* Para encontrar o caminho mais curto em um **grafo ponderado**, usamos o **algoritmo de Dijkstra**.
* Um **ciclo** em um grafo é um caminho que começa e termina no mesmo vértice. Ciclos **não atrapalham** o funcionamento do algoritmo, **desde que os pesos das arestas sejam positivos**.
* Um **grafo direcionado** é aquele onde as arestas têm direção (ou seja, ir de A para B não significa que é possível voltar de B para A).
* Um **grafo não direcionado** é aquele em que as arestas permitem ida e volta entre os vértices conectados.
* O algoritmo de DJK **não funciona com arestas de peso negativo**. Para esses casos, usamos o **algoritmo de Bellman-Ford**.

## Etapas do algoritmo de Dijkstra

1. **Escolher o vértice mais "barato" ainda não processado.**
   Isso significa escolher o vértice de onde conseguimos chegar com o menor custo até o momento.

2. **Verificar os vizinhos desse vértice.**
   Para cada vizinho, calculamos o custo total do caminho passando por esse vértice.
   Se for mais barato do que o custo atual salvo para esse vizinho, **atualizamos o custo**.

3. **Marcar o vértice atual como "processado".**
   Repetimos o processo até que todos os vértices tenham sido processados.

4. **Reconstruir o caminho final.**
   Depois de atualizar os custos, usamos as informações salvas para encontrar o caminho de menor custo até o destino.

