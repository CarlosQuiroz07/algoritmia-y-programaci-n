#entrada
dinero=int(input("ingrese la cantidad de dinero en COP:"))
lista=[100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50]
for i in lista:
 if(dinero>=i):
    resultado=(dinero//i)
    print("existen:"+ str(resultado)+("billete"if dinero >=1000 else "moneda")+"de"+ str (i))
    dinero=(dinero % i)