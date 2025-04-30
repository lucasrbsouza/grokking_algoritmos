# 🌀 Recursão

**Recursão** é quando uma função chama a si mesma para resolver um problema.

Para que uma função recursiva funcione corretamente, ela precisa de **dois casos essenciais**:

- **Caso base**: condição que encerra a recursão.
- **Caso recursivo**: parte em que a função chama a si mesma com um problema menor.

Sem o caso base, a função recursiva entraria em um **loop infinito**, consumindo toda a memória da pilha.

---

## 🧩 Caso Base

O **caso base** é a condição de parada da função recursiva. Sem ele, a função nunca deixará de se chamar.

---

## 🔁 Caso Recursivo

O **caso recursivo** é a parte do código onde a função se chama novamente, com um parâmetro modificado (geralmente mais próximo do caso base).

---

## 🧱 Pilha de Execução

A **pilha** é uma estrutura de dados do tipo LIFO (Last In, First Out), ou seja, o **último a entrar é o primeiro a sair**.

A recursão utiliza a pilha de chamadas da linguagem de programação para armazenar cada chamada da função. A cada nova chamada, um novo item é colocado no topo da pilha. Quando o caso base é alcançado, os itens começam a ser removidos da pilha na ordem inversa.

### Operações típicas em pilhas:

- `push`: insere um item no topo da pilha.
- `pop`: remove e retorna o item do topo da pilha.

Embora usar a pilha seja útil, **guardar todas as chamadas recursivas pode consumir muita memória**, especialmente para problemas grandes.

---

## 🤔 Recursão vs. Laços

Muitas vezes, **usar loops (`for`, `while`) é mais eficiente que a recursão**, tanto em desempenho quanto em consumo de memória.

No entanto, **entender e saber usar recursão é uma habilidade valiosa**, especialmente porque muitos algoritmos importantes dependem dela, como:

- Algoritmos de **divisão e conquista**
- **Quicksort**
- **Merge sort**
- Algoritmos em **árvores e grafos**

---

## 💡 Exemplo de Recursão: Fatorial

O fatorial de um número `n` (representado por `n!`) é definido como:

```
n! = n × (n - 1) × (n - 2) × ... × 1
```

### Implementação recursiva em Python:

```python
def fatorial(n):
    # Caso base: fatorial de 0 é 1
    if n == 0:
        return 1
    # Caso recursivo: n * fatorial de (n-1)
    else:
        return n * fatorial(n - 1)

# Exemplo de uso
print(fatorial(5))  # Saída: 120
```