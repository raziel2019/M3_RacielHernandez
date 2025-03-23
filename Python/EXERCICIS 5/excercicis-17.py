#17. Realitza un programa que demani per teclat el resultat (dada sencer) obtingut a llançar un dau de sis cares i mostri per pantalla el nombre en 
# lletres (dada cadena) de la cara oposada a el resultat obtingut.
# Nota 1: En les cares oposades d'un dau de sis cares estan els números: 1-6, 2-5 i 3-4.
# Nota 2: Si el nombre de el dau introduït és menor que 1 o més gran que 6, es mostrarà el missatge: "ERROR: nombre incorrecte.".
# exemple:
# Introduïu nombre de el dau: 5
# A la cara oposada hi ha el "dos".


numero = int(input("Introduce el número del dado (1-6): "))

if numero == 1:
    print("En la cara opuesta está el 'seis'.")
elif numero == 2:
    print("En la cara opuesta está el 'cinco'.")
elif numero == 3:
    print("En la cara opuesta está el 'cuatro'.")
elif numero == 4:
    print("En la cara opuesta está el 'tres'.")
elif numero == 5:
    print("En la cara opuesta está el 'dos'.")
elif numero == 6:
    print("En la cara opuesta está el 'uno'.")
else:
    print("ERROR: número incorrecto.")
