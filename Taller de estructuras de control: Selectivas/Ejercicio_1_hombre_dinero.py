#entrada
inversion=int(input("introduzca el valor de su inversion que se encuentra en el banco:"))
interes=int(input("introduzca el valor que se pagaba de intereses:"))
tiempo=int(input("introduzca el tiempo que pago esso intereses: "))
#caja negra
porcentaje=(interes/(tiempo*inversion))*100
inverfinal=(inversion*porcentaje)/100
valorealfinal=(inversion+inverfinal)
if(interes<100000):
    print("el valor fue menor a 100.000 para reinvertit")
elif(interes>100000):
    print("el valor excede de 100.000 y se reinvierte")
print("el valor del porcentaje anual equivale a:", porcentaje,"%")
print("el dinero que se genero por concepto inntereses es", inverfinal)
print("el valor de la inversion final es:", valorealfinal)