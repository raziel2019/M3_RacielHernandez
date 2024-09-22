#17. Un ciclista part d'una ciutat A a les HH hores, MM minuts i SS segons. 
# El temps de viatge fins arribar a una altra ciutat B és de T segons. 
# Escriure un algoritme que determini l'hora d'arribada a la ciutat B.

HH = int(input("Introduce las hores de partida: "))
MM = int(input("Introduce los minuts de partida: "))
SS = int(input("Introduce los segons de partida: "))
T = int(input("Introduce el temps de viatge en segons: "))

segons_inici = HH * 3600 + MM * 60 + SS

segons_arribar = segons_inici + T

HH_arribar = (segons_arribar // 3600) % 24 
MM_arribar = (segons_arribar % 3600) // 60
SS_arribar = segons_arribar % 60

print("la hora de llegada a la ciutat B es: " + str(HH_arribar) + ": " +  str(MM_arribar) + ": " + str(SS_arribar) )
