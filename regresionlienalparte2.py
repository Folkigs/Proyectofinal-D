import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("salarios.csv")

x = datos['Experience Years'].tolist()  # años de experiencia
y = datos['Salary'].tolist()            # salario

n = len(x)
sum_x = sum(x)
sum_y = sum(y)
sum_x2 = sum([xi**2 for xi in x])
sum_xy = sum([x[i] * y[i] for i in range(n)])

a1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a0 = (sum_y - a1 * sum_x) / n

print("Pendiente (a1):", round(a1, 2))
print("Ordenada al origen (a0):", round(a0, 2))

plt.scatter(x, y, color='blue', label='Datos')
x_linea = x
y_linea = [a1 * xi + a0 for xi in x_linea]
plt.plot(x_linea, y_linea, color='red', label='Recta de regresión')

plt.xlabel("Experiencia en años")
plt.ylabel("Salario")
plt.title("Regresión Lineal (sin sklearn)")
plt.legend()
plt.grid(True)
plt.show()

experiencias = [15, 30, 50]
for exp in experiencias:
    salario_estimado = a1 * exp + a0
    print(f"Salario estimado para {exp} años: {round(salario_estimado, 2)}")
