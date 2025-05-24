import numpy as np
import matplotlib.pyplot as plt

x_lineal = [3, 5]
y_lineal = [19, 99]

x_deseado = 4

pendiente = (y_lineal[1] - y_lineal[0]) / (x_lineal[1] - x_lineal[0])
resultado_lineal = y_lineal[0] + pendiente * (x_deseado - x_lineal[0])

print("Interpolación Lineal:")
print("El valor estimado de f(4) es:", resultado_lineal)