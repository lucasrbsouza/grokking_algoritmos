## Pseudocódigo – Ordenação por Seleção (Selection Sort)

```plaintext
SELECTION-SORT(lista)
    n ← tamanho da lista

    para i de 0 até n - 1
        menor_indice ← i

        para j de i + 1 até n - 1
            se lista[j] < lista[menor_indice]
                menor_indice ← j

        se menor_indice ≠ i
            trocar lista[i] com lista[menor_indice]
