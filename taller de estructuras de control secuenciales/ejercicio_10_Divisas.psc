Algoritmo ejercicio_10_Divisas
	//entradas
	//ingreso de datos
	Escribir "ingrese la cantidad de cheliines austriacos:"
	Leer chelines
	Escribir "ingrese la cantidad en dracmas griegos:"
	Leer dracmas
	Escribir "ingrese la cantidad en pecetas:"
	Leer pecetas
	//caja negra}
	chelines1<-(chelines*956.871)/100
	pecetas1<-(dracmas*88.607)/100
	francos<-(pecetas1/20.110)
	dolares<-(pecetas/122.499)
	liras<-(pecetas*100)/9.289
	//salida
	Escribir "la cantidad de chelines a pecetas es:", chelines1
	Escribir "la cantidad de dracmas a francos es:", francos
	Escribir "la cantidad de dolar equivalente es:" , dolares
	Escribir "la cantidad de liras equivalentes es:", liras
FinAlgoritmo
