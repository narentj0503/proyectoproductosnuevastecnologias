class Producto:
    def _init_(self, producto_id, nombre, descripcion, costo, cantidad, margen_de_venta):
        self.id = producto_id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.precio_de_venta = self.calcular_precio_venta(margen_de_venta)

    def calcular_precio_venta(self, margen_de_venta):
        return self.costo / (1 - margen_de_venta)

class RegistroProductos:
    def _init_(self):
        self.productos = {}

    def registrar_producto(self, producto):
        self.productos[producto.id] = {
            'nombre': producto.nombre,
            'descripcion': producto.descripcion,
            'costo': producto.costo,
            'cantidad': producto.cantidad,
            'precio_de_venta': producto.precio_de_venta
        }

    def imprimir_listado(self):
        for producto_id, producto_info in self.productos.items():
            print(f"ID: {producto_id}")
            print(f"Nombre: {producto_info['nombre']}")
            print(f"Descripción: {producto_info['descripcion']}")
            print(f"Costo: {producto_info['costo']}")
            print(f"Cantidad: {producto_info['cantidad']}")
            print(f"Precio de Venta: {producto_info['precio_de_venta']}")
            print("-----------------------------")

if __name__ == "_main_":
    registro = RegistroProductos()

    producto_id_1 = int(input("Ingrese el ID del Producto 1: "))
    nombre_1 = input("Ingrese el nombre del Producto 1: ")
    descripcion_1 = input("Ingrese la descripción del Producto 1: ")
    costo_1 = float(input("Ingrese el costo del Producto 1: "))
    cantidad_1 = int(input("Ingrese la cantidad del Producto 1: "))

    margen_1 = float(input("Ingrese el margen de venta para el Producto 1 (porcentaje): ")) / 100

    producto1 = Producto(
        producto_id=producto_id_1,
        nombre=nombre_1,
        descripcion=descripcion_1,
        costo=costo_1,
        cantidad=cantidad_1,
        margen_de_venta=margen_1
    )
    registro.registrar_producto(producto1)

    producto_id_2 = int(input("Ingrese el ID del Producto 2: "))
    nombre_2 = input("Ingrese el nombre del Producto 2: ")
    descripcion_2 = input("Ingrese la descripción del Producto 2: ")
    costo_2 = float(input("Ingrese el costo del Producto 2: "))
    cantidad_2 = int(input("Ingrese la cantidad del Producto 2: "))

    margen_2 = float(input("Ingrese el margen de venta para el Producto 2 (porcentaje): ")) / 100

    producto2 = Producto(
        producto_id=producto_id_2,
        nombre=nombre_2,
        descripcion=descripcion_2,
        costo=costo_2,
        cantidad=cantidad_2,
        margen_de_venta=margen_2
    )
    registro.registrar_producto(producto2)

    registro.imprimir_listado()
