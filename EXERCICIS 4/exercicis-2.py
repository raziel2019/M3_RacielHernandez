# Añade a la clase anterior un método para que muestre 
# el nombre y la edad de la persona en este formato: `"Nombre: Manel, Edad: 19"`.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def mostrar(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

persona = Persona("Manuel", 19)
print(persona.mostrar())