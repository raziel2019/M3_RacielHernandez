# 10. Un alumne vol saber quin serà el seu qualificació final en la matèria de Algorismes. Aquesta qualificació es compon dels següents percentatges:
# 55% de la mitjana dels seus tres qualificacions parcials.
# 30% de la qualificació de l'examen final.
# 15% de la qualificació d'un treball final.


parcial1 = int(input("introduce el primer parcial: "))
parcial2 = int(input("introduce el segundo parcial: "))
parcial3 = int(input("introduce el tercero parcial: "))

lexamen_final = int(input("introduce la qualificació de l'examen final: "))
treball_final = int(input("introduce la qualificació de treball final: "))

promedio_mitjana = (parcial1 + parcial2 + parcial3) / 3

porcentaje_final = (promedio_mitjana * .55) + (lexamen_final * .30) + (treball_final * .15)

print("La qualificació final es: " + str(porcentaje_final))
