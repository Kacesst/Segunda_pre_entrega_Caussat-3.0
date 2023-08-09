import json

class Cliente:
    def __init__(self, nombre, apellido, dni, telefono, email, contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono
        self.email = email
        self.contraseña = contraseña
        self.carrito = []

    def agregar_producto_al_carrito(self, producto, cantidad):
        for item in self.carrito:
            if item["producto"] == producto:
                item["cantidad"] += cantidad
                print(f"{cantidad} unidades de {producto.nombre} agregadas al carrito.")
                return

        self.carrito.append({"producto": producto, "cantidad": cantidad})
        print(f"{cantidad} unidades de {producto.nombre} agregadas al carrito.")

    def obtener_total_carrito(self):
        total = 0
        for item in self.carrito:
            producto = item["producto"]
            cantidad = item["cantidad"]
            total += producto.precio * cantidad
        return total

    def guardar_en_json(self):
        cliente_data = {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "dni": self.dni,
            "telefono": self.telefono,
            "email": self.email,
            "contraseña": self.contraseña,
            "carrito": self.carrito
        }

        with open("clientes.json", "w") as archivo:
            json.dump(cliente_data, archivo)

    def cargar_desde_json(self):
        try:
            with open("clientes.json", "r") as archivo:
                cliente_data = json.load(archivo)
                self.nombre = cliente_data["nombre"]
                self.apellido = cliente_data["apellido"]
                self.dni = cliente_data["dni"]
                self.telefono = cliente_data["telefono"]
                self.email = cliente_data["email"]
                self.contraseña = cliente_data["contraseña"]
                
                # Limpiar el carrito actual y cargar los elementos del carrito desde el JSON
                self.carrito = cliente_data["carrito"]
        except FileNotFoundError:
            # Si el archivo no existe, el cliente no está registrado
            pass
