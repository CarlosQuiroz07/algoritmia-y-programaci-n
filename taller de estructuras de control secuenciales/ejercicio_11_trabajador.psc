Algoritmo ejercicio_11_trabajador 
	//entradas
	Escribir "ingrese el nombre del trabajador"
	leer nombre
	Escribir "ingrese el numero de horas trabajadas por dia"
	Leer htrabajadas
	Escribir "ingrese el valor por hora trabajada"
	Leer trabajoxh
	Escribir "ingrese el numero de horas extras"
	Leer hextras
	Escribir "ingrese cuantos hijos posee"
	Leer Canthijos
	//caja negra
	horasExtras<-(trabajoxh*0.25)
	horastrabajo<-(htrabajadas*trabajoxh)*30
	sueldobase<-(horastrabajo+horasExtras)
	elpagoforzoso<-(sueldobase*0.05)
	politicaHabitacional<-(sueldobase*0.02)
	cajadeahorro<-(sueldobase*0.07)
	actAcademica<-(250000)
	cadhijo<-(173000*Canthijos)
	primahogar<-(180000)
	salarioneto1<-(elpagoforzoso+politicaHabitacional+cajadeahorro)
	salarioneto2<-(actAcademica+cadhijo+primahogar+horasExtras)
	salarioneto3<-(sueldobase+salarioneto2)-salarioneto1
	//salidas
	Escribir " el salario base constaria de:", sueldobase
	Escribir "el numero de deduccciones es:", elpagoforzoso+politicaHabitacional+cajadeahorro
	Escribir "el numero de asignaciones es:", actAcademica+cadhijo+primahogar+horasExtras
	Escribir "el salario neto para el mes de diciembre:", salarioneto3
	
FinAlgoritmo
