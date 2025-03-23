# 61.- Escribe un programa que pida al usuario una frase y cuente el número de veces que aparece el carácter "e".
#  Si no hay ningún "e", el programa debería mostrar un mensaje indicándolo.

frase = input("Introduce una frase: ")
contador = 0
for caracter in frase:
    if caracter == 'e':
        contador +=1

if contador == 0:
    print("No hay un caracter 'e' en la frase.")
else:
    print(f"Número de veces que aparece 'e': {contador}")
 