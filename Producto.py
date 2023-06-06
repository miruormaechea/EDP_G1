from Validadores import *


class Producto:
    """
    Representa los productos disponibles en la tienda de cupcakes.

    Atributos:
    - sabor (dict): Un diccionario que contiene los sabores de cupcakes disponibles y sus precios.
    - relleno (dict): Un diccionario que contiene los tipos de relleno disponibles y sus precios.
    - cobertura (dict): Un diccionario que contiene las opciones de cobertura disponibles y sus precios.
    - sprinkle (dict): Un diccionario que contiene las opciones de sprinkle disponibles y sus precios.

    Métodos:
    - __init__(self): Inicializa una instancia de la clase Producto.
    - __str__(self): Devuelve una representación en cadena de los productos.
    - ver_productos(self, opcion=None, modificar=False): Muestra los productos disponibles en la tienda.
    """

    def __init__(self):
        """
        Inicializa una instancia de la clase Producto.
        Lo inicizaliza en tipo diccionario
        """
        self.sabor = {
            "Chocolate": 100,
            "Vainilla": 200,
            "Frutilla": 400,
            "Zanahoria": 5000
        }
        self.relleno = {
            "Sin relleno": 0,
            "Dulce de leche": 400,
            "Crema Pastelera": 300,
            "Batata": 400,
            "Membrillo": 300
        }
        self.cobertura = {
            "Sin cobertura": 0,
            "Chocolate": 100,
            "Crema": 30
        }
        self.sprinkle = {
            "Sin sprinkles": 0,
            "Chocolate": 400,
            "Multicolor": 200
        }

    def __str__(self):
        """
        Devuelve una representación en cadena de los productos.
        :return: Una representación en cadena de los productos.
        :rtype: str
        """
        return f"Producto\nSabor: {self.sabor}\nRelleno: {self.relleno}\nCobertura: {self.cobertura}\nSprinkle: {self.sprinkle}"

    def ver_productos(self, opcion=None, modificar=False):
        """
        Muestra los productos disponibles en la tienda.
        :param opcion: La opción seleccionada por el usuario (opcional).
        :type opcion: int, optional
        :param modificar: Indica si se está realizando una modificación de productos (opcional).
        :type modificar: bool, optional
        :return: El diccionario correspondiente a la opción seleccionada.
        :rtype: dict
        """
        if opcion == None:
            opcion = input("Seleccione una opcion: \n 1.Sabores \n 2.Rellenos \n 3.Coberturas \n 4.Sprinkles\n")
            while not verificar_rango(opcion, 4):
                opcion = input(
                    "Seleccione una opcion valida: \n 1.Sabores \n 2.Rellenos \n 3.Coberturas \n 4.Sprinkles\n")

        def mostrar(productos, tipo):
            """
            Muestra los productos de un tipo específico.
            :param productos: El diccionario de productos de un tipo específico.
            :type productos: dict
            :param tipo: El tipo de producto.
            :type tipo: str
            """
            cont = 0
            print(f"{tipo} disponibles:")
            for tipo_de_parte, precio in productos.items():
                cont += 1
                print(f"{cont} {tipo_de_parte} - ${precio}")
            if modificar:
                cont += 1
                print(f"{cont} agregar uno")

        match int(opcion):
            case 1:
                mostrar(self.sabor, "Sabores")
                return self.sabor
            case 2:
                mostrar(self.relleno, "Rellenos")
                return self.relleno
            case 3:
                mostrar(self.cobertura, "Coberturas")
                return self.cobertura
            case 4:
                mostrar(self.sprinkle, "Sprinkles")
                return self.sprinkle
