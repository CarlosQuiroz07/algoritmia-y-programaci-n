Algoritmo Ejercicio_20_computadores
    //entradas
    Escribir "Ingrese el precio al contado del computador (COP): "
    Leer contado
    Escribir "Ingrese el valor de cada cuota mensual (COP): "
    Leer couta
    //caja negra
    totalcuotas<-(couta * 12)
    recargo<-(contado-totalcuotas)
    porcentajerecargo<-(recargo/contado)*100
    //salida
    Escribir "El porcentaje de recargo por pago en cuotas es: ", porcentajerecargo, "%"
FinAlgoritmo
