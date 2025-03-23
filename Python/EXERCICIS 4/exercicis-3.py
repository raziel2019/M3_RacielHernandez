# Añade un método a la clase `Persona` llamado `presenta()` 
# para que responda `"Hola, me llamo Manel y tengo 19 años."`

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presenta(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."

persona = Persona("Manel", 19)
print(persona.presenta())
