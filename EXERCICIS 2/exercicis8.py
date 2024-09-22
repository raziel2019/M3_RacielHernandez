#8. Un venedor rep un sou base més un 10% extra
# per comissió de les seves vendes, el venedor vol saber quants
# diners obtindrà per concepte de comissions per les tres vendes que realitza en el mes 
# i el total que rebrà al mes tenint en compte el seu sou base i comissions.

sou_base = float(input("Introduce sou base: "))

vendes1 = float(input("Introduce vendes 1: "))
vendes2 = float(input("Introduce vendes 2: "))
vendes3 = float(input("Introduce vendes 3: "))

comissions = (vendes1 +vendes2 + vendes3) * .10

total_sou = sou_base + comissions

print("el total que rebrà al mes tenint en compte el seu sou base i comissions: " + str(total_sou))