#4. Crea un programa que demani a l'usuari dos nombres i mostri la seva divisió si el segon no és zero, o un missatge d'avís en cas contrari.

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if num2 != 0:
    print("La división es:", num1 / num2)
else:
    print("Error: No se puede dividir por cero.")

