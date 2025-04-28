"""A pesquisa binaria tem complexidade de O(log n)"""
def pesquisa_binaria(lista, item):
    baixo = 0
    # para pegar o índice do último elemento
    alto = len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio -1
        else:
            baixo = meio + 1
    return None

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(pesquisa_binaria(lista,5))
