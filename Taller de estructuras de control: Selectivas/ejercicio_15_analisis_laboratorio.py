#entrada
edad = int(input("Introduzca la edad del paciente en años: "))
edad1 = float(input("Ingrese la edad del paciente en meses (si es menor a 1 año): "))
sexo = int(input("Introduzca el sexo del paciente (0 para mujer, 1 para hombre): "))
nivelhemoglobina = float(input("Ingrese el nivel de hemoglobina (g%): "))

# Determinar la edad en meses si es necesario
if edad1 > 0: 
    meses = edad1
else:  
    meses = edad * 12


if(meses>=0 and meses<=1):
    print(" el valor de la edad esta entre los rangos de 0 - 1 meses")
    if 13 <= nivelhemoglobina <= 26:
        print("Negativo para anemia")
    elif nivelhemoglobina < 13:
        print("Positivo para anemia")
    else:
        print("Nivel de hemoglobina fuera de rango esperado")
if(meses>1 and meses<=6):
    print(" el valor de la edad esta entre los rangos de 1 - 6 meses")
    if 10 <= nivelhemoglobina <= 18:
        print("Negativo para anemia")
    elif nivelhemoglobina < 10:
        print("Positivo para anemia")
    else:
        print("Nivel de hemoglobina fuera de rango esperado")
if(meses>6 and meses<=12):
    print(" el valor de la edad esta entre los rangos de 6 - 12 meses")
    if 11 <= nivelhemoglobina <= 15:
        print("Negativo para anemia")
    elif nivelhemoglobina < 11:
        print("Positivo para anemia")
    else:
        print("Nivel de hemoglobina fuera de rango esperado")
if(edad>1 and edad<=5):
    print(" el valor de la edad esta entre los rangos de 1 - 5 años")
    if 11.5 <= nivelhemoglobina <= 15:
        print("Negativo para anemia")
    elif nivelhemoglobina < 11.5:
        print("Positivo para anemia")
    else:
        print("Nivel de hemoglobina fuera de rango esperado")
if(edad>5 and edad<=10):
    print(" el valor de la edad esta entre los rangos de 5 - 10 años")
    if 12.6 <= nivelhemoglobina <= 15.5:
        print("Negativo para anemia")
    elif nivelhemoglobina < 12.6:
        print("Positivo para anemia")
    else:
        print("Nivel de hemoglobina fuera de rango esperado")
if(edad>10 and edad<=15):
    print(" el valor de la edad esta entre los rangos de 10 - 15 años")
    if 13 <= nivelhemoglobina <= 15.5:
        print("Negativo para anemia")
    elif nivelhemoglobina < 13:
        print("Positivo para anemia")
    else:
        print("Nivel de hemoglobina fuera de rango esperado")
if(sexo==0):
    print("como es una mujer el valor dependera de el rango de la edad")
    if(edad>15):
        print(" el valor de la edad esta supera el rango de los 15 años ")
        if 12 <= nivelhemoglobina <= 16:
            print("Negativo para anemia")
        elif nivelhemoglobina < 12:
            print("Positivo para anemia")
        else:
            print("Nivel de hemoglobina fuera de rango esperado")
if(sexo==1):
    print("como es un hombre el valor dependera de rango de la edad ")
    if(edad>15):
        print(" el valor de la edad esta supera el rango de los 15 años ")
        if 14 <= nivelhemoglobina <= 18:
            print("Negativo para anemia")
        elif nivelhemoglobina < 14:
            print("Positivo para anemia")
        else:
            print("Nivel de hemoglobina fuera de rango esperado")
