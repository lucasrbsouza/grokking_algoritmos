# Grafos

Grafos são estruturas de dados compostas por **vértices (ou nós)** e **arestas (ou conexões)** entre esses vértices.

## Tipos de Grafos

### Grafo Direcionado (ou Dígrafo)

Em um **dígrafo**, as arestas possuem direção, ou seja, vão de um vértice para outro, como uma seta. Exemplo:

```
A → B
```

Neste exemplo, **A é vizinho de B**, mas **B não é vizinho de A**, pois a seta vai apenas de A para B.

### Árvores

Uma **árvore** é um tipo especial de grafo **sem ciclos** e com uma estrutura hierárquica. Exemplo:

```
    A
   / \
  B   C
```

* **A** é a **raiz**.
* **B** e **C** são **filhos** de A.
* Em uma árvore, os caminhos **seguem apenas uma direção** (da raiz para os filhos), ou seja, **"só descem e nunca sobem"**.

---

## Representação de Grafos

Para armazenar grafos em código, podemos usar uma **tabela hash (ou dicionário)** onde as chaves são os vértices e os valores são listas de vizinhos. Exemplo:

```python
vertices = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": []
}
```

Isso significa:

```
A → B, C  
B → D  
C →  
D →  
```

> **Observação:** Tabelas hash **não são ordenadas**, então a ordem de inserção dos elementos **não importa**.

---

# Fila

**Fila** é uma estrutura de dados do tipo **FIFO** (*First In, First Out*), ou seja, **o primeiro a entrar é o primeiro a sair**.

### Exemplo prático:

Uma fila de supermercado funciona assim — quem entra primeiro, é atendido primeiro.

### Características:

* **Não permite acesso aleatório** aos elementos.
* Possui duas operações principais:

  * `enqueue` (inserir na fila)
  * `dequeue` (remover da fila)

---

# Pesquisa em Largura (Breadth-First Search - BFS)

A **pesquisa em largura** é um algoritmo usado em grafos para **encontrar o caminho mais curto** entre dois vértices (quando todas as arestas têm o mesmo peso).

### Funcionamento:

1. Começa pelo vértice inicial.
2. Visita todos os vizinhos imediatos.
3. Depois, visita os vizinhos dos vizinhos, e assim por diante.

### Exemplo de níveis de conexão:

* Conexões de **1º grau**: vizinhos diretos.
* Conexões de **2º grau**: vizinhos dos vizinhos.
* E assim por diante.

### Complexidade de Tempo:

```
O(V + A)
```

* **V**: número de vértices
* **A**: número de arestas

---

# Ordenação Topológica

A **ordenação topológica** é um algoritmo aplicado em **grafos direcionados acíclicos (DAGs)** para **ordenar os vértices de forma linear**, respeitando a direção das arestas.

### Quando usar?

* Quando você precisa representar **dependências** entre tarefas.
* Ex: Em um sistema de construção, onde o arquivo A precisa ser compilado **antes** do B.

### Exemplo:

Se tivermos o seguinte grafo:

```
A → B → D
 \      
  → C
```

Uma possível ordenação topológica seria:

```
A, B, C, D
```

Ou:

```
A, C, B, D
```

> Ambas são válidas, desde que **nenhum vértice apareça antes de seus predecessores**.

### Regras principais:

* Só funciona em **grafos direcionados**.
* O grafo **não pode ter ciclos**.
* O resultado é uma **lista linear de vértices** ordenada conforme suas dependências.

### Algoritmo básico (usando BFS - Kahn’s Algorithm):

1. Calcular o **grau de entrada** de cada vértice (quantas arestas chegam até ele).
2. Colocar na fila os vértices com grau de entrada igual a 0.
3. Remover da fila, adicionar à ordenação e **diminuir o grau dos vizinhos**.
4. Repetir até a fila estar vazia.

Se ao final nem todos os vértices forem incluídos, **o grafo tem um ciclo**, e **a ordenação topológica não é possível**.
