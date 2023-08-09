import json
def iniciar_sesion():
    print("======= INICIO DE SESIÓN =======")
    email = input("Email: ")
    contraseña = input("Contraseña: ")

    # Cargar clientes existentes desde el archivo
    try:
        with open("data/clientes.json", "r") as archivo_clientes:
            clientes = json.load(archivo_clientes)
    except FileNotFoundError:
        clientes = []

    # Verificar las credenciales ingresadas
    for cliente in clientes:
        if cliente["email"] == email and cliente["contraseña"] == contraseña:
            print("Inicio de sesión exitoso.")
            return cliente
    print("Correo o contraseña incorrectos. Inténtalo nuevamente.")
    return None