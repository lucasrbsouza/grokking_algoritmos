def busca_menor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def selection_sort(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = busca_menor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

if __name__ == "__main__":
    lista = [90,76, 34,21,2,5,45,77,54,86]
    print(selection_sort(lista))