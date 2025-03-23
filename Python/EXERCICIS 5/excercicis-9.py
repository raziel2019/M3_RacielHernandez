#9. Algorisme que demani tres nombres i els mostri ordenats (de més a menys);
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

numeros = [num1, num2, num3]
numeros.sort(reverse=True)

print("Números ordenados de mayor a menor:", numeros)
