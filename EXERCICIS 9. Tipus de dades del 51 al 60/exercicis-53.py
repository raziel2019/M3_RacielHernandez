#53.- Fer un programa per què et calculi el percentatge d'aprovats en una  assignatura  d'un vector 
# on  hi ha emmagatzemades les notes dels alumnes de la classe. 
# El vector s'anirà omplint per teclat fins que el programa trobi un input sense cap caràcter.

class CalculadoraAprobados:
    notas = []
    aprobados = 0
    porcentaje_aprobados = 0

    def __init__(self):
        entrada = "0"
        while entrada != "":
            entrada = input("Introduce la nota del alumno (pulsa Enter para finalizar): ")
            if entrada != "":
                try:
                    nota = float(entrada)
                    if 0 <= nota <= 10:
                        self.notas.append(nota)
                    else:
                        print("Introduce una nota entre 0 y 10.")
                except ValueError:
                    print("Por favor, introduce un número válido.")

        if self.notas:
            self.aprobados = sum(1 for nota in self.notas if nota >= 5.0)
            self.porcentaje_aprobados = (self.aprobados / len(self.notas)) * 100
            print(f"Porcentaje de aprobados: {self.porcentaje_aprobados:.2f}%")
        else:
            print("No se han ingresado notas.")

CalculadoraAprobados()