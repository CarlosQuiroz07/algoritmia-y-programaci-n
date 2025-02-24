#entrada
salariobrutomensual=int(input("el salario bruto de los empleados es de:"))
ventadepar1=int(input("lo que genero el departamento 1 es de:"))
ventadepar2=int(input("lo que genero el departamento 2 es de:"))
ventadepar3=int(input("lo que genero el departamento 3 es de:"))
ventatotal=((ventadepar1+ventadepar2+ventadepar3)*0.33)
if(ventadepar1>=ventatotal):
    print("si el valor del departamento 1 sobrepasa el 33%")
    incrementosalarial=(salariobrutomensual*0.20)
    print(f"como el valor del departamento uno sobrepasa el 33%, los empleados se les incrementara un 20% {incrementosalarial}")
elif(ventadepar2>=ventatotal): 
    print("si el valor del departamento 1 sobrepasa el 33%")
    incrementosalarial2=(salariobrutomensual*0.20)
    print(f"como el valor del departamento uno sobrepasa el 33%, los empleados se les incrementara un 20% {incrementosalarial2}")
elif(ventadepar3>=ventatotal):
    print("si el valor del departamento 1 sobrepasa el 33%")
    incrementosalarial3=(salariobrutomensual*0.20)
    print(f"como el valor del departamento uno sobrepasa el 33%, los empleados se les incrementara un 20% {incrementosalarial3}")
#salida
salarioahora=(salariobrutomensual+incrementosalarial)
print(f"el salario ahora es de:{salarioahora}")
ventassuma=(ventadepar1+ventadepar2+ventadepar3)
print(f"el valor total de las ventas de los 3 departamentos es de:{ventassuma}")