Algoritmo palíndromo
	nuevo_texto<- ""
	escribir"escribir una palabra para validar si es un palindromo"
	Leer palindromo1
	long<-Longitud(palindromo1)
	inversa<-""
	para i <- long Hasta 1 con paso -1 Hacer
		inversa<-inversa+Subcadena(palindromo1,i,i)
	
	FinPara
	Escribir inversa
	si palindromo1 = inversa Entonces
		escribir" es una palindromo"
	SiNo
		Escribir "no es un palindromo"
	FinSi
FinAlgoritmo
