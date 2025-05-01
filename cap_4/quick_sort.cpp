QUICKSORT(A, p, r)
  if p < r
      q = PARTITION(A, p, r)  // q é o índice do pivô após o particionamento
      QUICKSORT(A, p, q - 1)  // Ordena a sublista à esquerda do pivô
      QUICKSORT(A, q + 1, r)  // Ordena a sublista à direita do pivô

PARTITION(A, p, r)
  x = A[r]  // Pivô (último elemento)
  i = p - 1 // Índice do menor elemento
  for j = p to r - 1
      if A[j] ≤ x
          i = i + 1
          trocar A[i] com A[j]  // Move elementos menores para a esquerda
  trocar A[i + 1] com A[r]      // Posiciona o pivô corretamente
  return i + 1                  // Retorna o índice do pivô