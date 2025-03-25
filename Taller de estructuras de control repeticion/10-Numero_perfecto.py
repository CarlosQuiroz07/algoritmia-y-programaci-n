"""
Un número perfecto es aquel cuya suma de sus divisores propios (excluyendo el número en sí) es igual al mismo número. 
Por ejemplo, 6 es un número perfecto porque sus divisores propios son 1, 2 y 3, y 1 + 2 + 3 = 6.
"""
Numero = int(input("Numero y validar si es perfecto o no:"))
suma = 0 

for i in range(1,Numero):
    divisor = Numero % i
    if divisor == 0:
        suma += 1
        if Numero == 6: 
            i_1 = i + 1
            i_2 = i + 2
            print(f"numero perfecto {Numero}: {i} + {i_1} + {i_2} = {Numero}")
        if Numero == 28:
            i_3 = i + 1
            i_4 = i + 3
            i_5 = i + 6 
            i_6 = i + 13
            print(f"numero perfecto {Numero}: {i_3} + {i_4} + {i_5} + {i_6} = {Numero}")
if suma == Numero:    
    print("El numero es perfecto")

