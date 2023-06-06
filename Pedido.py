from Producto import *
from datetime import datetime
from Validadores import *


class Pedido():
    """
    Representa un pedido de cupcakes realizado por un usuario.

    Atributos:
    - nombre_usuario (str): El nombre de usuario del cliente que realiza el pedido.
    - productos (Producto): El objeto de productos disponibles en la tienda.
    - total (float): El total del pedido.
    - carrito (dict): El diccionario que contiene los productos seleccionados en el pedido.
    - fecha (datetime): La fecha y hora en que se realizó el pedido.

    Métodos:
    - __init__(self, nombre_usuario, productos: Producto): Inicializa una instancia de la clase Pedido.
    - __str__(self): Devuelve una representación en cadena del pedido.
    - hacer_pedido(self, pedido_anterior=None): Permite al usuario realizar un pedido de cupcakes.
    - seleccionar(tipo: str, categoria): Permite al usuario seleccionar una opción de un tipo específico de producto.
    """

    def __init__(self, nombre_usuario, productos: Producto):
        """
        Inicializa una instancia de la clase Pedido.
        :param nombre_usuario: El nombre de usuario del cliente que realiza el pedido.
        :type nombre_usuario: str
        :param productos: El objeto de productos disponibles en la tienda.
        :type productos: Producto
        """
        self.nombre_usuario = nombre_usuario
        self.productos = productos
        self.total = 0
        self.carrito = dict()
        self.fecha = datetime.now()

    def __str__(self):
        """
        Devuelve una representación en cadena del pedido.
        :return: Una representación en cadena del pedido.
        :rtype: str
        """
        return f"Pedido de {self.nombre_usuario.nombre} \nTotal: ${self.total} \nDetalles del pedido: Cupcake/s Sabor: {self.carrito['sabor'][0]} - Relleno: {self.carrito['relleno'][0]} - Cobertura: {self.carrito['cobertura'][0]} - Sprinkle: {self.carrito['sprinkle'][0]} "

    def hacer_pedido(self, pedido_anterior=None):
        """
        Permite al usuario realizar un pedido de cupcakes.
        :param pedido_anterior: Un pedido anterior del usuario (opcional).
        :type pedido_anterior: Pedido, optional
        :return: None
        """

        def seleccionar(tipo: str, categoria):
            """
            Permite al usuario seleccionar una opción de un tipo específico de producto.
            :param tipo: El tipo de producto a seleccionar (sabor, relleno, cobertura, sprinkle).
            :type tipo: str
            :param categoria: El código de categoría del producto.
            :type categoria: int
            :return: La opción seleccionada por el usuario.
            :rtype: str
            """
            dict_tipo = self.productos.ver_productos(categoria)
            n = input(
                f"Ingrese el número de {tipo} que quiera:  ")
            while verificar_rango(n, len(dict_tipo)) == False:
                n = input(
                    "Ingrese un número valido de sabor que quiera:  ")
            return list(dict_tipo)[int(n) - 1]

        total = 0
        while True:
            sabor_seleccionado = seleccionar("sabor", 1) if not pedido_anterior else \
            pedido_anterior.carrito.get("sabor")[0]
            relleno_seleccionado = seleccionar("relleno", 2) if not pedido_anterior else \
            pedido_anterior.carrito.get("relleno")[0]
            cobertura_seleccionada = seleccionar("cobertura", 3) if not pedido_anterior else \
            pedido_anterior.carrito.get("cobertura")[0]
            sprinkle_seleccionada = seleccionar("sprinkle", 4) if not pedido_anterior else \
            pedido_anterior.carrito.get("sprinkle")[0]

            cantidad = input("¿Cuantos cupcakes quiere?: ")
            validado = False
            while not validado:
                while not es_int(cantidad):
                    cantidad = input("Ingrese una cantidad valida de cupcakes: ")
                if int(cantidad) > 100:
                    print("El numero maximo de cupcakes por pedido es 100")
                    cantidad = "not int"
                elif int(cantidad) < 1:
                    print("El numero minimo de cupcakes por pedido es 1")
                    cantidad = "not int"
                else:
                    validado = True
            total += self.productos.sabor[sabor_seleccionado] * int(cantidad)
            total += self.productos.relleno[relleno_seleccionado] * int(cantidad)
            total += self.productos.cobertura[cobertura_seleccionada] * int(cantidad)
            total += self.productos.sprinkle[sprinkle_seleccionada] * int(cantidad)
            self.total = total

            self.carrito["sabor"] = (sabor_seleccionado, self.productos.sabor[sabor_seleccionado])
            self.carrito["relleno"] = (relleno_seleccionado, self.productos.relleno[relleno_seleccionado])
            self.carrito["cobertura"] = (cobertura_seleccionada, self.productos.cobertura[cobertura_seleccionada])
            self.carrito["sprinkle"] = (sprinkle_seleccionada, self.productos.sprinkle[sprinkle_seleccionada])
            break

        print(f"Su pedido ha sido registrado con éxito. Total a pagar: ${total}")
