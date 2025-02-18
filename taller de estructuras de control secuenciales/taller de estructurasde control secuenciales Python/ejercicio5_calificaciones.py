
#entrada
parcial1=float(input("ingrese el resultado de la primer nota del parcial"))
parcial2=float(input("ingrese el resultado de la segunda nota del parcial"))
parcial3=float(input("ingrese el resultado de la tercer nota del parcial"))
examenfinal=float(input("dijite la caliificacion del examen final"))
trabajofinal=float(input("dijite la calificacion del trabajo final"))
#caja negra
nota1=(parcial1+parcial2+parcial3)/3
nota2=(nota1*0.55)
nota3=(examenfinal*0.30)
nota4=(trabajofinal*0.15)
notafinal=(nota2+nota3+nota4)
#salida
print("la nota exacta de la suma de los parciales seria:", nota1)
print("la nota con el 55% de lo parciales es:",nota2)
print("la nota con el 30% de el examen final es:", nota3)
print("la nota con el 15% de el trabajo final es:",nota4)
print("la nota definitiva de la suma de las tres calificaciones:", notafinal)