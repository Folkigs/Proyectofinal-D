import numpy as np
import matplotlib.pyplot as plt

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

def graficar_funciones():
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
   
    plt.figure(figsize=(8, 6))
    plt.plot(x, y1, label='seno', color='b', linestyle='-', linewidth=2)
    plt.plot(x, y2, label='coseno', color='r', linestyle='--', linewidth=2)
    
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('grafica de funciones seno y coseno')
    plt.legend()
    plt.grid(True)
    plt.show()

vector = np.array([4, 3, 1])
N = len(vector)
matriz_fila = multiplos_fila(N, vector)
matriz_columna = multiplos_columna(N, vector)

print("matriz con multiplos en filas:")
print(matriz_fila)
print("\nMatriz con multiplos en columnas:")
print(matriz_columna)

graficar_funciones()

print("Matriz con multiplos en filas:")
print(matriz_fila)
print("\nMatriz con multiplos en columnas:")
print(matriz_columna)