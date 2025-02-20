Algoritmo prestamos_Bolivares
	//entrada
	Escribir "introduzca el monto del prestamo"
	Leer prestamo
	Escribir " introduzca cual fue el pago de los intereses"
	Leer interes
	Escribir "diga el tiempo de pago de estos intereses"
	Leer tiempo
	//caja negra
	interesporcientoanual<-(interes/(tiempo*prestamo))*100
	//salida
	Escribir interesporcientoanual, " % "
FinAlgoritmo