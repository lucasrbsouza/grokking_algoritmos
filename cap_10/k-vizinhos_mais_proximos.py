"""estudos sobre knn com o uso da bivlioteca knn"""
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Dados de treino
# [peso (g), textura (0 = lisa, 1 = irregular)]
X = [
    [150, 0],  # maçã
    [160, 0],  # maçã
    [130, 1],  # laranja
    [120, 1],  # laranja
]

# Rótulos (classes)
# 0 = maçã, 1 = laranja
y = [0, 0, 1, 1]

# Novo dado (fruta desconhecida)
novo_dado = np.array([[155, 0]])

# Criar modelo KNN com K=3
modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X, y)

# Previsão
resultado = modelo.predict(novo_dado)
print("Resultado:", "Maçã" if resultado[0] == 0 else "Laranja")

# Visualização
cores = ['red' if label == 0 else 'orange' for label in y]
for i in range(len(X)):
    plt.scatter(X[i][0], X[i][1], color=cores[i], label="Maçã" if y[i] == 0 else "Laranja")

# Ponto novo (predição)
plt.scatter(novo_dado[0][0], novo_dado[0][1], color='blue', marker='*', s=200, label="Fruta Desconhecida")

plt.xlabel("Peso (g)")
plt.ylabel("Textura (0 = Lisa, 1 = Irregular)")
plt.title("Classificação com KNN")
plt.legend()
plt.grid(True)
plt.show()
