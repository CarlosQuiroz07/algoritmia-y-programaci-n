"""
Se encuestó a varias personas en discotecas y sitios de diversión sobre su consumo de licor. 
El programa procesará los datos y generará estadísticas.
"""
consumo_licor = 0
consumo_nolicor = 0
consumo = 0
conta_mujer = 0
conta_hombre = 0
conta_menor_mujer = 0
conta_hombre_noaguardiente = 0
conta_aguardiente = 0
conta_ron = 0
conta_cerveza = 0
conta_tequila = 0
conta_whisky = 0
conta_otro = 0
edad_promedio = 0

while True:
    pregunta_dicotomica = input('Consumes licor \"Si/No": ')
    pregunta_dicotomica = pregunta_dicotomica.capitalize()
    if pregunta_dicotomica == 'si':
        consumo_licor += 1
    else:
        consumo_nolicor += 1
    consumo += 1

    licor_preferencia = int(input("Cual es su licor de preferencia (opciones: 1-Aguardiente, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro): "))

    if licor_preferencia == 1:
        conta_aguardiente += 1
    elif licor_preferencia == 2:
        conta_ron += 1
    elif licor_preferencia == 3:
        conta_cerveza += 1
    elif licor_preferencia == 4:
        conta_tequila += 1
    elif licor_preferencia == 5:
        conta_whisky += 1
    elif licor_preferencia == 6:
        conta_otro += 1

    edad = int(input("Ingrese su edad: "))
    sexo = input("Ingrese su sexo (Masculino,Femenino)")
    sexo = sexo.capitalize()

    if 0 < edad < 100:
        edad_promedio += 1

        if sexo == "Femenino" and edad < 18:
            conta_menor_mujer += 1

        if sexo == "Masculino" and 20 <= edad <= 25 and licor_preferencia != 1:
            conta_hombre_noaguardiente += 1

        if licor_preferencia == 3:
             edad_promedio += edad
    else:
        print("Por favor, ingrese una edad válida")

    continuar_encuesta = input("\n¿Continuamos con la encuesta? (si/no): ")
    continuar_encuesta = continuar_encuesta.lower()
    if continuar_encuesta != 'si':
        break

print(f"Total de personas que consumen licor: {consumo}")
print(f"Total de mujeres menores de edad: {conta_menor_mujer}")
print(f"Total de hombres entre 20-25 años que no consumen aguardiente: {conta_hombre_noaguardiente}")
print(f"Promedio de edad de quienes consumen cerveza: {edad_promedio / conta_cerveza}")
print(f"Porcentaje de personas que consumen whisky: {(conta_whisky / consumo) * 100}%")
