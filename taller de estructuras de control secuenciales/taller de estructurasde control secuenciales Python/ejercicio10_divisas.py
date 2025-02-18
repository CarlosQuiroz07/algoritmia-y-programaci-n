
#entrada
chelines=int(input("ingrese la cantidad de chelines"))
dracmas=int(input("ingrese la cantidad de dracmas"))
pecetas=int(input("ingrese la cantidad de pecetas"))
#caja negra 
chelines1=(chelines*956.781)/100
pecetas1=(dracmas*88.607)/100
francos=(pecetas1/20.110)
dolares=(pecetas/122.499)
liras=(pecetas*100)/9.289
#salida
print("la cantidad de chelines a pecetas es:", chelines1)
print("la cantidad de dragmas a francos es:", francos)
print("la cantidad equivalente al dolar es:",dolares)
print("la cantidadd de liras equivalentes es:", liras)