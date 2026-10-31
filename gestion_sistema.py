# SISTEMA DE GESTIÓN DE INVENTARIO Y PEDIDOS

# Estructuras de datos globales (Diccionarios para búsquedas rápidas)
# inventario = { "ID_PROD": {"nombre": "...", "cantidad": 0, "precio": 0.0} }
inventario = {}
# pedidos = { "ID_PED": {"cliente": "...", "id_producto": "...", "cantidad": 0} }
pedidos = {}

# MÓDULO 1: GESTIÓN DE INVENTARIO (PRODUCTOS)

def registrar_producto():
    """Procedimiento para registrar un nuevo producto en el sistema."""
    print("REGISTRAR PRODUCTO ")
    id_prod = input("Ingrese el ID del producto (Ej. P01): ").strip().upper()
    
    if id_prod in inventario:
        print("Error: El ID del producto ya existe.")
        return

    nombre = input("Nombre del producto: ").strip()
    try:
        cantidad = int(input("Cantidad en stock: "))
        precio = float(input("Precio unitario: $"))
        
        inventario[id_prod] = {
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio
        }
        print("¡Producto registrado con éxito!")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos para cantidad y precio.")

def mostrar_inventario():
    """Función para mostrar todos los productos registrados."""
    print(" INVENTARIO ACTUA")
    if not inventario:
        print("El inventario está vacío.")
        return
    
    print(f"{'ID':<10} | {'NOMBRE':<20} | {'CANTIDAD':<10} | {'PRECIO'}")
    print("-" * 60)
    for id_prod, datos in inventario.items():
        print(f"{id_prod:<10} | {datos['nombre']:<20} | {datos['cantidad']:<10} | ${datos['precio']:.2f}")

def editar_producto():
    """Procedimiento para modificar los datos de un producto existente."""
    print("\n--- EDITAR PRODUCTO ---")
    id_prod = input("Ingrese el ID del producto a editar: ").strip().upper()
    
    if id_prod not in inventario:
        print("Error: Producto no encontrado.")
        return
    
    print(f"Editando: {inventario[id_prod]['nombre']}")
    try:
        nueva_cant = int(input("Nueva cantidad (o mismo valor): "))
        nuevo_precio = float(input("Nuevo precio (o mismo valor): $"))
        
        inventario[id_prod]["cantidad"] = nueva_cant
        inventario[id_prod]["precio"] = nuevo_precio
        print("¡Producto actualizado con éxito!")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")

def eliminar_producto():
    """Procedimiento para eliminar un producto del sistema."""
    print("ELIMINAR PRODUCTO")
    id_prod = input("Ingrese el ID del producto a eliminar: ").strip().upper()
    
    if id_prod in inventario:
        del inventario[id_prod]
        print("¡Producto eliminado con éxito!")
    else:
        print("Error: Producto no encontrado.")


# MÓDULO 2: GESTIÓN DE PEDIDOS

def registrar_pedido():
    """Procedimiento para registrar un pedido validando el stock."""
    print("REGISTRAR PEDIDO")
    id_ped = input("Ingrese el ID del pedido (Ej. V01): ").strip().upper()
    
    if id_ped in pedidos:
        print("Error: El ID del pedido ya existe.")
        return
    
    cliente = input("Nombre del cliente: ").strip()
    id_prod = input("ID del producto a comprar: ").strip().upper()
    
    if id_prod not in inventario:
        print("Error: El producto solicitado no existe en el inventario.")
        return
    
    try:
        cantidad_pedida = int(input("Cantidad solicitada: "))
        
        # Lógica de negocio: Validar que haya stock suficiente
        if cantidad_pedida <= inventario[id_prod]["cantidad"]:
            # Descontar del inventario
            inventario[id_prod]["cantidad"] -= cantidad_pedida
            
            # Registrar el pedido
            pedidos[id_ped] = {
                "cliente": cliente,
                "id_producto": id_prod,
                "cantidad": cantidad_pedida
            }
            print("¡Pedido registrado y stock actualizado con éxito!")
        else:
            print(f"Error: Stock insuficiente. Solo hay {inventario[id_prod]['cantidad']} unidades disponibles.")
    except ValueError:
        print("Error: Ingrese un valor numérico para la cantidad.")

def mostrar_pedidos():
    """Función para mostrar todos los pedidos realizados."""
    print("\n--- LISTADO DE PEDIDOS ---")
    if not pedidos:
        print("No hay pedidos registrados.")
        return
    
    print(f"{'ID PEDIDO':<12} | {'CLIENTE':<20} | {'PRODUCTO (ID)':<15} | {'CANTIDAD'}")
    print("-" * 70)
    for id_ped, datos in pedidos.items():
        print(f"{id_ped:<12} | {datos['cliente']:<20} | {datos['id_producto']:<15} | {datos['cantidad']}")

def eliminar_pedido():
    """Procedimiento para eliminar un pedido (y devolver el stock)."""
    print(" ELIMINAR/CANCELAR PEDIDO")
    id_ped = input("Ingrese el ID del pedido a cancelar: ").strip().upper()
    
    if id_ped in pedidos:
        datos = pedidos[id_ped]
        id_prod = datos["id_producto"]
        
        # Devolver el stock al inventario (Escalabilidad y consistencia)
        if id_prod in inventario:
            inventario[id_prod]["cantidad"] += datos["cantidad"]
            
        del pedidos[id_ped]
        print("¡Pedido cancelado y stock devuelto con éxito!")
    else:
        print("Error: Pedido no encontrado.")


def menu_principal():
    """Ciclo principal del programa que gestiona las opciones del usuario."""
    while True:
        print("\n" + "="*40)
        print("   SISTEMA DE GESTIÓN (RETO 2)")
        print("="*40)
        print("1. Registrar un Producto")
        print("2. Mostrar Inventario")
        print("3. Editar un Producto")
        print("4. Eliminar un Producto")
        print("-" * 40)
        print("5. Registrar un Pedido")
        print("6. Mostrar Pedidos")
        print("7. Eliminar/Cancelar un Pedido")
        print("-" * 40)
        print("8. Salir")
        
        opcion = input("\nSeleccione una opción (1-8): ")
        
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            editar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            registrar_pedido()
        elif opcion == "6":
            mostrar_pedidos()
        elif opcion == "7":
            eliminar_pedido()
        elif opcion == "8":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Punto de entrada del programa
if __name__ == "__main__":
    menu_principal()