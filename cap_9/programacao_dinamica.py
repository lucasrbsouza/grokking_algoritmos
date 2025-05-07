"""criando a solucao para um probelma da mochila em comum usanod programacao dinamica"""
# Exemplo em Python
def mochila(valores, pesos, capacidade):
    n = len(valores)
    tabela = [[0] * (capacidade + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacidade + 1):
            if pesos[i - 1] <= w:
                tabela[i][w] = max(valores[i - 1] + tabela[i - 1][w - pesos[i - 1]], tabela[i - 1][w])
            else:
                tabela[i][w] = tabela[i - 1][w]

    return tabela[n][capacidade]

if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    capacidade = 50

    print(mochila(valores, pesos, capacidade))