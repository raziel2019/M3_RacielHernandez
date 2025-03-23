#5. Escriu un programa que demani a l'usuari una cadena i mostri el primer i l'últim caràcter, els dos en majúscules.
cadena = input("Introduce una cadena: ")

if len(cadena) > 0:
    primero = cadena[0].upper()
    ultimo = cadena[-1].upper()
    print(f"Primer carácter en mayúsculas: {primero}, último carácter en mayúsculas: {ultimo}")
else:
    print("La cadena está vacía.")
