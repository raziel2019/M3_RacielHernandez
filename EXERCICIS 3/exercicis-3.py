#  Escribe un programa que genere una hora específica al azar (por ejemplo, las 10:30:00) y muestre cuánto tiempo
#  ha pasado hasta ahora, en horas, minutos y segundos.

import random
from datetime import datetime

hoy = ""
hora = random.randrange(0,24)
minutos = random.randrange(0,60)
segundos = random.randrange(0,60)

hora_string = str(hora)
minutos_string = str(minutos)
segundos_string = str(segundos)

hora_al_azar = hora_string + ":" + minutos_string + ":" + segundos_string

hora_desarrollada = datetime.strptime(hora_al_azar, "%H:%M:%S").time()

current_dateTime = datetime.now()

print(current_dateTime)

print(hoy)





