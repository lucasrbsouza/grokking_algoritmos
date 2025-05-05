"""criando uma representacao da implementacao do algoritmo de Dijkstra"""

def ache_no_custo_mais_baixo(custos, processados):
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None
    for nodo in custos:
        custo = custos[nodo]
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo

def dijkstra():
    grafo = {}
    grafo["inicio"] = {}
    grafo["inicio"]["a"] = 6

    grafo["inicio"]["b"] = 2
    grafo["a"] = {}
    grafo["a"]["fim"] = 1
    grafo["b"] = {}
    grafo["b"]["a"] = 3
    grafo["b"]["fim"] = 5

    grafo["fim"] = {}
    infinito = float("inf")
    custos = {"a": 6, "b": 2, "fim": infinito}

    pais = {"a": "inicio", "b": "inicio", "fim": None}

    processados = []

    nodo = ache_no_custo_mais_baixo(custos, processados)
    while nodo is not None:
        custo = custos[nodo]
        vizinhos = grafo[nodo]
        for n in vizinhos.keys():
            novo_custo = custo + vizinhos[n]
            if custos[n] > novo_custo:
                custos[n] = novo_custo
                pais[n] = nodo
        processados.append(nodo)
        nodo = ache_no_custo_mais_baixo(custos, processados)
    return custos, pais

if __name__ == '__main__':
    custos, pais = dijkstra()
    print("Custos finais:", custos)
    print("Pais (caminho):", pais)

    # Reconstruir o caminho mais curto do fim ao início
    caminho = []
    nodo = "fim"
    while nodo in pais:  # enquanto houver pai conhecido
        caminho.insert(0, nodo)
        nodo = pais[nodo]
    caminho.insert(0, "inicio")  # adicionar o início manualmente

    print("Caminho mais curto:", " -> ".join(caminho))
