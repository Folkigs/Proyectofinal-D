import numpy as np
import matplotlib.pyplot as plt

# Definir la función
def f(x):
    return 2*x*np.cos(2*x) - (x + 1)**2

# Método de la falsa posición
def falsa_posicion(a, b, tol=1e-4, max_iter=3):
    print("\nMétodo de la Falsa Posición\n")
    print(f"{'i':<3} {'a':<10} {'b':<10} {'f(a)':<10} {'f(b)':<10} {'x':<10} {'εr':<10}")
    for i in range(1, max_iter+1):
        fa, fb = f(a), f(b)
        x = (a * fb - b * fa) / (fb - fa)
        fx = f(x)
        er = abs((x - a) / x) * 100 if i > 1 else 100  # Error relativo

        print(f"{i:<3} {a:<10.4f} {b:<10.4f} {fa:<10.4f} {fb:<10.4f} {x:<10.4f} {er:<10.4f}")

        if fx * fa < 0:
            b = x
        else:
            a = x

        if er < tol:
            break

    return x

# Intervalo inicial
a, b = -3, -2
raiz = falsa_posicion(a, b)

# Gráfica
x_vals = np.linspace(-4, 1, 100)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label='f(x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(raiz, color='r', linestyle='--', label=f'Raíz: {raiz:.4f}')
plt.legend()
plt.title("Método de la Falsa Posición")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()
