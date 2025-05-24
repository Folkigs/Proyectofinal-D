def tengosueño():
    
    try:
      
        N = int(input("ingrese un numero entero positivo: "))
     
        if N > 0:
          
            print (f"El numero ingresado es {N}")
        else:
          
            print("Error: El numero debe ser entero positivo")
    except ValueError:
       
        
       
        print ("Error : La entrada no es un numero entero xD")

tengosueño()