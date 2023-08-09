import json
class Empleado:
    def __init__(self, nombre, apellido, dni, telefono, email, contraseña, cargo):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono
        self.email = email
        self.contraseña = contraseña
        self.cargo = cargo

def cargar_empleados():
    try:
        with open("empleados.json", "r") as file:
            empleados_data = json.load(file)
            empleados = [Empleado(**data) for data in empleados_data]
        return empleados
    except FileNotFoundError:
        return []

def guardar_empleados(empleados):
    empleados_data = [{"nombre": emp.nombre, "apellido": emp.apellido, "dni": emp.dni,
                       "telefono": emp.telefono, "email": emp.email, "contraseña": emp.contraseña,
                       "cargo": emp.cargo} for emp in empleados]
    with open("empleados.json", "w") as file:
        json.dump(empleados_data, file, indent=4)

def menu_gestion_empleados():
    empleados = cargar_empleados()

    while True:
        print("===== MENÚ DE GESTIÓN DE EMPLEADOS =====")
        print("1. Mostrar lista de empleados")
        print("2. Agregar nuevo empleado")
        print("3. Salir")
        opcion = input("Ingrese el número de opción que desee: ")

        if opcion == "1":
            if not empleados:
                print("No hay empleados registrados.")
            else:
                print("Lista de empleados:")
                for i, emp in enumerate(empleados, start=1):
                    print(f"{i}. {emp.nombre} {emp.apellido} - {emp.cargo}")
        elif opcion == "2":
            nombre = input("Ingrese el nombre del nuevo empleado: ")
            apellido = input("Ingrese el apellido del nuevo empleado: ")
            dni = input("Ingrese el DNI del nuevo empleado: ")
            telefono = input("Ingrese el teléfono del nuevo empleado: ")
            email = input("Ingrese el correo electrónico del nuevo empleado: ")
            contraseña = input("Ingrese la contraseña del nuevo empleado: ")
            cargo = input("Ingrese el cargo del nuevo empleado: ")
            nuevo_empleado = Empleado(nombre, apellido, dni, telefono, email, contraseña, cargo)
            empleados.append(nuevo_empleado)
            guardar_empleados(empleados)
            print("Empleado agregado con éxito.")
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    menu_gestion_empleados()
