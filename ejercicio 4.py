import numpy as np
def matriz(vector):
    N = len(vector)
    matriz = np.zeros( (N, N), dtype=int)
                      
    for j in range(N):
        for i in range(N):
            matriz[i,j] = vector[j] * (i + 1)

    return matriz


vector = np.array([1, 2, 3])
matrizresultante = matriz(vector)
print(matriz)