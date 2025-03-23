#5. Escriu un programa que demani un nom d'usuari i una contrasenya i si
# s'ha introduït "anna" i "12345" s'indica "Has entrat a sistema", sinó es dona un error.

usuario = input("Introduce el nombre de usuario: ")
contraseña = input("Introduce la contraseña: ")

if usuario == "anna" and contraseña == "12345":
    print("Has entrado al sistema.")
else:
    print("Error: Nombre de usuario o contraseña incorrectos.")
