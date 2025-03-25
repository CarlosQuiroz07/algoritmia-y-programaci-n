"""
El programa solicita la altura de N estudiantes y determina cuál es la mayor de todas.
"""
num_estudiantes = input("Cantidad estudiantes: ")
max_altura = 0
N = int(num_estudiantes)

for i in range(N):
    altura = float(input("Ingrese la altura del estudiante: "))
    if altura > max_altura:
        max_altura = altura


print(f"La mayor altura registrada es: {max_altura}")
