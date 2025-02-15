Algoritmo ejercicio_5_calificaciones
	//entrada
	// ingreso de calificacion y su porcentaje de notas
	escribir"dijite el promedio de su primer parcial"
	Leer calificacion1
	escribir"dijite el promedio de su segundo parcial"
	Leer calificacion11
	escribir"dijite el promedio de su tercer parcial"
	Leer calificacion111
	nta<-(calificacion1+calificacion11+calificacion111)/3
	Escribir "la nota exacta seria" ,nta
	Escribir "dijitela calificación del examen final "
	leer calificacion2
	Escribir "dijite la calificación del trabajo final."
	Leer calificacion3
	//caja negra
	nta1<-(nta*0.55)
	escribir "la nota de los parciales se basa en:" , nta1
	nta2<-(calificacion2*0.30)
	Escribir "la nota del examen final se basa en:" , nta2
	nta3<- (calificacion3*0.15)
	Escribir "la nota del trabajo final se basa en:" , nta3
	nta4<-(nta1+nta2+nta3)
	//salida
	Escribir "la nota definitiva de las tres notas son y su porcentajes son:" ,nta4
FinAlgoritmo
