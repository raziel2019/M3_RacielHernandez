# Crea una clase `Persona` con atributos `nombre` y `edad`. 
# Crea un objeto de tipo `Persona` con `nombre = "Manel"` y `edad = 19`. 
# Imprime el objeto. ¿Qué ves?

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

persona = Persona("Manel", 19)
print(persona)
