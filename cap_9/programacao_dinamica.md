# Programação Dinâmica

A **Programação Dinâmica (PD)** é uma técnica de otimização utilizada na resolução de problemas complexos, dividindo-os em subproblemas menores e resolvendo cada um deles apenas uma vez, armazenando os resultados para evitar retrabalho.

Ela é especialmente útil em problemas onde a solução ótima pode ser construída a partir das soluções ótimas de subproblemas menores. Ou seja, quando o problema apresenta **subestrutura ótima** e **sobreposição de subproblemas**.

---

## Como funciona a Programação Dinâmica?

1. **Divisão em subproblemas:** O problema original é decomposto em partes menores.
2. **Armazenamento de resultados:** Os resultados das subpartes são armazenados, geralmente em uma **tabela (matriz ou vetor)**.
3. **Construção da solução final:** A partir dos subproblemas resolvidos, é construída a solução do problema maior.

---

## Estrutura Geral

* A solução envolve **uma tabela com linhas e colunas**, onde cada célula representa um subproblema.
* **A ordem das linhas/colunas pode variar** sem afetar a resposta final, desde que a lógica de preenchimento seja respeitada.
* **Itens menores ou adicionais podem exigir redefinir a tabela**, pois eles afetam os subproblemas.

---

## Características Importantes

* **Não é possível trabalhar com frações de itens** (ex: em problemas como a Mochila 0/1). É tudo ou nada.
* A PD **só funciona bem quando os subproblemas são discretos**, ou seja, podem ser resolvidos independentemente.
* **Nem sempre a solução ótima usa toda a capacidade disponível** (ex: em problemas com restrição de peso ou tempo).
* A técnica é muito usada para **otimização sob restrições** (tempo, espaço, peso, custo etc).

---

## Dicas para Resolver Problemas com Programação Dinâmica

1. **Identifique os subproblemas**: Qual é a menor versão do problema?
2. **Crie a tabela**: Decida o que cada linha e coluna representam.
3. **Defina a relação de recorrência**: Como o valor de uma célula depende dos outros?
4. **Inicialize corretamente**: Comece preenchendo os casos base.
5. **Preencha a tabela passo a passo**, garantindo que os subproblemas anteriores estejam resolvidos antes de usá-los.

> **Obs:** Não existe uma fórmula única para resolver todos os problemas com PD. A abordagem depende do problema específico.

---

## Problemas Clássicos que Utilizam PD

* Problema da Mochila 0/1
* Fibonacci otimizado
* Subsequência comum mais longa (LCS)
* Cadeamento de matrizes
* Soma de subconjunto
* Caminho mínimo em matriz
* Corte de hastes (rod cutting)
