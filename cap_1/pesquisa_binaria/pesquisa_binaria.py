# A pesquisa binária tem complexidade de O(log n)
def pesquisa_binaria(lista, item):
    # Define o índice inicial (início da lista)
    baixo = 0
    # Define o índice final (fim da lista)
    alto = len(lista) - 1

    # Continua o loop enquanto a parte não verificada da lista for válida
    while baixo <= alto:
        # Calcula o índice do elemento do meio
        meio = (baixo + alto) // 2
        # Obtém o valor do elemento do meio
        chute = lista[meio]

        # Verifica se o valor do meio é o item procurado
        if chute == item:
            return meio  # Retorna o índice onde o item foi encontrado

        # Se o valor do meio for maior que o item procurado,
        # atualiza o índice final para procurar na metade inferior
        if chute > item:
            alto = meio - 1
        else:
            # Se o valor do meio for menor que o item procurado,
            # atualiza o índice inicial para procurar na metade superior
            baixo = meio + 1

    # Se o item não for encontrado na lista, retorna None
    return None

# Exemplo de uso do algoritmo
if __name__ == '__main__':
    # Lista ordenada
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Procura pelo número 5 na lista
    print(pesquisa_binaria(lista, 5))  # Saída esperada: 4
