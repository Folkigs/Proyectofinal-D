import numpy as np

def multiplos_fila(N, vector):
    matriz = np.zeros((N, N),dtype=int)
    for i in range(N):
        for j in range(N):
            matriz[i, j] = vector[i] * (j + 1)
    return matriz

def multiplos_columna(N, vector):
    matriz = np.zeros((N, N), dtype=int)
    for j in range(N):
        for i in range(N):
            matriz[i, j] = vector[j] * (i + 1)
    return matriz

vector = np.array([4, 3, 1])
N = len(vector)
matriz_fila = multiplos_fila(N, vector)
matriz_columna = multiplos_columna(N, vector)

print("matriz con multiplos en filas:")
print(matriz_fila)
print("\nMatriz con multiplos en columnas:")
print(matriz_columna)