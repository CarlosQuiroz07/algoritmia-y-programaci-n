#entrada
nombrecliente=(input("ingrese el nombre del cliente "))
montocompra=int(input("ingrese el monto de la compra "))
if(montocompra<50000):
    print("no hay descuento por el valor de la compra ")
elif(montocompra>=50000 and montocompra<=100000):
    print(" como no excede a los 50.000 se le aplicara el descuento del 5%:")
    descuento1=(montocompra*0.05) 
    print(f"el valor del descuento es de: {descuento1}")
    pagototal1=(montocompra-descuento1)
    print(f"el valor con descuento es de: {pagototal1}")
elif(montocompra>=100000 and montocompra<=700000):
    print("como el valor de excede los 100.000cop el descuento es del 11%")
    descuento1=(montocompra*0.11)
    print(f"el descuento aplicado es de:{descuento1}")
    pagototal1=(montocompra-descuento1)
    print(f"el valor con descuento es de:{pagototal1}")
elif(montocompra>=700000 and montocompra<=1500000):
    print("como el valor de la como supera los 700.000 el descuento sera del 118")
    descuento1=(montocompra*0.18)
    print(f"el descuento aplicado es de:{descuento1}")
    pagototal1=(montocompra-descuento1)
    print(f"el valor con descuento es de :{pagototal1}")
elif(montocompra>1500000):
    print("como ell valor supera el 1.500.000 el descuento es del 25%:")
    descuento1=(montocompra*0.25)
    print(f"el valor del descuento aplicado es de: {descuento1}")
    pagototal1=(montocompra-descuento1)
    print(f"el valor con el descueno es de: {pagototal1}")
print(f"el nombre del cliente es:{nombrecliente}")

