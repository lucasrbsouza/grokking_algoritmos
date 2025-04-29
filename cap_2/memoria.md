# Como funciona a Memoria
Quando queremos armazenar algo, pedimos para o computador e o computador nos libera um espaço 
e nos retorna o endereco de memoria
se quisermo armazenar mais de um item usamos arrays ou listas

## Array 
Um array significa que todas as tarefas serão armazenados um do lado do outra (contiguamente)
- se for armazenar dez itens esse dez itens precisam estar lado a lado, se caso no 8 espaço 
ele tiver ocupado, será necessario mover os itens para todos caberem
- por isso adicionar um item no array pode ser muito lento
- no entando podemos pedir para o compurtador reservar 10 lugares para adicionarmos os items,
ai podemos adicionar os items numa boa, porem se aparecer mais um item precisariamos mover novamente

Desvantagens do array:
- pode ser que os espaços que a gente reservou seja ou mais que suficiente ou insuficiente
- se houver mais espços reservados do que items, esses epaços não podem ser ocupados por outra coisa; 
não estaremos usando a memoria, porem ninguem utilizara também
- se for insuficiente, vai ser preciso mover os items novamente para que caiba todos

Vantagems do Array
- são otimos para ler elementos aleatorios, pois ja sabemos os endereços de cada elemento
- para ler os elementos é instantaneos 
- Permite acesso aleatorio 

Leitura no Array tem complexidade de O(1)
Insercao no Array tem complexidade de O(n)
Deleção no Array tem complexidade de O(n)

## Listas Encadeadas
Na lista encadeada os items podem estar em qualquer lugar da memoria
cada item armazena o endereco do proximo item
para armazenar um item é facil:
- precisamos apenas que tenha espaço na memoria
- adicionamos os items nesses epaços, e cada item tera o endereco do proximo item
- ex: 01->786->654->02->667->0987

Vantagens:
- Na lista encadeada os items não precisam estar lado a lado, eles so precisam ser armazenados
em qualquer lugar da memoria e ter o endereço do proximo item da lista
- São melhores para inserir elementos no meio de uma lista, so basta mudar o endereço
- São melhores para deleções, so basta mudar o endereço

Desvantagens:
- a lista encadeada é pessima para ler elementos aleatorios,
pois, justamete pelos endereços dos items serem qualquer endereço de memoria, nos temos que passar
por cada item para saber o endereço do proximo item, até chegar no elemento que desejamos
- So permite acesso sequencial (leitura passando por todos os elementos da lista, um por um)

Leitura na lista tem complexidade de O(n)
Insercao na lista tem complexidade de O(1)
Delecao na lista tem complexidade de O(1)