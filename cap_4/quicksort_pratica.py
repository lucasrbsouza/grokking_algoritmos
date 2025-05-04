import random

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivo = arr[0]
        menores = [i for i in arr[1:] if i<= pivo]
        maiores = [i for i in arr[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)


def quicksort_otm(arr):
    if len(arr) < 2:
        return arr
    else:
        pivo = random.choice(arr)
        menores = [i for i in arr if i < pivo]
        iguais = [i for i in arr if i == pivo]
        maiores = [i for i in arr if i > pivo]
        return quicksort_otm(menores) + iguais + quicksort_otm(maiores)


if __name__ == '__main__':
    lista_inversa = [i for i in range(11,0,-1)]
    lista_ordenada = [i for i in range(1,12)]
    print(lista_inversa)
    print(lista_ordenada)

    print("-"*len(lista_ordenada) + "quicksort" +"-"*len(lista_ordenada))
    print(quicksort_otm(lista_inversa))
    print(quicksort_otm(lista_ordenada))

    print(40*"*")
    print(quicksort(lista_ordenada))
    print(quicksort(lista_inversa))