from perfil import ver_perfil
from compra import realizar_compra
from carrito import ver_carrito

def menu_despues_inicio_sesion(cliente):
    while True:
        print("======= MENÚ DESPUÉS DEL INICIO DE SESIÓN =======")
        print("1. Ver perfil")
        print("2. Realizar compra")
        print("3. Ver carrito")
        print("4. Salir")
        opcion = input("Ingrese el número de opción que desee: ")

        if opcion == "1":
            ver_perfil(cliente)
        elif opcion == "2":
            realizar_compra(cliente)
        elif opcion == "3":
            ver_carrito(cliente)
        elif opcion == "4":
            print("Hasta luego.")
            break
        else:
            print("Opción inválida. Ingrese un número válido del menú.")
