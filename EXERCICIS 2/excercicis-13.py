#13. Realitzar un algoritmes que llegeixi un nombre 
# i que mostri la seva arrel quadrada 
# i la seva arrel cúbica. Python3 no té cap funció predefinida que permeti calcular 
# l'arrel cúbica, Com es pot calcular?

numero = int(input("introduce un nombre: "))

arrel_quadrada = numero ** (1/2)

arrel_cúbica = numero ** (1/3)

print("l'arrel quadrada es: " + str(arrel_quadrada))

print("l'arrel cúbica es: " + str(arrel_cúbica))
