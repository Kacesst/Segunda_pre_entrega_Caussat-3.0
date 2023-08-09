from tienda import Tienda
from cliente import Cliente


def menu_inicio(tienda):
    while True:
        print("======= MENÚ DE INICIO =======")
        print("1. Ingresar a su cuenta")
        print("2. Registrarse como nuevo cliente")
        print("3. Salir")
        opcion = input("Ingrese el número de opción que desee: ")

        if opcion == "1":
            email = input("Ingrese su correo electrónico: ")
            password = input("Ingrese su contraseña: ")
            cliente = tienda.iniciar_sesion(email, password)
            if cliente:
                print("Inicio de sesión exitoso.")
                
            else:
                print("Inicio de sesión fallido. Correo electrónico o contraseña incorrectos.")
        elif opcion == "2":
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            dni = input("Ingrese su DNI: ")
            telefono = input("Ingrese su teléfono: ")
            correo = input("Ingrese su correo electrónico: ")
            contraseña = input("Ingrese su contraseña: ")
            nuevo_cliente = Cliente(nombre, apellido, dni, telefono, correo, contraseña)
            tienda.registrar_cliente(nuevo_cliente)  
            print("Cliente registrado con éxito.")
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido del menú.")
