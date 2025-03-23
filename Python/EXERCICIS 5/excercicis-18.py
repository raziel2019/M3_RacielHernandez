#18. Realitza un programa que demani el dia de la setmana (de l'1 a l'7) i escriviu el dia corresponent. Si introduïm un altre número ens dóna un error.


dia = int(input("Introduce un número de día de la semana (1-7): "))

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miércoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sábado")
elif dia == 7:
    print("Domingo")
else:
    print("ERROR: número de día incorrecto.")
