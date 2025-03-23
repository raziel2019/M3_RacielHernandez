import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * (self.radio ** 2)

radio = float(input("Introduce el radio del círculo: "))
circulo = Circulo(radio)

print(f"El área del círculo es: {circulo.calcular_area():.2f}")
