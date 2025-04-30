def busca_binaria(lista, item):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim)//2

        if lista[meio] == item:
            return meio

        if lista[meio] > item:
            fim = meio - 1

        else:
            inicio = meio + 1

    return None

if __name__ == "__main__":
    lista = [1,2,3,4,5,6,7]
    print(busca_binaria(lista, 2))