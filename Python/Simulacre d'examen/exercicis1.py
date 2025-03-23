#1. Escriu un programa que demani a l'usuari una cadena i la mostri al revés.  "Estudiaré molt per l'examen!" -> "!nemaxe'l rep tlom éraidutsE"

cadena = input("Introduce una cadena:")

cadena_al_reves = ""

for caracter in cadena:
    cadena_al_reves = caracter + cadena_al_reves

print(cadena_al_reves)