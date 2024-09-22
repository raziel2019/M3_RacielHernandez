#19. Escriure un algoritme per calcular la nota final d'un estudiant, 
# considerant que: per cada resposta correcta 5 punts, per una incorrecta -1 i per respostes en 
# blanc 0. Imprimeix el resultat obtingut per l'estudiant.

resposta_correcta = int(input("escribe la cantidad de resposta correcta: "))
resposta_incorrecta = int(input("escribe la cantidad de resposta incorrecta: "))
resposta_blanc = int(input("escribe la cantidad de resposta en blanc: "))

resultat = (resposta_correcta * 5) + ( resposta_incorrecta * -1 )+ (resposta_blanc * 0)

print("resultat obtingut per l'estudiant: " + str(resultat))