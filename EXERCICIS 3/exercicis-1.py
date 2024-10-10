#1. Escriu un programa que demani a l'usuari dues dates específiques en format YYYY-MM-D. Mostra la diferència en dies entre aquestes dues dates.
from datetime import datetime

fecha1 = input("introduce la primera fecha: ")
fecha2 = input("introduce la segunda fecha: ")

fecha_y_hora = datetime.strptime(fecha1, "%Y-%m-%d")
fecha_y_hora2 = datetime.strptime(fecha2, "%Y-%m-%d")

diferencia_dias = (fecha_y_hora - fecha_y_hora2 )

print(diferencia_dias)