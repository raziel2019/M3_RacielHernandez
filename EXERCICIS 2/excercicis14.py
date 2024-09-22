#14. Donat un nombre de dues xifres, dissenyi un algoritme 
# que permeti obtenir el nombre invertit. Exemple, si s'introdueix 
# 23 que mostri 32.

numero = int(input("introduce un numero: "))

if 10 <= numero < 100:
  primera_cifra = numero // 10
  print("primera cifra: "+ str(primera_cifra))
  segunda_cifra = numero % 10
  print("segunda cifra: "+ str(segunda_cifra))

nombre_invertit = str(segunda_cifra) + str(primera_cifra)

print("el nombre invertit: " + str(nombre_invertit))




