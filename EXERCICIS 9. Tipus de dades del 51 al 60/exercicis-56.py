#56.- Demanem 10 valors a l'usuari i els emmagatzemem en un vector de 10 posicions. 
# Seguidament demanem un valor a l'usuari que buscarem dins el vector. 
# Finalment mostrarem per pantalla en quina posició l'hem guardat, si no el troba li diem que no hi és.

class BuscadorEnVector:
    vector = [None] * 10
    encontrado = False

    def __init__(self):
        print("Introduce 10 valores para el vector:")
        for i in range(10):
            self.vector[i] = input(f"Valor {i + 1}: ")

        valor_buscar = input("Introduce el valor a buscar en el vector: ")
        
        for i in range(10):
            if self.vector[i] == valor_buscar:
                print(f"El valor {valor_buscar} se encuentra en la posición {i}.")
                self.encontrado = True
                break
        
        if not self.encontrado:
            print("El valor no está en el vector.")

BuscadorEnVector()