#12. Escriure un programa que llegeixi un any indicar si és de traspàs. 
# Nota: un any és de traspàs si és un nombre divisible per 4, però no si 
# és divisible per 100, excepte que també sigui divisible per 400.

año = int(input("Introduce un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")



