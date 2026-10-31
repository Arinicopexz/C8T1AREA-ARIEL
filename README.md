# Sistema de Gestión de Pedidos e Inventario (Reto 2)

Este proyecto es un sistema básico, modular y escalable desarrollado en Python para gestionar el inventario de productos y los pedidos de clientes mediante operaciones CRUD (Crear, Leer, Actualizar, Eliminar).

## Características y Funcionalidades
El código está organizado en funciones y procedimientos específicos para mantener la modularidad y facilitar su escalabilidad:

### Gestión de Inventario
- `registrar_producto()`: Añade nuevos productos al sistema verificando que el ID no esté duplicado.
- `mostrar_inventario()`: Imprime una tabla formateada con el stock actual.
- `editar_producto()`: Permite actualizar el stock y el precio de un producto existente.
- `eliminar_producto()`: Borra permanentemente un producto de la base de datos temporal (diccionario).

### Gestión de Pedidos
- `registrar_pedido()`: Crea un pedido, validando previamente que el producto exista y que haya **stock suficiente**. Si es exitoso, descuenta automáticamente la cantidad del inventario.
- `mostrar_pedidos()`: Muestra el registro histórico de las ventas.
- `eliminar_pedido()`: Cancela un pedido y, para mantener la consistencia de los datos, devuelve las unidades canceladas al inventario original.

## Principios de Programación Aplicados
1. **Modularidad:** Separación estricta de la lógica en funciones y un bucle principal `menu_principal()`.
2. **Estructuras de Datos:** Uso de diccionarios anidados (`{}`), lo que permite búsquedas instantáneas por ID ($O(1)$) en lugar de recorrer listas enteras, mejorando drásticamente el rendimiento.
3. **Escalabilidad:** El sistema previene caídas mediante bloques `try-except` para evitar errores de tipeo del usuario al ingresar números (validación de entradas).

## Evidencias de Ejecución (Capturas de Pantalla)

*(Nota: Reemplaza las rutas de abajo subiendo tus propias capturas de pantalla a la carpeta de tu repositorio)*

**1. Menú Principal y Registro de Productos**
![Registro de Productos]

**2. Visualización del Inventario**
![Inventario]

**3. Registro de Pedido (con descuento automático de stock)**
![Registro de Pedidos]