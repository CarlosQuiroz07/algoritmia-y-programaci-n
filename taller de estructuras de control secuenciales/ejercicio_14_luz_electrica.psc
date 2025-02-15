Algoritmo ejercicio_14_luz_electrica
	//entradas
	Escribir "dijtar el numero de la lectura actual de la luz"
	Leer lecturaactual
	Escribir "introducir la lectura anterior de la luz "
	leer lecuraanterior
	Escribir "introducir el valor del costo por kilovatio"
	leer costokilovatio
	//caja negra
	consumo<-(lecturaactual-lecuraanterior)
	montoTotal<-(consumo*costokilovatio)
	//salida
	Escribir "el numero del consumo sea incrementado o disminuido es de:", consumo
	Escribir "el monto total del valor del servicio de luz:", montoTotal
	
	
FinAlgoritmo
