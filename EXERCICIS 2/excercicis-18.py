# 18. Demanar el nom i els dos cognoms d'una persona i mostrar les inicials.

nom = input("introduce el nom: ")
cognoms_paterno = input("introduce el cognoms paterno: ")
cognoms_materno = input("introduce el cognoms_materno: ")

inicials = nom[0],cognoms_paterno[0],cognoms_materno[0]

print("Las inicials son: " + str(inicials))