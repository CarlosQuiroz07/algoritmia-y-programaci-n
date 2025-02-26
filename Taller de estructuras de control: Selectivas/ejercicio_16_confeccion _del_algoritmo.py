#entrada
import math
datos=input()
(a,b,c,)=datos.split()
a=int(a)
b=int(b)
c=int(c)
d=(b**2-4*a*c)
if(d>0):
    x1=((-b+ math.sqrt(d))/(2*a))
    x2=((-b- math.sqrt(d))/(2*a))
    print(f"las soluciones serian: x1={x1:.2f}, x2={x1:.2f}")
elif(d==0):
    x=(-b/(2*a))
    print(f"su unica solicion es:{x:.2f}")
else:
    print("no tiene solucion en los numeros reales")