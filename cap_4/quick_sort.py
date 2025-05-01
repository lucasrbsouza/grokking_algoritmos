import random

"""Versão com pivô fixo (para comparação) - O(n²) no pior caso"""
def quick_sort1(arr):
    if len(arr) < 2:
        return arr
    else:
        pivo= arr[0]
        menores = [i for i in arr[1:] if i <= pivo]
        maiores = [i for i in arr[1:] if i > pivo]
        return quick_sort1(menores) + [pivo] + quick_sort1(maiores)

"""Versão com pivô aleatório - O(n log n) esperado"""
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivo = random.choice(arr)
        menores = [i for i in arr if i < pivo]  # Todos menores que o pivô
        iguais = [i for i in arr if i == pivo]  # Todos iguais ao pivô
        maiores = [i for i in arr if i > pivo]  # Todos maiores que o pivô
        return quick_sort(menores) + iguais + quick_sort(maiores)


if __name__ == '__main__':
    lista = [1,2,3,4,5,6,7,8,9,10]

    print(quick_sort1(lista))
    print(quick_sort(lista))


