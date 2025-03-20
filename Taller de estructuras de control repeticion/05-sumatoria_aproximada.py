"""
El programa calcula el número de términos necesarios para que la siguiente sumatoria se aproxime a 1000 sin excederlo:
"""
suma = 0
K = 1
contar = 0
while True:
    termino = (K**2 + 1)/K  
    if suma + termino > 1000:
        break    

    suma += termino
    contar += 1
    K += 1 
    
print(f"Número de términos necesarios: {contar}")
print(f"Suma alcanzada: {suma}")