import numpy as np
import matplotlib.pyplot as plt

# Coeficientes del polinomio f(x) = x^3 - 5x^2 + 5x - 1
coef = [1, -5, 5, -1]

# Método de Birge-Vieta
def birge_vieta(coef, x0, max_iter=3):
    print("\nMétodo de Birge-Vieta\n")
    print(f"{'i':<3} {'x':<10} {'εr':<10}")

    for i in range(1, max_iter+1):
        b = [coef[0]]
        for j in range(1, len(coef)):
            b.append(coef[j] + b[-1] * x0)

        c = [b[0]]
        for j in range(1, len(b)-1):
            c.append(b[j] + c[-1] * x0)

        x1 = x0 - (b[-1] / c[-1])  # Nueva aproximación
        er = abs((x1 - x0) / x1) * 100 if i > 1 else 100  # Error relativo

        print(f"{i:<3} {x1:<10.4f} {er:<10.4f}")

        x0 = x1  # Actualizar x0

    return x1

# Aproximación inicial
x0 = 0.8
raiz = birge_vieta(coef, x0)

# Gráfica
x_vals = np.linspace(-1, 3, 100)
y_vals = np.polyval(coef, x_vals)

plt.plot(x_vals, y_vals, label="f(x)")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(raiz, color='r', linestyle='--', label=f'Raíz: {raiz:.4f}')
plt.legend()
plt.title("Método de Birge-Vieta")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()
