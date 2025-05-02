def busca_binaria(lista,item):
    inicio = 0
    fim = len(lista)
    while inicio < fim:
        meio = (inicio + fim) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        if chute < item:
            inicio = meio + 1
        else:
            fim = meio - 1
    return None

if __name__ == "__main__":
    lista = [1,2,3,4,5,6,7]
    print(busca_binaria(lista, 6))