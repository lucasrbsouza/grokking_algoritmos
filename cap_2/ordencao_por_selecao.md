## Ordenação por Seleção (Selection Sort)

A **ordenação por seleção** é um algoritmo simples que funciona assim:

1. Começamos com o primeiro item da lista.
2. Procuramos o **menor valor** no restante da lista.
3. Trocamos esse menor valor com o primeiro item.
4. Depois, vamos para o segundo item e repetimos o processo:
   - Procuramos o menor valor do restante da lista (do segundo item em diante).
   - Trocamos com o segundo item.
5. E assim por diante, até o fim da lista.

### Exemplo Simples

Imagine que temos esta lista:
`[5, 3, 6, 2, 10]`

Passo a passo:

- Procuramos o menor valor: `2`. Trocamos com `5`.
  - Lista: `[2, 3, 6, 5, 10]`
- Procuramos o menor a partir do segundo elemento: `3`. Já está certo.
- Procuramos o menor entre `[6, 5, 10]`: `5`. Trocamos com `6`.
  - Lista: `[2, 3, 5, 6, 10]`
- E assim por diante.

### Características do Selection Sort

- Simples de entender e implementar.
- Não precisa de memória extra.
- **Lento para listas grandes**.

### Complexidade

- Melhor caso: `O(n²)`
- Pior caso: `O(n²)`
- Não é eficiente para grandes volumes de dados, mas é bom para ensinar conceitos de ordenação.

---

