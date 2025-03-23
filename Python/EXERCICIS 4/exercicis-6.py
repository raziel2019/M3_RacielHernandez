class Producto:
    def __init__(self, nombre, precio, descuento):
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento
    
    def precio_con_descuento(self):
        return self.precio * (1 - self.descuento / 100)

nombre = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio del producto: "))
descuento = float(input("Introduce el descuento del producto (en porcentaje): "))

producto = Producto(nombre, precio, descuento)

print(f"Producto: {producto.nombre}")
print(f"Precio con descuento: {producto.precio_con_descuento():.2f}")
