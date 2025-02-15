Algoritmo ejercicio_19_lote
    Definir X, S, K, costo_total, ganancia, porcentaje_ganancia Como Real
    //ENTRADA
    Escribir "Ingrese la cantidad de naranjas: "
    Leer X
    Escribir "Ingrese el precio por docena (Bs.): "
    Leer S
    Escribir "Ingrese el ingreso total obtenido (Bs.): "
    Leer K
    //CAJA NEGRA
    costototal<-(X/12)*S
    ganancia<-(K-costo_total)
    porcentaje_ganancia<-(ganancia/costototal)*100-100
    //SALIDA
    Escribir "El porcentaje de ganancia es: ", porcentaje_ganancia, "%"
FinAlgoritmo
