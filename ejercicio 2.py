import numpy as np 

  

def vectorjeje(N): 

    if not isinstance(N, int) or N <= 0: 

        print("Error: N debe ser un entero positivo") 

        return None 

    vector = np.random.randint(1, 10, size =N) 

    return vector 

try: 

    N = int(input("ingrese un numero entero positivo: 10")) 

    if N > 0: 

        vector_resultado = vectorjeje(N) 

        if vector_resultado is not None: 

            print(f"vector generado: {vector_resultado}") 

        else: 

            print("Error: El número debe ser positivo") 

except ValueError: 
        print("Error: ingrese un numero entero valido") 