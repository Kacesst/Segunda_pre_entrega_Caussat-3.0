import json

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.clientes = []
        
        
    def iniciar_sesion(self, email, password):
        for cliente in self.clientes:
            if cliente.correo == email and cliente.contraseña == password:
                return cliente
        return None
        
    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print("¡Cliente registrado con éxito!")   

    
    def cargar_datos_json(archivo, tienda):
        try:
            with open(archivo, "r") as file:
                data = json.load(file)
                tienda.clientes = data.get("clientes", [])
                tienda.empleados = data.get("empleados", [])
                tienda.productos = data.get("productos", [])
        except FileNotFoundError:
            print(f"El archivo {archivo} no existe.")

    def guardar_datos_json(archivo, tienda):
        data = {
            "clientes": tienda.clientes,
            "empleados": tienda.empleados,
            "productos": tienda.productos
    }
        with open(archivo, "w") as file:
            json.dump(data, file, indent=4)

#(if __name__ == "__main__":nombre_tienda = "Mi Tienda"archivo_json = "datos.json"tienda = Tienda(nombre_tienda)tienda.cargar_datos_json(archivo_json))
    