bd = {}
def registro (bd):
    nombre =  input("Ingrese su nombre: ")
    contraseña = input("Ingrese una contraseña segura: ")
    nuevo_usuario = [nombre, contraseña]
    if len(bd) == 0:
        bd['nombre'] = nuevo_usuario[0]
        bd['contraseña'] = nuevo_usuario[1]
    return bd

def leer_data(bd):
    for key, value in bd.items():
        print(f"{key}: {value}")

def login(bd):
    nombre = input ("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese  su contraseña: ")
    while nombre  != bd.get('nombre') or contraseña != bd.get('contraseña'):
        print("Usuario o Contraseña incorrecta")
        nombre = input ("Intente nuevamente ingresando su nombre de usuario: ")
        contraseña = input("Intente nuevamente ingresando su contraseña: ")
    else:
        print("Bienvenido", nombre)


registro(bd)
leer_data(bd)
login(bd)
