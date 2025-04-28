# 🔍 O que é Pesquisa Binária?

A pesquisa binária é um método eficiente para encontrar um elemento em uma lista ordenada. Em vez de verificar cada item um por um, como na busca linear, ela divide a lista ao meio repetidamente para localizar o valor desejado.

## 🧠 Como Funciona?

1. **Início**: Você tem uma lista ordenada e deseja encontrar um número específico.  
2. **Passo 1**: Compare o número do meio da lista com o número que você procura.  
   - Se forem iguais, você encontrou o número!  
   - Se o número procurado for **menor**, concentre-se na metade **esquerda** da lista.  
   - Se for **maior**, concentre-se na metade **direita**.  
3. **Repetição**: Repita o processo com a nova metade selecionada.  
4. **Conclusão**: Continue dividindo até encontrar o número ou até que a sublista esteja vazia (o que significa que o número não está na lista).  

## 📘 Exemplo Prático

Imagine a lista: `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`  
Você quer encontrar o número **7**.  

- **Primeira verificação**: O número do meio é **5**. Como **7** é maior, ignore os números menores que **5**.  
  - Nova lista: `[6, 7, 8, 9, 10]`  
- **Segunda verificação**: O número do meio agora é **8**. Como **7** é menor, ignore os números maiores que **8**.  
  - Nova lista: `[6, 7]`  
- **Terceira verificação**: O número do meio é **7**. Bingo! Número encontrado.  

## ⚡ Por que é Eficiente?

Porque a cada passo, você elimina **metade da lista**. Isso significa que, mesmo em listas muito grandes, você precisa de poucas verificações para encontrar o número.  

**Exemplo**:  
- Em uma lista de **1.000 elementos**, são necessárias no máximo cerca de **10 verificações**.  

## ✅ Lembre-se

- A lista **deve estar ordenada** para que a pesquisa binária funcione corretamente.  
- É **muito mais rápida** que a busca linear em listas grandes.  
