import numpy as np 

         

def matriz(N): 

    if not isinstance(N, int) or N <= 0: 

        print ("error: N debe ser un entero positivo") 

        return None 

         

    vectoooor = np.random.randint(1, 10, size =N) 

    print(f"vector generado: {vectoooor}") 

    matriz = np.array([vectoooor * (i + 1) for i in range(N)]) 

    return matriz

     

     

try: 

    N= int(input("Ingrese un numero entero positivo: ")) 

    if N > 0: 

        matrizresultado =   matriz(N) 

        if matrizresultado is not None: 

            print ("matriz resultante:") 

            print(matrizresultado) 

    else: 

            print("Error: El numero debe ser positivo") 

             

except ValueError: 

    print("Error: Ingrese un numero entero valido") 

     