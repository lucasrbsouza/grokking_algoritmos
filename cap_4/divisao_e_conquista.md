# Divisao e conquista (DC)
Para resolver um algoritmo de Divisão e conquista devemos seguir dois passos:
 1) determinar o caso base, que é o caso mais simples possível
 2) dividir ou diminuir o problema ate ele se transformar no caso base

Algoritmo de DC, além de ser um algoritmo é também uma maneira pensar sobre um problema

Dica: o caso base de um array, será muitas das vezes 1 ou um array vazio

````
    Exemplo com soma([2, 3, 4]):
    Primeira chamada:
    lista = [2, 3, 4]
    → 2 + soma([3, 4])
    
    Segunda chamada:
    lista = [3, 4]
    → 3 + soma([4])
    
    Terceira chamada:
    lista = [4]
    → 4 + soma([])
    
    Quarta chamada:
    lista = [] → retorna 0 (caso base).
    
    Agora, volta resolvendo as somas:
    
    4 + 0 = 4
    
    3 + 4 = 7
    
    2 + 7 = 9
    
    Resultado final: 9 ✅