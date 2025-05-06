# Algortimos gulosos
a beleza dos algoritmos gulosos é que eles são faceis 
Em termos tecnicos:
- um algoritmo guloso em cada etapa escolhe- se a solucao ideal
- no fim voce tem um solucao global

é importante lembrar que o algoritmo guloso não oferece a melhor solucao aqui, mas oferece um valor bem proximo
mas, um algoritmo guloso são simples de escrever e normalmente chegam bem perto da solucao perfeita

## Algoritmo de aproximaxao
 quando é necessario muito tempo para calcular a solucao exaa, um algoritmo de aproximcao é uma boa idea e funciona
 algortimo de aproximacao são avaliado:
 - por sua rapidez
 - pela capacidade de chegar a solucao ideal

## Problemas np-completos
O problema do caixeiro viajante, quanto o problema de cobertura de conjutos são problemas np-completos

como saber se um problema é np-completo:
não há uma maneira facil de dizer se um problema é np-completo
porem há alguns indicativos:
- Se o algoritmo roda rapido pra alguns itens, mas fica muito lento com o aumento de itens
- "Todas a combinacoes de X" geralmenrte significam um problema np-completo
- Quando tem que caculucar "cada possivel versao" porque não pode subdividr em problemas menores
- Se o probelma envolve uma sequencia (como no caixeiro viajante) e é dificil de resolver
- se pode reescrever o problema de cobertura minima de conjuntos ou o problema do caixeiro viajante