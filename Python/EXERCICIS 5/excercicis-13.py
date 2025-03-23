# 13. Escriu un programa que demani una data (dia, mes i any) i digui si és correcta.

dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
año = int(input("Introduce el año: "))

es_fecha_valida = False

if 1 <= mes <= 12:
    if mes in (1, 3, 5, 7, 8, 10, 12):
        es_fecha_valida = 1 <= dia <= 31
    elif mes in (4, 6, 9, 11):
        es_fecha_valida = 1 <= dia <= 30
    elif mes == 2:
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            es_fecha_valida = 1 <= dia <= 29
        else:
            es_fecha_valida = 1 <= dia <= 28

if es_fecha_valida:
    print("La fecha es correcta.")
else:
    print("La fecha es incorrecta.")
