# Escribe un programa que genere tres números aleatorios entre 1 y 100,
# los muestre y luego muestre su suma.

import random

numeroRandom1 = random.randrange(100)
numeroRandom2 = random.randrange(100)
numeroRandom3 = random.randrange(100)

suma = numeroRandom1 + numeroRandom2 + numeroRandom3

print(f"Numero 1: {numeroRandom1}, Numero 2: {numeroRandom2} , Numero 3: {numeroRandom3} , Suma: {suma} ")

