#entrada
sueldo=int(input("cual es su sueldo base?:"))
if(sueldo<900000 and sueldo>900000):
    print("depende del valor del sueldo que agregaran los procentajes ")
elif(sueldo<900000):
    print("como el valor de del sueldo fue decreciente se sumara el 15%")
    sueldodecreciente=(sueldo*0.15)+sueldo
    print(f"el valor ahora del sueldo es: {sueldodecreciente}")
elif(sueldo*0.12):
    print("como el valor de el sueldo es de forma decreciente se suma el 12%")
    sueldocreciente=(sueldo*0.12)+sueldo
    print(f"el valor de ahora es de: {sueldocreciente}")

