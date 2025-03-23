#Algorisme que sumi tots els nombres parells compresos entre 2 i 100.

acumulador = 0

for i in range(2,101):
    if i % 2 == 0:
      print(i)
      acumulador = acumulador + i
print(acumulador)