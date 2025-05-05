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


## Pseudocódigo

```plaintext
Entrada:
- grafo com pesos positivos
- vértice inicial

Inicialize:
- custo[vértice] = infinito (∞), exceto o inicial que é 0
- predecessores[vértice] = indefinido
- conjunto de vértices não processados

Enquanto houver vértices não processados:
    - selecione o vértice com menor custo
    - para cada vizinho do vértice:
        - novo_custo = custo[vértice atual] + peso(aresta)
        - se novo_custo < custo[vizinho]:
            - custo[vizinho] = novo_custo
            - predecessores[vizinho] = vértice atual
    - marque vértice como processado

Saída:
- custo mínimo para cada vértice
- caminho mais curto reconstruído a partir dos predecessores
````

---

## Exemplo de aplicação do algoritmo de Dijkstra

### Grafo:

```
     A
   /   \
  6     1
 /       \
B --- 2 --- C
 \         /
  \--- 1 --/
```

### Tabela de pesos:

| De | Para | Peso |
| -- | ---- | ---- |
| A  | B    | 6    |
| A  | C    | 1    |
| B  | C    | 2    |
| B  | D    | 1    |
| C  | D    | 5    |

Vamos encontrar o **caminho mais curto de A até D**.

### Execução passo a passo:

1. Início em A:

   * custo\[A] = 0
   * custo\[B] = ∞
   * custo\[C] = ∞
   * custo\[D] = ∞

2. A → C (peso 1):

   * custo\[C] = 0 + 1 = 1
   * predecessor\[C] = A

3. A → B (peso 6):

   * custo\[B] = 0 + 6 = 6
   * predecessor\[B] = A

4. C → D (peso 5):

   * custo\[D] = 1 + 5 = 6
   * predecessor\[D] = C

5. C → B (peso 2):

   * custo\[B] = min(6, 1 + 2) = 3
   * predecessor\[B] = C

6. B → D (peso 1):

   * custo\[D] = min(6, 3 + 1) = 4
   * predecessor\[D] = B

### Resultados finais:

| Vértice | Custo mínimo | Caminho       |
| ------- | ------------ | ------------- |
| A       | 0            | A             |
| B       | 3            | A → C → B     |
| C       | 1            | A → C         |
| D       | 4            | A → C → B → D |

---

## Conclusão

O algoritmo de Dijkstra é eficiente e confiável para encontrar caminhos mínimos em grafos com pesos positivos. Ele garante o menor custo de caminho entre um ponto inicial e os demais vértices do grafo.
