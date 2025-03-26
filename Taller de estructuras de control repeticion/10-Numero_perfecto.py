"""
Un número perfecto es aquel cuya suma de sus divisores propios (excluyendo el número en sí) es igual al mismo número. 
Por ejemplo, 6 es un número perfecto porque sus divisores propios son 1, 2 y 3, y 1 + 2 + 3 = 6.
"""

numero = int(input("Ingrese un número para verificar si es perfecto: "))
suma = 0  

for i in range(1, numero):
    if numero % i == 0:
        suma += i  

if suma == numero:
    print(f"{numero} es un número perfecto.")
    if numero == 6: 
            print(f"numero perfecto {numero}: {i-4} + {i-3} + {i-2} = {numero}")
    elif numero == 28:
            print(f"numero perfecto {numero}: {i-26} + {i-25} + {i-23} + {i-20} + {i-13} = {numero}")
else:
    print(f"{numero} no es un número perfecto.")
#solo se validara  de forma especifica el 6 y el 28