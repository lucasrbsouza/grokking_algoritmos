# Algoritmo K-Vizinhos Mais Próximos (K-Nearest Neighbors - KNN)

O algoritmo **K-Vizinhos Mais Próximos**, conhecido pela sigla **KNN** (*K-Nearest Neighbors*), é um dos algoritmos mais simples e eficazes de **aprendizado supervisionado**. Ele pode ser utilizado tanto para **classificação** quanto para **regressão**, dependendo do problema que estamos tentando resolver.

## O que é o KNN?

O KNN funciona com base em uma ideia bastante intuitiva: **dado um ponto desconhecido, o algoritmo verifica quais são os "K" pontos mais próximos a ele em um conjunto de dados conhecido, e utiliza essa informação para prever a classe ou o valor do ponto desconhecido.**

Ou seja, se queremos classificar um novo ponto, o KNN olha para os "K" pontos mais próximos dele e decide com base na maioria das classes desses vizinhos.

## Aplicações do KNN

* **Classificação**: O KNN é frequentemente usado para classificar um item em um grupo (ou classe) com base nas classes dos seus vizinhos mais próximos.
* **Regressão**: Também é possível usar o KNN para prever valores contínuos (números), estimando a média dos valores dos vizinhos mais próximos.

### Exemplos

* Classificação: Determinar se um e-mail é "spam" ou "não spam" com base em e-mails já rotulados.
* Regressão: Estimar o preço de uma casa com base nas características de casas vizinhas (metragem, número de quartos, localização etc).

## Como o KNN funciona?

1. **Escolher o valor de K** (número de vizinhos).
2. **Calcular a distância** entre o ponto desconhecido e todos os pontos do conjunto de dados.
3. **Selecionar os K pontos mais próximos** (com menor distância).
4. **Fazer a predição**:

   * **Classificação**: considerar a classe mais comum entre os K vizinhos.
   * **Regressão**: calcular a média dos valores dos K vizinhos.

## Cálculo da Distância

Para comparar os pontos, é necessário calcular a **distância** entre eles. A fórmula mais comum é a **distância Euclidiana**, que mede a "reta" entre dois pontos no espaço:

$$
d(p, q) = \sqrt{(p_1 - q_1)^2 + (p_2 - q_2)^2 + \ldots + (p_n - q_n)^2}
$$

Outras métricas de distância que também podem ser usadas:

* Distância de Manhattan
* Distância de Minkowski
* Distância de Hamming (para dados categóricos)

## Exemplo simples de classificação

Imagine que queremos saber se uma fruta é **maçã** ou **laranja**, com base no **peso** e na **textura**.

Temos estes dados:

| Peso | Textura   | Fruta   |
| ---- | --------- | ------- |
| 150g | Lisa      | Maçã    |
| 170g | Lisa      | Maçã    |
| 140g | Irregular | Laranja |
| 130g | Irregular | Laranja |

Agora aparece uma fruta nova com 160g e textura lisa.
O KNN olha para as frutas mais próximas (por peso e textura) e vê que a maioria é maçã.
**Resultado: é uma maçã.**
---

## Como escolher o melhor K?

Não existe um valor mágico.
O ideal é **testar vários valores** e escolher o que dá o melhor resultado no seu caso.
Um valor comum de teste é **K = 3 ou 5**.

---

## Dica extra: normalização dos dados

Se os seus dados têm escalas muito diferentes (ex: peso em gramas e altura em metros), isso pode atrapalhar o KNN.
**Normalizar** é transformar todos os dados para ficarem na mesma escala. Isso ajuda o algoritmo a funcionar melhor.


## Vantagens do KNN

* Fácil de entender e implementar.
* Não faz suposições sobre os dados (modelo não paramétrico).
* Bom desempenho com conjuntos de dados pequenos e bem distribuídos.

## Desvantagens do KNN

* **Lento com grandes volumes de dados**, pois precisa calcular a distância de todos os pontos.
* **Sensível a dados irrelevantes ou escalas diferentes**, por isso é importante normalizar os dados.
* Escolha do valor de **K** pode afetar muito o desempenho:

  * K muito pequeno: modelo sensível ao ruído.
  * K muito grande: pode gerar predições incorretas.

## Considerações Finais

O algoritmo KNN é uma excelente escolha para problemas de classificação e regressão quando se busca uma solução simples e intuitiva. No entanto, é importante realizar uma boa preparação dos dados (normalização, remoção de outliers, seleção de atributos relevantes) para obter bons resultados.


---

## Conclusão

O KNN é ótimo para começar a aprender sobre algoritmos de machine learning.
É simples, fácil de implementar e funciona bem em muitos casos do mundo real, como reconhecimento de imagem, diagnósticos médicos e sistemas de recomendação.
