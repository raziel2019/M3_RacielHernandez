#7. Realitza un algoritme que calculi la potència, per això demana per teclat la base i l'exponent. Poden ocórrer tres coses:
#L'exponent sigui positiu, només has d'imprimir la potència.
#L'exponent sigui 0, el resultat es 1.
#L'exponent sigui negatiu, el resultat es 1 / potència amb l'exponent positiu.


base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))

if exponente > 0:
    resultado = base ** exponente
    print("La potencia es:", resultado)
elif exponente == 0:
    print("La potencia es: 1")
else:
    resultado = 1 / (base ** abs(exponente))
    print("La potencia es:", resultado)
