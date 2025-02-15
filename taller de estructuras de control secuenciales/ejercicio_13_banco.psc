Algoritmo ejercicio_13_banco
	//entradas
	Escribir "escribir el numero de billetes de 50.000"
	Leer N1
	Escribir "escribir el numero de billetes de 20.000"
	Leer N2
	Escribir "escribir el numero de billetes de 10.000"
	Leer N3
	Escribir "escribir el numero de billetes de 5.000"
	Leer N4
	Escribir "escribir el numero de billetes de 2.000"
	Leer N5
	Escribir "escribir el numero de billetes de 1.000"
	Leer N6
	Escribir "escribir el numero de billetes de 500"
	Leer N7
	Escribir "escribir el numero de billetes de 100"
	Leer N8
	//caja negra
	cuantod1<-(50000*N1)
	cuantod2<-(20000*N2)
	cuantod3<-(10000*N3)
	cuantod4<-(5000*N4)
	cuantod5<-(2000*N5)
	cuantod6<-(1000*N6)
	cuantod7<-(500*N7)
	cuantod8<-(100*N8)
	cuantodinero<-(cuantod1+cuantod2+cuantod3+cuantod4+cuantod5+cuantod6+cuantod7+cuantod8)
	//salidas
	Escribir "el numero de billetes de 50.000:", cuantod1
	Escribir "el numero de billetes de 20.000:", cuantod2
	Escribir "el numero de billetes de 10.000:", cuantod3
	Escribir "el numero de billetes de 5.000:", cuantod4
	Escribir "el numero de billetes de 2.000:", cuantod5
	Escribir "el numero de billetes de 1.000:", cuantod6
	Escribir "el numero de billetes de 500:", cuantod7
	Escribir "el numero de billetes de 100:", cuantod8
	Escribir " el dinero que hay en el banco es:", cuantodinero
	
FinAlgoritmo
