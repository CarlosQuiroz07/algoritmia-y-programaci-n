#entrada
dinero=int(input("ingrese la cantidad de dinero en COP:"))
if(dinero>=100000):
    resultado=(dinero//100000)
    print("existen:"+ str(resultado)+ ": billetes de 100.000 COP")
    dinero=(dinero % 100000)
if(dinero>=50000):
    resultado=(dinero//50000)
    print("existen:"+ str(resultado)+ ": billetes de 50.000 COP")
    dinero=(dinero % 50000)
if(dinero>=20000):
    resultado=(dinero//20000)
    print("existen:"+ str(resultado)+ ": billetes de 20.000 COP")
    dinero=(dinero % 20000)
if(dinero>=10000):
    resultado=(dinero//10000)
    print("existen:"+ str(resultado)+ ": billetes de 10.000 COP")
    dinero=(dinero % 10000)
if(dinero>=5000):
    resultado=(dinero//5000)
    print("existen:"+ str(resultado)+ ": billetes de 5.000 COP")
    dinero=(dinero % 5000)
if(dinero>=2000):
    resultado=(dinero//2000)
    print("existen:"+ str(resultado)+ ": billetes de 2.000 COP")
    dinero=(dinero % 2000)
if(dinero>=1000):
    resultado=(dinero//1000)
    print("existen:"+ str(resultado)+ ": billetes de 1.000 COP")
    dinero=(dinero % 1000)
if(dinero>=500):
    resultado=(dinero//500)
    print("existen:"+ str(resultado)+ ": monedas de 500 COP")
    dinero=(dinero % 500)
if(dinero>=200):
    resultado=(dinero//200)
    print("existen:"+ str(resultado)+ ": monedas de 200 COP")
    dinero=(dinero % 200)
if(dinero>=100):
    resultado=(dinero//100)
    print("existen:"+ str(resultado)+ ": monedas de 100 COP")
    dinero=(dinero % 100)
if(dinero>=50):
    resultado=(dinero//50)
    print("existen:"+ str(resultado)+ ": monedas de 50 COP")
    dinero=(dinero % 50)
