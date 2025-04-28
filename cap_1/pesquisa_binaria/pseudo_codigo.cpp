Função PesquisaBinaria(lista, item):
    início ← 0
    fim ← tamanho(lista) - 1

    Enquanto início ≤ fim:
        meio ← (início + fim) / 2

        Se lista[meio] == item:
            Retorne meio

        Senão se lista[meio] < item:
            início ← meio + 1

        Senão:
            fim ← meio - 1

    Retorne -1
