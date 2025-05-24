import numpy as np
import matplotlib.pyplot as plt

x_cuad = [2, 3, 5]
y_cuad = [6, 19, 99]


x = 4  

L0 = ((x - x_cuad[1]) * (x - x_cuad[2])) / ((x_cuad[0] - x_cuad[1]) * (x_cuad[0] - x_cuad[2]))
L1 = ((x - x_cuad[0]) * (x - x_cuad[2])) / ((x_cuad[1] - x_cuad[0]) * (x_cuad[1] - x_cuad[2]))
L2 = ((x - x_cuad[0]) * (x - x_cuad[1])) / ((x_cuad[2] - x_cuad[0]) * (x_cuad[2] - x_cuad[1]))

resultado_cuad = y_cuad[0] * L0 + y_cuad[1] * L1 + y_cuad[2] * L2

print("\nInterpolación Cuadrática:")
print("El valor estimado de f(4) es:", resultado_cuad)


valores_x = np.linspace(2, 5, 100)
valores_y = []
for xi in valores_x:
    L0 = ((xi - x_cuad[1]) * (xi - x_cuad[2])) / ((x_cuad[0] - x_cuad[1]) * (x_cuad[0] - x_cuad[2]))
    L1 = ((xi - x_cuad[0]) * (xi - x_cuad[2])) / ((x_cuad[1] - x_cuad[0]) * (x_cuad[1] - x_cuad[2]))
    L2 = ((xi - x_cuad[0]) * (xi - x_cuad[1])) / ((x_cuad[2] - x_cuad[0]) * (x_cuad[2] - x_cuad[1]))
    yi = y_cuad[0] * L0 + y_cuad[1] * L1 + y_cuad[2] * L2
    valores_y.append(yi)

plt.figure()
plt.plot(x_cuad, y_cuad, 'ro', label='Puntos dados')
plt.plot(valores_x, valores_y, label='Interpolación cuadrática')
plt.title('Interpolación Cuadrática')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()