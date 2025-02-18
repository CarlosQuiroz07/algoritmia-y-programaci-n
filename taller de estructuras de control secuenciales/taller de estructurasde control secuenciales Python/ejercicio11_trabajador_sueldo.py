
#entrada
nombre=(input("introduzca el nombre del trabajador"))
htrabajadas=int(input("introduzca el numeroo de horas trabajadas"))
hextras=int(input("introduzca el numero de horas extras trabajadas"))
valorhora=int(input("introduzca el valor de hora trabajada"))
cantidadhijos=int(input("introduzca el numero de hijos que tiene"))
#caja negra
horasextras=(valorhora*0.25)
horastrabajo=(htrabajadas*valorhora)*30
sueldobase=(horastrabajo+horasextras)
elpagoforzoso=(sueldobase*0.05)
politicahabitacional=(sueldobase*0.02)
cajadeahorro=(sueldobase*0.07)
actacademica=(250000)
cadahijo=(173000*cantidadhijos)
primahogar=(180000)
salarioneto1=(elpagoforzoso+politicahabitacional+cajadeahorro)
salarioneto2=(actacademica+cadahijo+primahogar+horasextras)
salarioneto3=(sueldobase+salarioneto2)-salarioneto1
#salida
print("el sueldo base constaria de la suma de:", sueldobase)
print("el valor de la deducciones es:", salarioneto1)
print("el valor de la asignaciones es:", salarioneto2)
print("el sueldo par el mes de dieciembre seria:", salarioneto3)