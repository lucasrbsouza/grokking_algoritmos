📜 Pseudocódigo do Algoritmo de Dijkstra

Entrada:
- grafo com pesos positivos
- vértice inicial (início)

Inicialize:
- custo[vértice] = infinito, para todos os vértices
- custo[início] = 0
- predecessores[vértice] = indefinido
- conjunto de vértices não processados

Enquanto existirem vértices não processados:
    - escolha o vértice atual com o menor custo

    Para cada vizinho do vértice atual:
        - novo_custo = custo[atual] + peso(aresta atual → vizinho)
        - se novo_custo < custo[vizinho]:
            - custo[vizinho] = novo_custo
            - predecessores[vizinho] = atual

    - marque o vértice atual como processado (remova do conjunto)

Saída:
- custos mínimos a partir do vértice inicial
- caminho mínimo (reconstruído usando o vetor de predecessores)


Explicação rápida

custo: guarda o menor custo conhecido para chegar a cada vértice.
predecessores: armazena por qual vértice passamos para chegar até aquele.
O algoritmo sempre escolhe o vértice com menor custo atual para explorar primeiro.
Ele vai "melhorando" os caminhos à medida que encontra rotas mais baratas.
