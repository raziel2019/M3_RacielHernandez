# 12. Demana a l'usuari dos parells 
# de nombres x1, y1 i x2, y2, que representin dos punts en el pla.
#  Calcula i mostra la distància 
# entre ells.

x1 = int(input("introduce el primer numero del primer par x1: "))
y1 = int(input("introduce el segundo numero del primer par y1: "))

x2 = int(input("introduce el primer numero del segundo par x2:  "))
y2 = int(input("introduce el segundo numero del segundo par y2: "))

distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** .5

print("la distancia es: " + str(distancia))