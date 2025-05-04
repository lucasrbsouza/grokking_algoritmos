def busca_menor(arr):
    menor = arr[0]  # primeiro item
    menor_indice = 0
    for i in range(len(arr)):

        if arr[i] < menor:  # se o array na posicao i for menor que o primeiro item
            menor = arr[i]  # então o primeiro item vai ser o item na posicao i
            menor_indice = i  # então o menor indice vai ser o indice i

    return menor_indice


def selection_sort(arr):
    novo_arr = []
    for i in range(len(arr)):
        menor = busca_menor(arr)  # procurando o menor valor da lista e adicionando a variavel menor
        novo_arr.append(arr.pop(menor))  # removendo e lendo o menor valor e adicionando a lista novo_arr
    return novo_arr


if __name__ == "__main__":
    lista = [90, 76, 34, 21, 2, 5, 45, 77, 54, 86]
    print(selection_sort(lista))
