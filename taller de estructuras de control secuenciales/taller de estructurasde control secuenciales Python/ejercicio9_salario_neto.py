
#entrada
trabajoh=int(input("ingrese el valor de la hora trabajada"))
htrabajadas=int(input("ingrese el valor de las horas trabajadas"))
#caja negra
salariobruto=(htrabajadas*trabajoh)
descuento=(0.20*salariobruto)
salariodedia=(salariobruto-descuento)
salariomensual=(salariobruto*30)
salarioydescuento=(salariomensual-descuento)
#salida 
print("el salario brut por dia es:", salariobruto)
print("el valor del descuento es:", descuento)
print("el salario del dia quedo en:", salariodedia)
print("el salario aplicando el descuento es:", salarioydescuento)

