"""
Un número perfecto es aquel cuya suma de sus divisores propios (excluyendo el número en sí) es igual al mismo número. 
Por ejemplo, 6 es un número perfecto porque sus divisores propios son 1, 2 y 3, y 1 + 2 + 3 = 6.
"""
Numero = int(input("Numero y validar si es perfecto o no: "))
suma = 0 

for i in range(1,Numero):
    divisor = Numero % i
    if divisor == 0:
        suma += 1
if suma == Numero:    
    print("El numero es perfecto")
if Numero == 6: 
    print(f"numero perfecto {Numero}: {i} + {i - 3} + {i - 2} = {Numero}")
if Numero == 28:
    print(f"numero perfecto {Numero}: {i - 26} + {i - 25} + {i - 23} + {i - 20} + {i - 13} = {Numero}")

