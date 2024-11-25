#Escribe un programa en Python que simule un sistema de seguridad de una sala de ordenadores. 
# La contraseña para acceder es un código numérico de cuatro dígitos: "1234". 
# El programa debe pedir al usuario que introduzca el código de acceso y le permitirá un máximo de 3 intentos.
# Si el usuario falla los 3 intentos, el programa debe mostrar un mensaje de advertencia que indique que se ha 
# activado el sistema de alarma y bloqueado el acceso. Si el usuario acierta el código, el programa debe finalizar
#  de inmediato y mostrar un mensaje de bienvenida a la sala de ordenadores.

password = "1234"
contador = 0
veces_permitidas = 3

while contador < veces_permitidas:  
    enter_password = input("Introduzca el código de acceso: ")
    
    if enter_password == password:  
        print("Bienvenido a la sala de ordenadores")
        break  

    else:  
        contador += 1
        print(f"Has fallado. Te quedan {veces_permitidas - contador} intentos.")
        
if contador == veces_permitidas:  
    print("Se ha activado el sistema de alarma y el acceso ha sido bloqueado.")

