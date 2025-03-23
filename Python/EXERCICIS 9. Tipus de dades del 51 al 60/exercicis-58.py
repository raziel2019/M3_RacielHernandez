# Fer un programa que demani per teclat les següents dades
# *  Els ingressos que Joan ha rebut durant els dotze mesos de l'any.
# *  La quantitat a cercar a dintre del vector.
# Com a resultat de la cerca el programa ens ha de dir si Joan ha rebut o no aquesta quantitat, i en cas positiu, ens digui en quin mes l'ha cobrat (gener, febrer, ...).


class IngresosJoan:
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    ingresos = [0] * 12
    encontrado = False

    def __init__(self):
        print("Introduce los ingresos de Joan para cada mes del año:")
        for i in range(12):
            self.ingresos[i] = float(input(f"Ingreso para {self.meses[i]}: "))

        cantidad_buscar = float(input("Introduce la cantidad a buscar entre los ingresos: "))
        
        for i in range(12):
            if self.ingresos[i] == cantidad_buscar:
                print(f"Joan recibió {cantidad_buscar} en el mes de {self.meses[i]}.")
                self.encontrado = True
                break
        
        if not self.encontrado:
            print("Joan no ha recibido esa cantidad en ninguno de los meses.")

IngresosJoan()