
T = int(input())
for i in range(T):
    datos_juego = input()
    a, b = datos_juego.split()  # a:Hincha de madrid  ; b:Profesor brayan
    if a == "tijera" and b == "papel":
        print("Caso # 1: ¡LaVidaEsDura!")
        if a == "papel" and b == "tijera":
            print("Caso # 2: ¡No es suerte, es el árbitro!")

    elif a == "papel" and b == "piedra":
        print("Caso # 1: ¡LaVidaEsDura!")
        if a == "piedra" and b == "papel":
            print("Caso # 2: ¡No es suerte, es el árbitro!")

    elif a == "roca" and b == "lagarto":
        print("Caso # 1: ¡LaVidaEsDura!")
        if a == "lagarto" and b == "roca":
            print("Caso # 2: ¡No es suerte, es el árbitro!")

    elif a == "lagarto" and b == "holk":
        print("Caso # 1: ¡LaVidaEsDura!")
        if a == "holk" and b == "lagarto":
            print("Caso # 2: ¡No es suerte, es el árbitro!")
       
    elif a == "holk" and b == "tijera":
        print("Caso # 1: ¡LaVidaEsDura!")
        if a == "tijera" and b == "holk":
            print("Caso # 2: ¡No es suerte, es el árbitro!")

    elif a == "tijera" and b == "lagarto":
        print("Caso # 2: ¡No es suerte, es el árbitro!")
        if a == "lagarto" and b == "tijera":
            print("Caso # 2: ¡No es suerte, es el árbitro!")

    elif a == "lagarto" and b == "papel":
        print("Caso # 1: ¡LaVidaEsDura!")
        if a == "papel" and b == "lagarto":
            print("Caso # 2: ¡No es suerte, es el árbitro!")

    elif a == "papel" and b == "holk":
        print("Caso # 1: ¡LaVidaEsDura!")
        if a == "holk" and b == "papel":
            print("Caso # 2: ¡No es suerte, es el árbitro!")

    elif a == "holk" and b == "roca":
        print("Caso # 1: ¡LaVidaEsDura!")
        if a == "roca" and b == "holk":
            print("Caso # 2: ¡No es suerte, es el árbitro!")

    elif a == "roca" and b == "tijera":
        print("Caso # 1: ¡LaVidaEsDura!")
        if a == "tijera" and b == "roca":
            print("Caso # 2: ¡No es suerte, es el árbitro!")
