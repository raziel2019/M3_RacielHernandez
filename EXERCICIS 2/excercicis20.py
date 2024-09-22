# 20. Dissenyar un algorisme que ens digui els diners que
# tenim (en euros i cèntims) després de demanar-nos quantes monedes tenim 
# (de 2 €, 1 €, 50 cèntims, 20 cèntims o 10 cèntims).

monedes_2e = int(input("Introduce quantes de monedes de 2 € tenim: "))
monedes_1e = int(input("Introduce quantes de monedes de 1 € tenim: "))
monedes_50c = int(input("Introduce quantes de monedes de 50 cèntims tenim: "))
monedes_20c = int(input("Introduce quantes de monedes de 20 cèntims tenim: "))
monedes_10c = int(input("Introduce quantes de monedes de 10 cèntims tenim: "))


euros = (monedes_2e * 2) + (monedes_1e * 1) + (monedes_50c * .5) + (monedes_20c * .20) + (monedes_10c * .10)

euros_en_euros = euros // 1
euros_en_cèntims = int((euros - euros_en_euros) * 100)
print("els diners que tenim es: " + " euros " + str(euros_en_euros) + " cèntims " + str(euros_en_cèntims))