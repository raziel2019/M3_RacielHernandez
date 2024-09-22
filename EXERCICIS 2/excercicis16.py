#16. Dos vehicles viatgen a diferents velocitats (v1 i v2) i estan distanciats per una 
# distància d. El que està darrere viatja a una velocitat més gran. Es demana
# fer un algoritme per ingressar la distància entre els dos vehicles (km) i les seves respectives velocitats (km / h) i amb això determinar i mostrar en què temps (minuts) arribarà el vehicle més ràpid a l'altre.

dv1 = float(input("ingressar distància vehicles: "))
vv1 = float(input("ingressar velocitats vehicles 1: "))
vv2 = float(input("ingressar velocitats vehicles 2: "))

if vv1 > vv2:
    velocitat_mas_rapida = vv1
else : 
    velocitat_mas_rapida = vv2

diferents_velocitat = velocitat_mas_rapida - min(vv1, vv2)

temps_hores = dv1 / diferents_velocitat

temps_minuts = temps_hores * 60

print("el vehiculo mas rapido llegara en: " + str(temps_minuts) + "minuts") 