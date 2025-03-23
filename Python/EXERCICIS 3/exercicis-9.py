#9. Escriu un programa que mesuri quant temps triga en executar-se una operació, com per exemple calcular l'arrel quadrada de 3 números diferents.
# Utilitza datetime.now() per obtenir el temps abans i després de l'operació, i resta’ls per calcular el temps total d'execució.


from datetime import datetime
import math

inicio = datetime.now()

math.sqrt(12345)
math.sqrt(67890)
math.sqrt(24680)

fin = datetime.now()
tiempo_ejecucion = fin - inicio

print("Tiempo de ejecución:", tiempo_ejecucion)
