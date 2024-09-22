#2. Calcular el perímetre i àrea d'un rectangle donada la seva base i la seva altura.

base = int(input("Introduce la base: "))
altura = int(input ("Introduce la altura: "))

perimetre_rectangle =  2 * (base + altura)
area_rectangle = base * altura

print("Este es el perimetre: " + str(perimetre_rectangle))
print("Este es el area: " + str(area_rectangle))