# QuickSort

- QuickSort é um **algoritmo de ordenação** eficiente.
- É geralmente **mais rápido que o algoritmo de ordenação por seleção (Selection Sort)**.
- Utiliza a estratégia de **divisão e conquista**.
- É um dos algoritmos de ordenação **mais rápidos na prática**.

## Como funciona o QuickSort

1. **Escolha um pivô** (um elemento do array).
2. **Particione** o array em dois subarrays:
   - Um com os elementos **menores que o pivô**.
   - Outro com os elementos **maiores que o pivô**.
3. **Aplique o QuickSort recursivamente** em ambos os subarrays.

### Complexidade

- **Melhor caso:** O(n log n)  
- **Pior caso:** O(n²) (ocorre quando o pivô escolhido é sempre o maior ou menor elemento)

> ⚠️ A complexidade do QuickSort depende fortemente da **entrada de dados** e da **escolha do pivô**.

- Quando usamos **um pivô fixo**, o pior caso é O(n²).
- Com a escolha de um **pivô aleatório**, o algoritmo tende a manter a complexidade **O(n log n)** mesmo nos piores cenários com alta probabilidade.

📌 **Na prática**, o QuickSort costuma ser **mais rápido que o Merge Sort**, mesmo ambos tendo complexidade O(n log n), devido à sua menor utilização de memória.

---

# Revisão Rápida: 
## ➤ List Comprehension

📌 **O que é List Comprehension?**  
É uma forma **concisa e eficiente** de criar listas em Python, substituindo estruturas como `for` e `append()`.

### Sintaxe Básica:

```python
[expressão for item in iterável if condição]
```

- **expressão**: O valor que será inserido na nova lista (pode ser o próprio `item` ou uma transformação dele).
- **item**: A variável que representa cada elemento do iterável.
- **condição** *(opcional)*: Um filtro que determina quais elementos serão incluídos na lista.

---
# 📌 Exemplo Prático: List Comprehension

### 1. Criar uma lista de quadrados de 0 a 9:

```python
quadrados = [x**2 for x in range(10)]
print(quadrados)  # Saída: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### 2. Filtrar apenas os números pares de uma lista:

```python
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [x for x in numeros if x % 2 == 0]
print(pares)  # Saída: [2, 4, 6, 8, 10]
```

### 3. Transformar uma lista de strings em letras maiúsculas:

```python
palavras = ["python", "é", "legal"]
maiusculas = [palavra.upper() for palavra in palavras]
print(maiusculas)  # Saída: ['PYTHON', 'É', 'LEGAL']
```