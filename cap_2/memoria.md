# Como Funciona a Memória

Quando queremos armazenar algo, pedimos ao computador, e ele nos libera um espaço e retorna o **endereço de memória**.  
Se quisermos armazenar mais de um item, usamos **arrays** ou **listas encadeadas**.

---

## Array

Um array significa que todos os itens serão armazenados **um ao lado do outro** (de forma contígua na memória).

- Se quisermos armazenar dez itens, esses dez espaços precisam estar disponíveis lado a lado.
- Se o oitavo espaço estiver ocupado, será necessário mover os itens para outro lugar onde caibam todos.
- Por isso, **adicionar um item em um array pode ser lento**.
- Podemos pedir ao computador para reservar 10 posições de antemão, assim adicionamos os itens normalmente.
  - Mas, se precisarmos de mais espaço, teremos que mover tudo de novo para um lugar maior.

### Vantagens do Array

- Ótimos para **ler elementos aleatórios**, pois sabemos exatamente onde cada elemento está.
- Leitura é praticamente **instantânea**.
- Permite **acesso aleatório** aos elementos.

### Desvantagens do Array

- Pode haver desperdício de memória se reservamos mais espaço do que usamos.
- Se reservamos espaço de menos, teremos que mover todos os itens para outro lugar maior.
- Os espaços reservados mas não utilizados **ficam inutilizados**, não podendo ser aproveitados por outros dados.

### Complexidades no Array

- Leitura: `O(1)`
- Inserção: `O(n)`
- Deleção: `O(n)`

---

## Listas Encadeadas

Na **lista encadeada**, os itens podem estar em **qualquer lugar da memória**.  
Cada item armazena o **endereço do próximo item**.

- Para armazenar um item, basta que haja espaço em qualquer lugar.
- Adicionamos os itens nesses espaços, e cada item aponta para o próximo.
  - Exemplo: `01 -> 786 -> 654 -> 02 -> 667 -> 0987`

### Vantagens da Lista Encadeada

- Os itens **não precisam estar lado a lado**, apenas conectados pelo endereço do próximo.
- **Inserções** no meio da lista são simples: só precisamos atualizar o ponteiro.
- **Deleções** também são fáceis: basta mudar o endereço do item anterior.

### Desvantagens da Lista Encadeada

- Péssima para **ler elementos aleatórios**.
  - Precisamos **percorrer um a um** até chegar no elemento desejado.
- **Só permite acesso sequencial**.

### Complexidades na Lista Encadeada

- Leitura: `O(n)`
- Inserção: `O(1)`
- Deleção: `O(1)`

