# Crea un programa en Python que simule un sistema para calcular el porcentaje de plantas de un jardín 
# que necesitan riego. El programa debe pedir al usuario que introduzca el nivel de humedad de cada planta 
# (en un valor numérico), uno por uno, hasta que el usuario deje la entrada en blanco para indicar que ha terminado. 
# Una planta se considera que necesita riego si su nivel de humedad es inferior a 30. El programa debe calcular y mostrar el 
# porcentaje de plantas que necesitan riego en comparación con el total de plantas introducidas. 

acumulador_plantas_necesitan_riego = []
acumulador_plantas_introducidas = []

while True:
    nivel_humedad = input("Introduzca el nivel de humedad de cada planta (o presione Enter para salir): ")
    
    if nivel_humedad == "":

        total_plantas = len(acumulador_plantas_introducidas)
        total_necesitan_riego = len(acumulador_plantas_necesitan_riego)
        
        if total_plantas > 0:
            porcentaje_plantas_riego = (total_necesitan_riego / total_plantas) * 100
        else:
            porcentaje_plantas_riego = 0
        
        print("\nEl programa ha terminado.")
        print(f"Total de plantas introducidas: {total_plantas}")
        print(f"Total de plantas que necesitan riego: {total_necesitan_riego}")
        print(f"Porcentaje de plantas que necesitan riego: {porcentaje_plantas_riego:.2f}%")
        break

        nivel_humedad = int(nivel_humedad)
        acumulador_plantas_introducidas.append(nivel_humedad)
        
        if nivel_humedad < 30:
            print("La planta necesita riego.")
            acumulador_plantas_necesitan_riego.append(nivel_humedad)
        else:
            print("La planta tiene suficiente agua.")
    