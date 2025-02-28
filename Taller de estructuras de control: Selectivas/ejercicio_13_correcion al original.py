#entrada
nombre=(input("ingrese el nombre:"))
nacimiento=input()
(dia,mes,año)=nacimiento.split()
dia=int(dia)
mes=int(mes)
año=int(año)
if dia>=22 and mes>=11 or dia<=21 and mes<=12 and dia>=22 and mes>=12 or dia<=20 and mes<=1 and dia>=21 and mes>=1 or dia<=19 and mes<=2 and dia>=20 and mes>=2 or dia<=19 and mes<=3 and dia>=21 and mes>=3 or dia<=20 and mes<=4 and 21 and mes>=4 or dia<=21 and mes<=5 and dia>=22 and mes>=5 or dia<=21 and mes<=6 and dia>=22 and mes>=6 or dia<=22 and mes<=7 and dia>=23 and mes>=7 or dia<=23 and mes<=8 and dia>=24 and mes>=8 or dia<=22 and mes<=9 and dia>=23 and mes>=9 or dia<=22 and mes<=10 and dia>=23 and mes>=10 or dia<=21 and mes<=11:
    print("decidir el signo zodiacal")
elif(dia>=22 and mes>=11 or dia<=21 and mes<=12):
    print("su signo zodiacal es Sagitario")
    edad=(2025-año)
    print(f"nombre: {nombre}")
    print(f"su edad es :{edad}")
elif(dia>=22 and mes>=12) or (dia<=20 and mes<=1):
    print("su signo zodiacal es Capricornio")
    edad=(2025-año)
    print(f"nombre: {nombre}")    
    print(f"la edad es : {edad}")
elif(dia>=21 and mes>=1) or (dia<=19 and mes<=2):
    print("su signo zodiacal es Acuario")
    edad=(2025-año)
    print(f"la edad es : {edad}")
elif(dia>=20 and mes>=2) or (dia<=19 and mes<=3):
    print("su signo zodiacal es Piscis")
    edad=(2025-año)
    print(f"nombre: {nombre}")
    print(f"la edad es : {edad}")
elif(dia>=21 and mes>=3) or (dia<=20 and mes<=4):
    print("su signo zodiacal es Aries")
    edad=(2025-año)
    print(f"nombre: {nombre}")
    print(f"la edad es : {edad}")
elif(dia>=21 and mes>=4) or (dia<=21 and mes<=5):
    print("su signo zodiacal es Tauro")
    edad=(2025-año)
    print(f"nombre: {nombre}")
    print(f"la edad es : {edad}")
elif(dia>=22 and mes>=5) or (dia<=21 and mes<=6):
    print("su signo zodiacal es Geminis")
    edad=(2025-año)
    print(f"nombre: {nombre}")
    print(f"la edad es : {edad}")
elif(dia>=22 and mes>=6) or (dia<=22 and mes<=7):
    print("su signo zodiacal es Cancer")
    edad=(2025-año)
    print(f"nombre: {nombre}")
    print(f"la edad es : {edad}")
elif(dia>=23 and mes>=7) or (dia<=23 and mes<=8):
    print("su signo zodiacal es Leo")
    edad=(2025-año)
    print(f"nombre: {nombre}")
    print(f"la edad es : {edad}")
elif(dia>=24 and mes>=8) or (dia<=22 and mes<=9):
    print("su signo zodiacal es Virgo")
    edad=(2025-año)
    print(f"nombre: {nombre}")
    print(f"la edad es : {edad}")
elif(dia>=23 and mes>=9) or (dia<=22 and mes<=10):
    print("su signo zodiacal es Libra")
    edad=(2025-año)
    print(f"nombre: {nombre}")
    print(f"la edad es : {edad}")
elif(dia>=23 and mes>=10) or (dia<=21 and mes<=11):
    print("su signo zodiacal es Escorpion")
    edad=(2025-año)
    print(f"nombre: {nombre}")
    print(f"la edad es : {edad}")





