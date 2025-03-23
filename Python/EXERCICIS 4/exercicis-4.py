class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def saluda(self, nombre):
        return f"Hola {nombre}, soy {self.nombre}."

persona = Persona("Manuel", 19)

nombre_saludo = input("¿Cuál es tu nombre? ")

print(persona.saluda(nombre_saludo))
