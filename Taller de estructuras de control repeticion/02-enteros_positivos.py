"""
El programa imprime todos los números impares menores que 100, excepto aquellos que sean divisibles por 7.
"""
for i in range(1, 100, 1):
    if (i % 2 == 1 and i % 7 != 0):
        print(i)
