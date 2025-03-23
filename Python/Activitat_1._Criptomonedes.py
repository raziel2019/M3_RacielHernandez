#Actualment estàs invertint en tres criptomonedes diferents. Avui has comprat les següents quantitats a diferents preus:
#Bitcoin (BTC): 0.5 BTC a 27,000 euros/BTC.
#Ethereum (ETH): 2 ETH a 1,800 euros/ETH.
#Ripple (XRP): 1000 XRP a 0.50 euros/XRP.
#El teu objectiu és calcular:
#El valor total de la inversió.
#El valor de cada criptomoneda.
#El percentatge que representa cada criptomoneda sobre el valor total de la inversió.
#El rendiment de la inversió (ROI), que es calcula com 
#((valor_total - cost_total_inicial) / cost_total_inicial) * 100

cantidad_BTC = 0.5
precio_BTC = 27000
cantidad_ETH = 2
precio_ETH = 1800
cantidad_XRP = 1000
precio_XRP = 0.50

valor_BTC = cantidad_BTC * precio_BTC
valor_ETH = cantidad_ETH * precio_ETH
valor_XRP = cantidad_XRP * precio_XRP

valor_total_inversion = valor_BTC + valor_ETH + valor_XRP

porcentaje_BTC = (valor_BTC / valor_total_inversion) * 100
porcentaje_ETH = (valor_ETH / valor_total_inversion) * 100
porcentaje_XRP = (valor_XRP / valor_total_inversion) * 100

coste_total_inicial = 15000

ROI = ((valor_total_inversion - coste_total_inicial) / coste_total_inicial) * 100


print("Valor de la inversió en Bitcoin: " + str(valor_BTC) + " euros")
print("Valor de la inversió en Ethereum: " + str(valor_ETH) + " euros")
print("Valor de la inversió en Ripple: " + str(valor_XRP) + " euros")
print("Valor total de la inversió: " + str(valor_total_inversion) + " euros")
print("Percentatge de Bitcoin: " + str(porcentaje_BTC))
print("Percentatge d'Ethereum: " + str(porcentaje_ETH))
print("Percentatge de Ripple: " + str(porcentaje_XRP))
print("Rendiment de la inversió (ROI): " + str(ROI))