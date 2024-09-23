# 7. Realitza un programa que rebi una quantitat 
# de minuts i mostri per pantalla a quantes hores i minuts correspon.
# Per exemple: 1000 minuts són 16 hores i 40 minuts.

quantitat_minuts = int(input("escriu: "))

conversion_hores = int(quantitat_minuts / 60)

conversion_resto_minutes = (quantitat_minuts % 60)


print(str(quantitat_minuts) + " minuts són " + str(conversion_hores) + " hores " +"i " + str(conversion_resto_minutes)  + " minuts.")