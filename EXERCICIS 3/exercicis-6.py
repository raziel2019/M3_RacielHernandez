#6. Escriu un programa que generi una cadena de 3 caràcters que inclogui lletres (majúscules i minúscules) i números aleatoris.
import random
import string

caracteres = string.ascii_letters + string.digits
cadena_aleatoria = ''.join(random.choice(caracteres) for _ in range(3))

print("Cadena aleatoria de 3 caracteres:", cadena_aleatoria)
