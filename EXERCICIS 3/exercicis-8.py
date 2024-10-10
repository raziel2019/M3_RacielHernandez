#8. Escriu un programa que generi un color aleatori en format RGB. Cada component (R, G, B) ha de ser un valor entre 0 i 255.

import random

R = random.randint(0, 255)
G = random.randint(0, 255)
B = random.randint(0, 255)

print(f"Color RGB aleatorio: ({R}, {G}, {B})")
