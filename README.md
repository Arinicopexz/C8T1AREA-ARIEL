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




**1. Menú Principal y Registro de Productos**
![Registro de Productos]

**2. Visualización del Inventario**
![Inventario]

**3. Registro de Pedido (con descuento automático de stock)**
![Registro de Pedidos]
<img width="316" height="208" alt="image" src="https://github.com/user-attachments/assets/54da51f6-e8e9-4a40-b6d3-f81e293a583d" />
<img width="400" height="112" alt="image" src="https://github.com/user-attachments/assets/a9c8d48e-a2f3-4cb7-9673-6cbf1b45ea28" />
<img width="322" height="130" alt="image" src="https://github.com/user-attachments/assets/a2ba351b-0a70-4afa-8f7c-42b615a533e8" />

