"""
El programa realiza la división entera de dos números utilizando restas sucesivas en lugar de la operación de división convencional.
"""
dividiendo = int(input("Dividiendo: "))
divisor = int(input("Divisor: "))
if divisor == 0:
    print("No se puede dividir por cero")
else:
    cociente = 0
    restante = dividiendo

    while restante >= divisor:
        restante -= divisor
        cociente += 1
    

residio = restante
print(f"Cociente: {cociente}")
print(f"Residuo: {restante}")
print(f"{dividiendo} ÷ {divisor} = {cociente} con residuo {restante}")
