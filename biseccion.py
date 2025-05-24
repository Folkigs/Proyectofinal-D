import math
import numpy as np
import matplotlib.pyplot as plt

def funcion(x):
    return 2*x * np.cos(2*x) - (x + 1)**2

def imprimir_iteracion(iteracion, a, b, c, error):
    print(f"Iteración {iteracion}: Xa = {a}, Xb = {b}, Xc = {c}, Error relativo = {error}")

def biseccion(a, b, f, iteraciones):
    if f(a) * f(b) > 0:
        print("El intervalo no es válido")
        return None
    
    c = (a + b) / 2
    error = None
    for i in range(1, iteraciones + 1):
        prev_c = c
        c = (a + b) / 2
        if i > 1:
            error = abs((c - prev_c) / c) * 100
        imprimir_iteracion(i, a, b, c, error if error is not None else "N/A")
        if f(c) == 0:
            return c
        if f(a) * f(c) > 0:
            a = c
        else:
            b = c
    
    return c

def graficar_funcion(a, b, f, raiz):
    x = np.linspace(a, b, 400)
    y = f(x)
    
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label='f(x) = 2x cos(2x) - (x + 1)^2')
    plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
    plt.scatter(raiz, f(raiz), color='red', zorder=3, label=f'Raíz estimada: {round(raiz, 5)}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.title('Gráfica de la función y la raíz estimada')
    plt.grid()
    plt.show(block=True)

a = float(input("Dame Xa: "))
b = float(input("Dame Xb: "))
decimales = int(input("Dime cuántos decimales quieres: "))
resultado = biseccion(a, b, funcion, 5) or a
if resultado is not None:
    print("Resultado después de 5 iteraciones: ", round(resultado, decimales))
    graficar_funcion(a, b, funcion, resultado)

