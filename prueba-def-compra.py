productos = {
    1: {"nombre": "Manzana", "precio": 0.50},
    2: {"nombre": "Pan", "precio": 1.20},
    3: {"nombre": "Leche", "precio": 0.90},
    4: {"nombre": "Huevos", "precio": 2.50},
}

carrito = []


def mostrar_menu():
    print("Tienda básica")
    print("Productos disponibles:")
    for codigo, info in productos.items():
        print(f"{codigo}. {info['nombre']} - ${info['precio']:.2f}")
    print("0. Finalizar compra")


def agregar_producto(codigo, cantidad):
    if codigo in productos and cantidad > 0:
        carrito.append({"codigo": codigo, "cantidad": cantidad})
        print(
            f"Agregado {cantidad} x {productos[codigo]['nombre']} al carrito.")
    else:
        print("Producto inválido o cantidad incorrecta.")


def calcular_total():
    total = 0
    for item in carrito:
        info = productos[item["codigo"]]
        total += info["precio"] * item["cantidad"]
    return total


def mostrar_factura():
    if not carrito:
        print("No hay productos en el carrito.")
        return
    print("\nFactura:")
    for item in carrito:
        info = productos[item["codigo"]]
        subtotal = info["precio"] * item["cantidad"]
        print(f"- {info['nombre']} x {item['cantidad']} = ${subtotal:.2f}")
    total = calcular_total()
    print(f"Total a pagar: ${total:.2f}")


def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione el código del producto: "))
        except ValueError:
            print("Ingrese un número válido.")
            continue

        if opcion == 0:
            break

        if opcion not in productos:
            print("Opción no válida.")
            continue

        try:
            cantidad = int(input("Cantidad: "))
        except ValueError:
            print("Ingrese una cantidad válida.")
            continue

        agregar_producto(opcion, cantidad)

    mostrar_factura()

    if carrito:
        total = calcular_total()
        while True:
            try:
                pago = float(input("Ingrese el monto de pago: $"))
            except ValueError:
                print("Ingrese un monto numérico válido.")
                continue
            if pago < total:
                print("Pago insuficiente. Intente de nuevo.")
                continue
            cambio = pago - total
            print(f"Pago recibido: ${pago:.2f}")
            print(f"Cambio: ${cambio:.2f}")
            print("Gracias por su compra.")
            break


if __name__ == "__main__":
    main()
