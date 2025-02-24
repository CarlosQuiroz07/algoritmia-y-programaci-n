#entrada
datos=input()
(P, Q)=datos.split()
P=int(P)
Q=int(Q)
if(P**3+Q**4-2*P**2>680):
    print("los valores de P y Q satisfacen la expresion")
else:
    print("los valores de P y Q  no satisfacen la expresion")