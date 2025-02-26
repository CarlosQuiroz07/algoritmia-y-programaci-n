#entrada
categoria=int(input("ingrese la categoria para la que hay que hacer el aumento correspondiente "))
sueldo=int(input("ingrese el salario bruto del trabajador: "))
if(categoria==1 and sueldo==5000000):
    print("como es la categoria 1 el aumento sera del 10%")
    suelcate=(5000000*0.10)+sueldo
    print(f"el nuevo sueldo bruto con el aumento es de: {suelcate}COP")
elif(categoria==2 and sueldo==4300000):
    print("como es la categoria 2 el aumento sera del 15%")
    suelcate=(4300000*0.15)+sueldo
    print(f"el nuevo salario bruto con el aumento es de: {suelcate}")
elif(categoria==3 and sueldo==3600000):
    print("como es la categoria 3 el aumento seria del 20%")
    suelcate=(3600000*0.20)+sueldo
    print(f"el nuevo salario bruto con el aumento es de: {suelcate}")
elif(categoria==4 and sueldo==2000000):
    print("como es la categoria 4 el aumento sera del 40%")
    suelcate=(2000000*0.40)+sueldo
    print(f"el nuevo salario bruto con el aumento es de: {suelcate}")
elif(categoria==5 and sueldo==900000):
    print("como es la categoria 5 el aumento sera del 60%")
    suelcate=(900000*0.60)+sueldo
    print(f"el nuevo salrio bruto con el aumento es de: {suelcate}")
