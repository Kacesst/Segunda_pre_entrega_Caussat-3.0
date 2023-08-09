from cliente import Cliente
def registrar_cliente():
    print("======= REGISTRO DE NUEVO CLIENTE =======")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    contraseña = input("Contraseña: ")
    
    

def registrar_nuevo_cliente(nombre, apellido, dni, telefono, correo, contraseña):
    nuevo_cliente = Cliente(nombre, apellido, dni, telefono, correo, contraseña)
    # Agrega la lógica necesaria para agregar el nuevo cliente a la lista de clientes en la tienda
    return nuevo_cliente
    
