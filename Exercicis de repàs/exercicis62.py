# Diseña un algoritmo que, dada una lista de temperaturas diarias durante una semana, 
# calcule y muestre la temperatura media, la máxima y la mínima.

lista_temperaturas = [45,30,27,8,10,28]
temperatura_media = 0
temperatura_maxima = 0
temperatura_minima = 0


for i in lista_temperaturas:
   temperatura_minima = min(lista_temperaturas)
   temperatura_maxima = max(lista_temperaturas)
   temperatura_media = temperatura_media + i

temperatura_media = temperatura_media/6

print(temperatura_media)   
print(temperatura_minima)
print(temperatura_maxima)
 