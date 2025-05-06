# Algoritmos Gulosos

Os **algoritmos gulosos** são uma forma inteligente e rápida de resolver certos problemas. Eles funcionam escolhendo, a cada passo, a **melhor opção disponível no momento**, sem pensar no futuro.

> ⚠️ Nem sempre essa escolha leva à melhor solução possível, mas muitas vezes o resultado é **muito bom** e o algoritmo é **bem mais rápido** do que outros métodos.

### Como funciona um algoritmo guloso?

1. Você tem um problema.
2. Em cada etapa, faz a melhor escolha local (a que parece melhor naquele momento).
3. Quando termina, espera-se que essa sequência de boas escolhas gere uma boa solução final.

---

## Vantagens dos Algoritmos Gulosos

* São **fáceis de entender** e de **programar**.
* Costumam ser **rápidos**, mesmo para problemas grandes.
* Funcionam muito bem em várias situações do dia a dia.

---

## Algoritmos de Aproximação

Quando um problema é muito difícil e **levaria muito tempo para achar a melhor resposta**, usamos os **algoritmos de aproximação**.

Eles não garantem a melhor solução, mas conseguem uma **solução parecida** de forma **muito mais rápida**.

### O que faz um bom algoritmo de aproximação?

* Ele **roda rápido**, mesmo com muitos dados.
* A solução que ele encontra está **perto da melhor possível** (às vezes 90%, 95%, ou até mais!).

---

## Problemas NP-Completos

Alguns problemas são tão difíceis que ninguém descobriu um jeito de resolvê-los rapidamente. Esses são os **problemas NP-completos**.

### Exemplos famosos:

* **Caixeiro Viajante**: Qual é o menor caminho que visita todas as cidades uma vez e volta ao ponto inicial?
* **Cobertura de Conjuntos**: Qual o menor número de grupos que cobre todos os elementos de um conjunto?

Esses problemas são tão difíceis que até hoje **não existe um algoritmo eficiente que resolva todos os casos rapidamente**.

---

### Como saber se um problema é NP-completo?

Aqui vão algumas pistas:

* O problema **fica muito lento** quando aumentamos a quantidade de dados.
* Envolve testar **todas as combinações possíveis**.
* Você **não consegue dividir o problema em partes menores** mais simples.
* Ele pode ser reescrito como um problema famoso, como o do caixeiro viajante ou o da cobertura de conjuntos.

---

# Exemplos Práticos e Passo a Passo

## Exemplo 1: Troco com Menor Número de Moedas

### Problema:

Você precisa dar troco usando o menor número de moedas possível.
Moedas disponíveis: **1, 5, 10, 25 centavos**.
Valor a devolver: **63 centavos**.

### Passos:

1. Escolha a maior moeda que caiba no valor restante.
2. Subtraia o valor dessa moeda.
3. Repita até o valor chegar a 0.

### Solução:

* 2 moedas de 25 centavos = 50
* 1 moeda de 10 centavos = 60
* 3 moedas de 1 centavo = 63
  **Total**: 6 moedas

✅ Essa foi a **melhor solução possível** nesse caso.

> ⚠️ Mas cuidado! Esse método **não funciona com qualquer conjunto de moedas**. Com moedas de 1, 3 e 4 centavos, por exemplo, ele pode errar.

---

## Exemplo 2: Problema da Cobertura de Conjuntos

### Problema:

Você tem um conjunto de coisas para cobrir, e vários grupos que cobrem partes dessas coisas. Quer usar o **menor número de grupos possível** para cobrir tudo.

### Exemplo:

Queremos cobrir os itens `{1, 2, 3, 4, 5}`.
Temos os grupos:

* A = {1, 2}
* B = {2, 3, 4}
* C = {4, 5}

### Passos:

1. Escolha o grupo que cobre **mais itens ainda não cobertos**.
2. Marque esses itens como cobertos.
3. Repita até que todos os itens estejam cobertos.

### Solução:

* Primeiro escolhemos o grupo B → cobre 2, 3, 4
* Depois o grupo A → cobre 1
* Por fim o grupo C → cobre 5
  **Grupos usados**: B, A, C

✅ Todos os itens estão cobertos com **3 grupos**.

> Essa é uma **solução próxima da ideal**, e o método guloso foi rápido!

---

## Quando usar algoritmos gulosos?

Use quando:

* O problema permite tomar decisões locais que levam a uma boa solução.
* Você quer uma **solução rápida e boa o suficiente**.
* A resposta **exata é muito difícil de conseguir**.

---