import random

class Dado:
    @staticmethod
    def lanzar():
        return random.randint(1, 6)

lanzamientos = [Dado.lanzar() for _ in range(4)]

print(" ".join(map(str, lanzamientos)))
