"""
El programa calcula la suma de todos los números pares en el rango de 97 a 1003.
"""
suma = 0
for i in range(97, 1004, 1):
    if i % 2 == 0:
          suma += i
          print(suma)
print(suma)
