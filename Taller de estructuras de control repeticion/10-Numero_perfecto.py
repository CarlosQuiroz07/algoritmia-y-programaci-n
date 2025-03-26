"""
Un número perfecto es aquel cuya suma de sus divisores propios (excluyendo el número en sí) es igual al mismo número. 
Por ejemplo, 6 es un número perfecto porque sus divisores propios son 1, 2 y 3, y 1 + 2 + 3 = 6.
"""
Numero = int(input("Numero y validar si es perfecto o no: "))
suma = 0  

for i in range(1, Numero):
    if Numero % i == 0:
        suma += i
    
if suma == Numero:    
    print(f"El numero {Numero} es perfecto")
    
    if Numero == 6: 
        print(f"numero perfecto {Numero}: 1 + 2 + 3 = {Numero}")
    elif Numero == 28:
        print(f"numero perfecto {Numero}: 1 + 2 + 4 + 7 + 14 = {Numero}")
else:
    print(f"El numero {Numero} no es perfecto")
    print(f"Suma de divisores: {suma}")