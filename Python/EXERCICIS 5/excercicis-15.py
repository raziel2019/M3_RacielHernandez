# 15. El director d'una escola està organitzant un viatge d'estudis, i requereix determinar quant ha de cobrar a cada alumne 
# i quant ha de pagar a la companyia de viatges pel servei. La manera de cobrar és la següent: si són 100 alumnes o més, 
# el cost per cada alumne és de 65 euros; de 50 a 99 alumnes, el cost és de 70 euros, de 30 a 49, de 95 euros, i si són menys de 30, 
# el cost de la renda de l'autobús és de 4000 euros, sense importar el nombre d'alumnes.
# Feu un algoritme que permeti determinar el pagament a la companyia d'autobusos i el que ha de pagar cada alumne pel viatge.


alumnos = int(input("Introduce el número de alumnos: "))

if alumnos >= 100:
    coste_por_alumno = 65
elif 50 <= alumnos < 100:
    coste_por_alumno = 70
elif 30 <= alumnos < 50:
    coste_por_alumno = 95
else:
    coste_total = 4000
    print("El costo total es de 4000 euros.")
    print("Cada alumno debe pagar:", coste_total / alumnos, "euros.")
    exit()

coste_total = coste_por_alumno * alumnos
print("El costo total es de:", coste_total, "euros.")
print("Cada alumno debe pagar:", coste_por_alumno, "euros.")
