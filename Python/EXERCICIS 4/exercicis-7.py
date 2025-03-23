class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b

    @staticmethod
    def restar(a, b):
        return a - b

    @staticmethod
    def multiplicar(a, b):
        return a * b

    @staticmethod
    def dividir(a, b):
        if b == 0:
            return "No se puede dividir por cero"
        return a / b

numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

print(f"Suma: {Calculadora.sumar(numero1, numero2)}")
print(f"Resta: {Calculadora.restar(numero1, numero2)}")
print(f"Multiplicación: {Calculadora.multiplicar(numero1, numero2)}")
print(f"División: {Calculadora.dividir(numero1, numero2)}")
