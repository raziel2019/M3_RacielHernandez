# 16. La política de cobrament d'una companyia telefònica és: quan es realitza una trucada, el cobrament és pel temps que aquesta dura,
# de tal manera que els primers cinc minuts costen 1 euro, els següents 3, 80 cèntims, els següents dos minuts, 70 cèntims, i a partir 
# del desè minut, 50 cèntims.
# A més a més, es carrega un impost de 3% quan és diumenge, i si és un altre dia, en torn de matí, 15%, i en torn de tarda, 10%. Feu un algoritme per determinar quant ha de pagar per cada concepte una persona que realitza una trucada.
duracion = int(input("Introduce la duración de la llamada en minutos: "))
dia = input("Introduce el día de la semana: ").lower()
turno = input("Introduce el turno (mañana o tarde): ").lower()

if duracion <= 5:
    coste = duracion * 1
elif duracion <= 8:
    coste = 5 + (duracion - 5) * 0.80
elif duracion <= 10:
    coste = 5 + 3 * 0.80 + (duracion - 8) * 0.70
else:
    coste = 5 + 3 * 0.80 + 2 * 0.70 + (duracion - 10) * 0.50

if dia == "domingo":
    coste *= 1.03
elif turno == "mañana":
    coste *= 1.15
else:
    coste *= 1.10

print("El coste total de la llamada es:", round(coste, 2), "euros.")
