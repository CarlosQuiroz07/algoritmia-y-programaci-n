#entrada
lecturanterior=int(input("introduzca cual fue la lectura anterior:"))
Lecturactual=int(input("introduzca  cual fue la lectura actual:"))
aseourbano=int(input("dijite la tarifa fija del aseo urbana:"))
valorlecturas=(lecturanterior-Lecturactual)
if(valorlecturas>0 and valorlecturas<=100):
    print("el valor de la lectura esta de 0 - 100 lo que equivale a 4.600COP por KW/H")
    monto=(valorlecturas*4600)/60
    print(f"el valor del monto por la lectura por el costo es de:{monto}")
    print(f"el valor de LA TERIFA FIJA DEL ASEO URBANO ES DE: {aseourbano}")
elif(valorlecturas>=101 and valorlecturas<=300):
    print("el valor de la lectura esta de 101 - 300 lo que equivale a 80.00COP por KW/H")
    monto=(valorlecturas*80000)/60
    print(f"el valor del monto por la lectura por el costo es de:{monto}")
    print(f"el valor de LA TERIFA FIJA DEL ASEO URBANO ES DE: {aseourbano}")
elif(valorlecturas>=301 and valorlecturas<=500):
    print("el valor de la lectura esta de 301 - 500 lo que equivale a 100.000COP por KW/H")
    monto=(valorlecturas*100000)/60
    print(f"el valor del monto por la lectura por el costo es de:{monto}")
    print(f"el valor de LA TERIFA FIJA DEL ASEO URBANO ES DE: {aseourbano}")
elif(valorlecturas>=501):
    print("como el valor excede los 501 el valor es de 120.000 COP por KW/H ")
    monto=(valorlecturas*120000)/60
    print(f"el valor del monto por la lectura por el costo es de:{monto}")
    print(f"el valor de LA TERIFA FIJA DEL ASEO URBANO ES DE: {aseourbano}")

