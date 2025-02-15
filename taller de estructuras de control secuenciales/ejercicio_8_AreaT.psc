Algoritmo ejercicio_8_AreaT
	//entradas
	Escribir "Dijite los datos de a"
	Leer Datos1
	Escribir "Dijite los datos de b"
	Leer datosb
	escribir"Dijite los datos de c"
	Leer datosc
	//caja negra
	datosS<-(Datos1+datosb+datosc)/2
	areaR<-(raiz(datosS*(datosS-Datos1)*(datosS-datosb)*(datosS-datosc)))
	Escribir "los datos del semiperimetro s son:",datosS
	Escribir "los datos del area triangulo es:", areaR
FinAlgoritmo
