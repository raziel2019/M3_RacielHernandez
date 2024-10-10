# 11. Programa que llegeixi tres dades d'entrada A, B i C. Aquests corresponen a les dimensions dels costats d'un triangle. El programa ha de determinar quin tipus de triangle és, tenint en compte els següent:
# Si es compleix Pitàgores llavors és triangle rectangle
# Si només dos costats de el triangle són iguals llavors és isòsceles.
# Si els 3 costats són iguals llavors és equilàter.
# Si no es compleix cap de les condicions anteriors, és escalè.


A = float(input("Introduce el lado A del triángulo: "))
B = float(input("Introduce el lado B del triángulo: "))
C = float(input("Introduce el lado C del triángulo: "))

if A**2 + B**2 == C**2 or A**2 + C**2 == B**2 or B**2 + C**2 == A**2:
    print("Es un triángulo rectángulo.")
elif A == B == C:
    print("Es un triángulo equilátero.")
elif A == B or A == C or B == C:
    print("Es un triángulo isósceles.")
else:
    print("Es un triángulo escaleno.")
