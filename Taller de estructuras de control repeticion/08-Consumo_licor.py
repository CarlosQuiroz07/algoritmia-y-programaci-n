"""
Se encuestó a varias personas en discotecas y sitios de diversión sobre su consumo de licor. 
El programa procesará los datos y generará estadísticas.
"""


def Encuesta_licor():
    licor = ["Aguardiente", "Ron", "Cerveza", "Tequila", "Whisky", "Otro"]

    total_encuestados = 0
    mujeres = 0
    hombres = 0
    consumo = 0
    menor_edad = 0
    consumo_20_25_años = 0
    mujeres_menor_edad = 0
    consumen_whisky = 0

    conteolicor = {
        "Aguardiente": 0,
        "Ron": 0,
        "Cerveza": 0,
        "Tequila": 0,
        "Whisky": 0,
        "Otro": 0
    }

    edad_consumidor = []
    edad_cerveza = []

    while True:
        while True:
            pregunta_dicotomica = input(
                "Consume alcohol? (Si/No): ").capitalize()
            if pregunta_dicotomica in ['Si', 'No']:
                break
            print('ERROR: Opción válida solo "Si o No"')

        if pregunta_dicotomica == 'No':
            total_encuestados += 1
            continuar = input(
                "¿Desea continuar con otra encuesta? (Sí/No): ").lower()
            if continuar not in ['sí', 'si']:
                break
            continue

        consumo += 1

        while True:
            licor_preferido = input(
                f"Licor preferido (Opciones: {', '.join(licor)}): ").capitalize()
            if licor_preferido in licor:
                conteolicor[licor_preferido] += 1
                break
            print("ERROR: Solo el valor que se encuentra en la lista")

        while True:
            try:
                edad = int(input("Cual es su edad: "))
                if 0 < edad < 100:
                    edad_consumidor.append(edad)
                    if edad < 18:
                        menor_edad += 1

                    if licor_preferido == 'Cerveza':
                        edad_cerveza.append(edad)

                    break
                print("ERROR: Deme un valor verdadero")
            except ValueError:
                print("Ingrese un número válido")

        while True:
            sexo = input('Cual es su sexo (Masculino/Femenino): ').capitalize()
            if sexo in ['Masculino', 'Femenino']:
                if sexo == 'Masculino':
                    hombres += 1
                    if 20 <= edad <= 25 and licor_preferido != 'Aguardiente':
                        consumo_20_25_años += 1
                else:
                    mujeres += 1
                    if edad < 18:
                        mujeres_menor_edad += 1
                break
            print("ERROR: Registre un sexo válido")

        if licor_preferido == 'Whisky':
            consumen_whisky += 1

        total_encuestados += 1

        continuar = input(
            "¿Desea continuar con otra encuesta? (Sí/No): ").lower()
        if continuar not in ['sí', 'si']:
            break

    promedio_edad_cerveza = sum(edad_cerveza) / \
        len(edad_cerveza) if edad_cerveza else 0

    print("\n--- RESULTADOS DE LA ENCUESTA ---")
    print(f"Total de personas encuestadas que consumen licor: {consumo}")
    print(f"Total de mujeres menores de edad: {mujeres_menor_edad}")
    print(
        f"Total de hombres que no consumen aguardiente y tienen entre 20 y 25 años: {consumo_20_25_años}")
    print(
        f"Promedio de edad de quienes consumen cerveza: {promedio_edad_cerveza}")

    porcentaje_whisky = (consumen_whisky / total_encuestados *
                         100) if total_encuestados > 0 else 0
    print(
        f"Porcentaje de personas que consumen whisky respecto al total encuestado: {porcentaje_whisky}%")


Encuesta_licor()
