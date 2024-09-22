# 11. Demana a l'usuari dos nombres i mostra la "distància" entre ells 
# (el valor absolut de la seva diferència, de manera que el resultat 
# sigui sempre positiu).

numero1 = int(input("introduce el primer nombre: "))
numero2 = int(input("introduce el segundo nombre: "))

if numero1 > numero2:
    distancia = numero1 - numero2
else:
    distancia = numero2 - numero1

print("la distancia entre los dos nombres es: " + str(distancia))
