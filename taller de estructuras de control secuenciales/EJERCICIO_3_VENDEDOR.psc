Algoritmo EJERCICIO_3_VENDEDOR
	//entrada
	//suminitracion de valores como su sueldo y ventas
	Escribir "Dijite su sueldo base"
	Leer SueldoBase1
	Escribir"suministre el valor de la comision 1"
	Leer comision1
	Escribir"suministre el valor de la comision 2"
	Leer comision2
	Escribir"suministre el valor de la comision 3"
	Leer comision3
	//caja negra
	porcencomisiones<-(comision1+comision2+comision3)
	Escribir "el resultado de su sueldo mas el 10% es:" ,porcencomisiones* 0.10
	valortotal<-(porcencomisiones*0.10)+SueldoBase1
	//salida
	Escribir "su ganancia completa fue:" , valortotal
FinAlgoritmo

