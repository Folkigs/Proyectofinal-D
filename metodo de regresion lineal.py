
import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6]
y = [5.04, 8.12, 10.64, 13.18, 16.20, 20.04]

x_np = np.array(x)
y_np = np.array(y)

n = len(x)
sum_x = sum(x)
sum_y = sum(y)
sum_xy = sum([x[i] * y[i] for i in range(n)])
sum_x2 = sum([x[i] ** 2 for i in range(n)])

a1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a0 = (sum_y - a1 * sum_x) / n

print("La ecuación de la recta es: f(x) = {:.3f} + {:.3f}x".format(a0, a1))

x_linea = np.linspace(1, 6, 100)
y_linea = a0 + a1 * x_linea

plt.plot(x, y, 'o', label='Datos originales')  # puntos
plt.plot(x_linea, y_linea, 'r-', label='Recta de regresión')  # línea
plt.title('Regresión lineal por mínimos cuadrados')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
