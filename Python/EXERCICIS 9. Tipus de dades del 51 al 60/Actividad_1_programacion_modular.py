def calculadora(num1, num2, operacion):
    if operacion == '+':
        return num1 + num2
    elif operacion == '-':
        return num1 - num2
    elif operacion == '*':
        return num1 * num2
    elif operacion == '/':
        if num2 == 0:
            return "Error: No se puede dividir por cero."
        return num1 / num2
    else:
        return "Error: Operación no válida."

resultados = [
    ("Suma (10 + 5)", calculadora(10, 5, '+')),
    ("Resta (10 - 5)", calculadora(10, 5, '-')),
    ("Multiplicación (10 * 5)", calculadora(10, 5, '*')),
    ("División (10 / 5)", calculadora(10, 5, '/')),
    ("División por cero (10 / 0)", calculadora(10, 0, '/')),
    ("Operación no válida (10 ^ 5)", calculadora(10, 5, '^')),
]

for caso, resultado in resultados:
    print(f"{caso}: {resultado}")
