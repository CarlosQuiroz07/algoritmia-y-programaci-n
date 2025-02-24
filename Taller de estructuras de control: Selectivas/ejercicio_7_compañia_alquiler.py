#entrada
distanciarrecorrida=int(input("ingres una cantidad recorrida en km:"))
if(distanciarrecorrida<=300):
    print("el valor de la distancia ya que no supero los 300km es de:")
    costo=50000
elif(distanciarrecorrida<=1000):
    print("el valor de la distancia ya que es inferior a los 1000km es de:")
    costo = 70000 + (distanciarrecorrida - 300) * 30000 
elif(distanciarrecorrida>=1000):
    print("el valor de la distancia que es superior a los 1000km es de:")
    costo = 90000 + (distanciarrecorrida - 1000) * 9000 
print(f"El costo total a pagar es: {costo:,} COP")
