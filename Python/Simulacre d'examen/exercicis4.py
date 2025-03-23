# Crea un programa en Python que ayude a un estudiante a revisar su vocabulario para un examen de idiomas.
# Primero, el estudiante debe introducir una frase o párrafo que simule su vocabulario de estudio. 
# A continuación, el programa le pedirá que introduzca una palabra específica para verificar si ya la sabe 
# (si se encuentra dentro de su vocabulario). El programa deberá comprobar si la palabra forma parte del vocabulario
# introducido y mostrar un mensaje indicando si la palabra está ahí o no.


frase = input("Introduce una frase o párrafo con tu vocabulario de estudio: ").lower()
vocabulario = []

for palabra in frase.split():
    if palabra not in vocabulario:
        vocabulario.append(palabra)

while True:
    palabra_conocida = input("Introduce una palabra específica para verificar (o escribe 'salir' para terminar): ").lower()
    
    if palabra_conocida == 'salir':
        print("Gracias por usar el programa. ¡Éxito en tu examen!")
        break
    
    if palabra_conocida in vocabulario:
        print("¡Conoces la palabra!")
    else:
        print("No conoces la palabra.")

