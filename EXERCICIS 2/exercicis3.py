#3. Donats els catets d'un triangle rectangle, calcular la seva hipotenusa.

cateto1 = int(input("Introduce el primer cateto: "))
cateto2 = int(input("Introduce el segundo cateto: "))

hipotenusa = (cateto1**2 + cateto2**2) ** 0.5


print("La hipotenusa es: " + str(hipotenusa))