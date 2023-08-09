import json

class Producto:
    def __init__(self, nombre, tipo, marca, modelo, color, precio, stock, descripcion, tallas_stock, diseño):
        self.nombre = nombre
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.precio = precio
        self.stock = stock
        self.descripcion = descripcion
        self.tallas_stock = tallas_stock
        self.diseño = diseño

def cargar_productos_desde_json(archivo):
    productos = []
    try:
        with open(archivo, "r") as file:
            data = json.load(file)
            for producto_data in data:
                producto = Producto(**producto_data)
                productos.append(producto)
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe.")
    return productos

if __name__ == "__main__":
    archivo_json = "productos.json"
    productos = cargar_productos_desde_json(archivo_json)
    for producto in productos:
        print("Nombre:", producto.nombre)
        print("Precio:", producto.precio)
        print("Stock:", producto.stock)
        print("-----------------------")
