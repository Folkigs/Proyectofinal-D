import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 8 * x * np.sin(x) * np.exp(-x) - 1

def df(x):
    return 8 * np.exp(-x) * (np.sin(x) + x * (np.cos(x) - np.sin(x)))

def newtonraphson(x0, im, n):
    print("Iteracion  | x0          | Er")
    print("______________________________________")
    results = []
    for i in range(n):
        x1 = x0 - f(x0) / df(x0)
        error = abs((x1 - x0) / x1)*100 if x1 != 0 else 0
        print(f"{i+1:<10} | {x0:<10.6f} | {error:<10.6f}")
        print("--------------------------------------")
        results.append((i+1, x0))
        if abs(x1 - x0) < im:
            break
        x0 = x1
    return results

x0 = 0.03
iterations = 5
results = newtonraphson(x0, 0.01, iterations)

x = np.linspace(-1, 3, 400)
y = f(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$f(x) = 8x\sin(x)e^{-x} - 1$', color='blue')
plt.axhline(0, color='black', linewidth=1, linestyle='--')

for i, x_i in results:
    plt.scatter(x_i, f(x_i), color='red')
    plt.text(x_i, f(x_i), f'  x{i}', verticalalignment='bottom')

plt.title("Método de Newton-Raphson")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()
