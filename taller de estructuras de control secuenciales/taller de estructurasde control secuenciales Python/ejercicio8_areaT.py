
#entrada
datosa=int(input("ingrese la datos de a:"))
datosb=int(input("ingrese la datos de b:"))
datosc=int(input("ingrese la datos de c:"))
#caja negra
datosSeriperimetro=(datosa+datosb+datosc)/2
resultado=(datosSeriperimetro*(datosSeriperimetro-datosa)*(datosSeriperimetro-datosb)*(datosSeriperimetro-datosc))
area= (resultado**0.5)
#salida
print("los datos del seriperimetro es:", datosSeriperimetro)
print("los datos del area es:", area)