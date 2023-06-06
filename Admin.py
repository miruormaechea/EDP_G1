from Persona import *
import matplotlib.pyplot as plt
from Pedido import *


class Admin(Persona):
    """
    Clase que representa a un administrador.
    Hereda de la clase Persona y agrega funcionalidades específicas para administradores.

    Atributos:
    - nombre_usuario (str): El nombre de usuario del administrador.
    - password (str): La contraseña del administrador.

    Métodos:
    - __init__(self, nombre, apellido, dni, mail, calle, altura, telefono, nombre_usuario, password): Inicializa una instancia de la clase Admin.
    - __str__(self): Devuelve una representación en cadena del administrador.
    - crear_admin(): Método estático para crear un nuevo administrador.
    - modificar_producto(self, producto): Permite al administrador modificar un producto existente o agregar uno nuevo.
    - ver_estadisticas(self, tienda): Muestra estadísticas de pedidos por sabor o por cobertura en forma de gráfico.
    """

    def __init__(self, nombre, apellido, dni, mail, calle, altura, telefono, nombre_usuario, password):
        """
        Inicializa una instancia de la clase Admin.
        Parámetros:
        - nombre (str): El nombre del administrador.
        - apellido (str): El apellido del administrador.
        - dni (str): El DNI del administrador.
        - mail (str): El correo electrónico del administrador.
        - calle (str): El nombre de la calle de residencia del administrador.
        - altura (str): La altura de la residencia del administrador.
        - telefono (str): El número de teléfono del administrador.
        - nombre_usuario (str): El nombre de usuario del administrador.
        - password (str): La contraseña del administrador.
        """
        super().__init__(nombre, apellido, dni, mail, calle, altura, telefono)
        self.nombre_usuario = nombre_usuario
        self.password = password

    def __str__(self):
        """
        Devuelve una representación en forma de cadena del objeto Admin.
        :return: La representación en forma de cadena del objeto Admin.
        """
        return f"Admin: {self.nombre} {self.apellido}\nUsername: {self.nombre_usuario}"

    @staticmethod
    def crear_admin():
        """
        Crea un objeto de la clase Admin a partir de la información ingresada por el usuario.
        :return: Un objeto Admin creado con los datos ingresados por el usuario.
        """
        nombre = input('Ingrese su nombre: ')
        while verNombre(nombre) == False:
            nombre = input("Por favor, ingrese un nombre válido: ")

        apellido = input('Ingrese su apellido: ')
        while verNombre(apellido) == False:
            apellido = input("Por favor, ingrese un apellido válido: ")

        dni = input('Ingrese su DNI: ')
        while verDNI(dni) == False:
            dni = input("Ingrese un DNI valido: ")

        mail = input('Ingrese su mail: ')
        while verMail(mail) == False:
            mail = input("Ingrese un email valido: ")

        calle = input('Ingrese su calle: ')
        while verNombre(calle) == False:
            calle = input("Ingrese una calle valída: ")

        altura = input('Ingrese su altura: ')
        while verAltura(altura) == False:
            altura = input("Ingrese una altura valída: ")

        telefono = input('Ingrese su telefono: ')
        while verTelefono(telefono) == False:
            telefono = input("Ingrese un teléfono valido: ")

        nombre_usuario = input('Ingrese un nombre de usuario: ')
        password = input('Ingrese una contraseña: ')

        return Admin(nombre, apellido, dni, mail, calle, altura, telefono, nombre_usuario, password)

    def modificar_producto(self, producto):
        """
        El admin Modifica un producto de la tienda.
        :param producto: El objeto Producto que se desea modificar.
        :return: None
        """
        diccionario_a_modificar = producto.ver_productos(modificar=True)
        key_a_modificar = "a"  # pasamos este parametro para entrar directamente al while
        while not verificar_rango(key_a_modificar, len(diccionario_a_modificar) + 1):
            key_a_modificar = input("Que tipo quiere modificar?")
        try:
            opcion_seleccionada = list(diccionario_a_modificar)[int(key_a_modificar) - 1]
        except IndexError:
            opcion_seleccionada = input("Que le gustaria agregar?")
        precio = input("Que precio le gustaria?")
        while not es_int(precio):
            print("Ingrese un numero por favor")
            precio = input("Que precio le gustaria?")
        diccionario_a_modificar[opcion_seleccionada] = int(precio)

    def ver_estadisticas(self, tienda):
        """
        Muestra estadísticas de pedidos en la tienda.
        :param tienda: El objeto Tienda del cual se obtendrán las estadísticas.
        :return: None
        """
        opcion = input(
            'Seleccione una opción:\n1. Cantidad de pedidos por sabor\n2. Cantidad de pedidos por cobertura ')
        while not es_int(opcion) or not verificar_rango(opcion, 2):
            opcion = input('Seleccione una opción válida: ')

        match int(opcion):
            case 1:
                contador_sabores = {}
                sabores = tienda.productos.sabor.keys()
                for sabor in sabores:
                    contador_sabores[sabor] = 0
                pedido: Pedido
                for pedido in tienda.pedidos:
                    sabor_pedido = pedido.carrito.get('sabor')[0]
                    contador_sabores[sabor_pedido] += 1
                sabores_pedidos = list(contador_sabores.keys())
                cantidad = list(contador_sabores.values())
                plt.title(label="Grafico sabor por pedidos", fontsize=20, color="black")
                plt.xlabel("Sabor")
                plt.ylabel('Cantidad de pedidos')
                plt.bar(sabores_pedidos, cantidad, color="green", width=0.5)
                plt.show()
            case 2:
                contador_coberturas = {}
                coberturas = tienda.productos.cobertura.keys()
                for cobertura in coberturas:
                    contador_coberturas[cobertura] = 0
                pedido: Pedido
                for pedido in tienda.pedidos:
                    cobertura_pedida = pedido.carrito.get('cobertura')[0]
                    contador_coberturas[cobertura_pedida] += 1
                sabores_pedidos = list(contador_coberturas.keys())
                cantidad = list(contador_coberturas.values())
                plt.title(label="Grafico coberturas por pedido", fontsize=20, color="black")
                plt.xlabel("Cobertura")
                plt.ylabel('Cantidad de pedidos')
                plt.bar(sabores_pedidos, cantidad, color="green", width=0.5)
                plt.show()
