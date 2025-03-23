#  Escribe un programa que genere una hora específica al azar (por ejemplo, las 10:30:00) y muestre cuánto tiempo
#  ha pasado hasta ahora, en horas, minutos y segundos.

import random
from datetime import datetime, timedelta


hora_aleatoria = datetime.now().replace(hour=random.randint(0, 23), minute=random.randint(0, 59), second=random.randint(0, 59))
hora_actual = datetime.now()

diferencia = hora_actual - hora_aleatoria

horas = diferencia.seconds // 3600
minutos = (diferencia.seconds % 3600) // 60
segundos = diferencia.seconds % 60

print("Hora aleatoria generada:", hora_aleatoria.time())
print(f"Tiempo transcurrido desde entonces: {horas} horas, {minutos} minutos y {segundos} segundos.")





