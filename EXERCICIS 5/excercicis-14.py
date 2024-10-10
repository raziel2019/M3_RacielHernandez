#14. L'associació de vinicultors té com a política fixar un preu inicial a el quilo de raïm, 
# la qual es classifica en tipus A i B, i més en mides 1 i 2. Quan es realitza la venda del producte, 
# aquesta és d'un sol tipus i grandària , es requereix determinar quant rebrà un productor pel raïm que lliura en un embarcament, 
# considerant el següent: si és de tipus a, se li carreguen 20 cèntims a el preu inicial quan és de mida 1; i 30 cèntims si és de mida 2. 
# Si és de tipus B, es rebaixen 30 cèntims quan és de mida 1, i 50 cèntims quan és de grandària 2. Feu un algoritme per determinar el guany obtingut.


precio_inicial = float(input("Introduce el precio inicial por kilo: "))
tipo = input("Introduce el tipo de uva (A o B): ").upper()
tamaño = int(input("Introduce el tamaño de la uva (1 o 2): "))
kilos = float(input("Introduce la cantidad de kilos: "))

if tipo == 'A':
    if tamaño == 1:
        precio_inicial += 0.20
    elif tamaño == 2:
        precio_inicial += 0.30
elif tipo == 'B':
    if tamaño == 1:
        precio_inicial -= 0.30
    elif tamaño == 2:
        precio_inicial -= 0.50

ganancia = precio_inicial * kilos
print("El productor recibirá:", ganancia, "euros.")
