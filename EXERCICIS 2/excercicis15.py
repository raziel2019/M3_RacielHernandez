# 15. Donades dues variables numèriques A i B, que l'usuari ha de teclejar, 
# es demana realitzar un algoritme que intercanviï els valors de les 
# dues variables i mostri que fa valen a al final les dues variables.

A = int(input("introduce un nombre A: "))
B = int(input("introduce un nombre B: "))

intercambio = A
A = B
B = intercambio

print("el valor de A es: " + str(A))
print("el valor de B es: " + str(B))