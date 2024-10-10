#10. Algorisme que demani els punts centrals x1, y1, x2, y2 i els radis r1, r2 de dos
# circumferències i les classifiqui en un d'aquests estats:
# exteriors
# tangents exteriors
# assecants
# tangents interiors
# interiors
# concèntriques

import math

x1 = float(input("Introduce el punto x del centro de la primera circunferencia: "))
y1 = float(input("Introduce el punto y del centro de la primera circunferencia: "))
r1 = float(input("Introduce el radio de la primera circunferencia: "))

x2 = float(input("Introduce el punto x del centro de la segunda circunferencia: "))
y2 = float(input("Introduce el punto y del centro de la segunda circunferencia: "))
r2 = float(input("Introduce el radio de la segunda circunferencia: "))

distancia_centros = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
suma_radios = r1 + r2
diferencia_radios = abs(r1 - r2)

if distancia_centros > suma_radios:
    print("Las circunferencias son exteriores.")
elif distancia_centros == suma_radios:
    print("Las circunferencias son tangentes exteriores.")
elif diferencia_radios < distancia_centros < suma_radios:
    print("Las circunferencias son secantes.")
elif distancia_centros == diferencia_radios:
    print("Las circunferencias son tangentes interiores.")
elif distancia_centros < diferencia_radios:
    print("Las circunferencias son interiores.")
else:
    print("Las circunferencias son concéntricas.")
