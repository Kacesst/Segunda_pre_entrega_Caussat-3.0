from tienda import Tienda
from cliente import Cliente
from menu_inicio import menu_inicio
from menu_despues_inicio_sesion import menu_despues_inicio_sesion

def main():
    nombre_tienda = "Mi Tienda"
    tienda = Tienda(nombre_tienda)
    menu_inicio(Cliente)
    menu_despues_inicio_sesion (Cliente)

if __name__ == "__main__":
    main()
