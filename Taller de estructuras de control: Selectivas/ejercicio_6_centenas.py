#entrada
A=int(input("Ingrese el dígito A: "))
B=int(input("Ingrese el dígito B: "))
C=int(input("Ingrese el dígito C: "))
D=int(input("Ingrese el dígito D: "))
N = A * 1000 + B * 100 + C * 10 + D
N_redondeado=round(N, -2)
print(f"Número original: {N}")
print(f"Número redondeado a la centena más cercana: {N_redondeado}")