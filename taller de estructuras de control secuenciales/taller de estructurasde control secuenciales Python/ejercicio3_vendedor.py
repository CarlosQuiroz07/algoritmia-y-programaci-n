
#entrada
sueldobase=int(input("introduzca su sueldo base"))
comision1=int(input("introduzca la primera comision"))
comision2=int(input("introduzca la segunda comision"))
comision3=int(input("introduzca la tercera comision"))
#caja negra
porcentajecomisiones=(comision1+comision2+comision3)
valor_total=(porcentajecomisiones*0.10)+sueldobase
#salida
print("el porcentaje de las comisiones  mas el 10% es:",porcentajecomisiones*0.10)
print("su ganancia completa fue de:",valor_total)