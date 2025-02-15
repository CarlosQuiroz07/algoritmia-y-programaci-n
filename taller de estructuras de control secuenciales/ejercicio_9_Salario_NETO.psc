Algoritmo ejercicio_9_Salario_NETO
	//ENTRADAS
	Escribir "dijite el valor por hora trabajada"
	Leer trabajoh
	Escribir "Dijite el numero de las horas trabajadas"
	leer htrabajadas
	//CAJA NEGRA
	salariobruto<-(htrabajadas*trabajoh)
	descuento<-(0.20*salariobruto)
	//salidas
	Escribir "el salario bruto por dia es:", salariobruto
	Escribir "el valor del descuento:", descuento
	salariodia<-(salariobruto-descuento)
	Escribir "el valor del salario dia es:", salariodia
	salarioM<-(salariobruto*30)
	Escribir "el salario neto por mes es:", salarioM-descuento
	
	
FinAlgoritmo
