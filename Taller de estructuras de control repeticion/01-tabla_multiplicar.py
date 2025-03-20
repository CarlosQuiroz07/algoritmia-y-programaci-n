"""
El programa solicita un número al usuario y muestra su tabla de multiplicar del 1 al 10.

"""
num = int(input(" ingrese un numero para hacer la respectiva tabla "))
for i in range(1, 11, 1):
    print(f"numero {num} x {i} = {num*i}")
