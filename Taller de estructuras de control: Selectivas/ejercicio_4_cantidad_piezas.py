#entrada
pieza1=int(input("el valor de la pieza 1 es ?:"))
pieza2=int(input("el valor de la pieza 2 es ?:"))
pieza3=int(input("el valor de la pieza 3 es ?:"))
montocompra=(pieza1+pieza2+pieza3)
if(montocompra>5000000 and montocompra<5000000):
    print("el decicir la manera del pago sera:")
elif(montocompra>5000000):
    print("como el valor excede los 5.000.000 se pagara con 55%, de inversion autonoma, con 30%, de inversion al banco y 15%, de credito del fabricante")
    inversion1=(montocompra*0.55)
    print(f"la inversion del 55%, es:{inversion1}")
    prestamo1=(montocompra*0.30)
    print(f"el valor del prestamo del banco que es del 30%, es:{prestamo1}")
    credito1=(montocompra*0.15)
    print(f"el valor del credito del fabricante del 15%, es de:{credito1}")
    interesC1=(credito1*0.20)
    print(f"el valor de los inetrese que nos da el fabricante por su credito es de:{interesC1}")
    print(f"el pago por el incremento de los 5.000.000 es de : {inversion1+prestamo1+credito1+interesC1}")
else:
    print("como el valor no excede los 5.000.000 se pagara con el 70%, de inversion autonoma y 30%, de credito del fabricante")
    inversion2=(montocompra*0.70)
    print(f"la inversion del 55%, es:{inversion2}")
    credito2=(montocompra*0.30)
    print(f"el valor del credito del fabricante del 30%, es de:{credito2}")
    interesC2=(credito2*0.20)
    print(f"el valor de los intereses que nos da el fabricante por su credito es de:{interesC2}")
    print(f"el pago por el monto que no llega a los 5.000.000 es de:{inversion2+credito2+interesC2}")