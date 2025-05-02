# Tabelas Hash

Tabelas hash, também conhecidas como **mapas hash**, **mapas**, **dicionários** ou **tabelas de dispersão**, são estruturas de dados que mapeiam **chaves** a **valores**.

---

## Quando usar uma Tabela Hash?

As tabelas hash são ótimas quando:

* Precisamos mapear um item em relação a outro.
* Queremos pesquisar rapidamente por um valor usando uma chave.
* Precisamos detectar ou evitar duplicatas com eficiência.

---

## Desempenho

* **Melhor caso:** O(1) – Inserções, pesquisas e remoções são feitas instantaneamente.
* **Pior caso:** O(n) – Quando há muitas colisões e a estrutura se degrada (ex: listas encadeadas longas).

Em geral, as tabelas hash são muito rápidas para **pesquisar**, **inserir** e **remover** itens.

---

## Funções Hash

Uma **função hash** é usada para converter uma chave (geralmente uma string ou número) em um **índice de array** onde o valor será armazenado.

### Requisitos de uma boa função hash:

* **Consistência**: Sempre retorna o mesmo valor para a mesma entrada.
* **Distribuição uniforme**: Diferentes entradas devem ser mapeadas para diferentes posições no array.

> A função hash informa **a posição exata** onde um item deve ser armazenado, eliminando a necessidade de varrer o array.

> Quando combinamos uma função hash com um array, temos uma **Tabela Hash**.

Uma boa função hash deve distribuir os valores **simetricamente** pelo array.

⚠️ Uma função hash ruim agrupa valores em poucas posições, criando **muitas colisões**.

---

## Colisões

**Colisão** acontece quando duas ou mais chaves são mapeadas para o **mesmo espaço** na tabela.

### Como resolver colisões:

* Usar **listas encadeadas** em cada posição do array para armazenar múltiplos itens.
* No entanto, se essas listas crescerem demais, a tabela perde eficiência.

Por isso, é essencial usar uma **boa função hash**: ela gera **menos colisões** e garante um desempenho melhor.

Se evitarmos colisões, a tabela hash operará sempre no melhor caso: **O(1)**.

---

## Fator de Carga

O **fator de carga** indica o quão cheia está a tabela hash. É calculado como:

```
Fator de carga = Número total de itens / Número total de posições na tabela
```

* Se o fator de carga for **maior que 1**, há **mais itens do que espaços disponíveis**, o que aumenta a chance de colisões.
* Quando o fator de carga ultrapassa **0.7**, é recomendado **redimensionar** a tabela.

### Como redimensionar:

1. Dobrar o tamanho do array original.
2. Recalcular os índices de todos os itens com a nova função hash.
3. Re-inserir os itens na nova tabela.

⚠️ O redimensionamento é um processo **caro**, então deve ser feito **com moderação**.
