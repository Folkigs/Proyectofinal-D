import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 8 * x * np.sin(x) * np.exp(-x) - 1

def metodo_secante(f, x0, x1, tol=1e-4, max_iter=5):
    print(f"{'Iteración':<10}{'x_n-1':<15}{'x_n':<15}{'Error Relativo (%)':<15}")
    print("_" * 60)
    
    iteraciones = []
    
    for i in range(1, max_iter + 1):
        if abs(f(x1) - f(x0)) < 1e-12:
            print("División por cero detectada. Deteniendo el cálculo.")
            return
        
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        error_rel = abs((x2 - x1) / x2) * 100 if x2 != 0 else abs(x2 - x1) * 100
        
        print(f"{i:<10}{x0:<15.6f}{x1:<15.6f}{error_rel:<15.6f}")
        iteraciones.append(x2)
        
        if error_rel < tol:
            break
        
        x0, x1 = x1, x2
    
   

    x_vals = np.linspace(-1, 1, 400)
    y_vals = f(x_vals)

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label='f(x) = 8x sin(x) e^(-x) - 1', color='b')
    plt.axhline(0, color='black', linestyle='--')
    plt.axvline(0, color='black', linestyle='--')
    plt.scatter(iteraciones, [f(x) for x in iteraciones], color='red', label='Aproximaciones')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.title('Método de la Secante - Aproximaciones')
    plt.show()

metodo_secante(f, -0.3, 0.5)
