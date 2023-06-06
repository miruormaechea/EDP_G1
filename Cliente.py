from Persona import *
from Pedido import *


class Cliente(Persona):
    """
    Clase que representa a un cliente de la tienda.

    Atributos:
    - nombre: El nombre del cliente.
    - apellido: El apellido del cliente.
    - dni: El DNI del cliente.
    - mail: El correo electrónico del cliente.
    - calle: La calle de residencia del cliente.
    - altura: La altura de residencia del cliente.
    - telefono: El número de teléfono del cliente.
    - nombre_usuario: El nombre de usuario del cliente.
    - password: La contraseña del cliente.
    - pedidos: Una lista de los pedidos realizados por el cliente.

    Métodos:
    - __init__(self, nombre, apellido, dni, mail, calle, altura, telefono, nombre_usuario, password): Constructor de la clase.
    - __str__(self): Devuelve una representación en forma de cadena del cliente.
    - crear_cliente(): Método estático para crear un nuevo cliente solicitando los datos al usuario.
    - repetir_pedido(self, n, tienda): Repite un pedido anterior del cliente en la tienda.
    - confirmar_pedido(self, pedido, tienda): Confirma un pedido realizado por el cliente en la tienda.
    - cambiar_info(self, opcion): Permite al cliente cambiar su información personal.
    - cambiar_contrasena(self): Permite al cliente cambiar su contraseña.


    """

    def __init__(self, nombre, apellido, dni, mail, calle, altura, telefono, nombre_usuario, password):
        """
        Inicializa un objeto Cliente.
        :param nombre: El nombre del cliente.
        :param apellido: El apellido del cliente.
        :param dni: El DNI del cliente.
        :param mail: El correo electrónico del cliente.
        :param calle: La calle del cliente.
        :param altura: La altura del cliente.
        :param telefono: El teléfono del cliente.
        :param nombre_usuario: El nombre de usuario del cliente.
        :param password: La contraseña del cliente.
        """
        super().__init__(nombre, apellido, dni, mail, calle, altura, telefono)
        self.nombre_usuario = nombre_usuario
        self.password = password
        self.pedidos = []

    def __str__(self):
        """
        Devuelve una representación en forma de cadena del cliente.
        :return: Cadena con la información del cliente.
        """
        return f"Cliente: {self.nombre} {self.apellido}\nDNI: {self.dni}\nEmail: {self.mail}\nDirección: {self.calle} {self.altura}\nTeléfono: {self.telefono}"

    @staticmethod
    def crear_cliente():
        """
        Crea un nuevo cliente solicitando los datos al usuario.
        :return: Un objeto Cliente con los datos ingresados por el usuario.
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

        return Cliente(nombre, apellido, dni, mail, calle, altura, telefono, nombre_usuario, password)

    def repetir_pedido(self, n, tienda):
        """
        Repite un pedido anterior del cliente en la tienda.
        :param n: El número del pedido a repetir.
        :param tienda: El objeto Tienda en el que se realizará el pedido.
        :return: None
        """
        pedido_anterior = self.pedidos[n - 1]
        pedido = Pedido(nombre_usuario=self, productos=tienda.productos)
        pedido.hacer_pedido(pedido_anterior)
        self.confirmar_pedido(pedido, tienda)

    def confirmar_pedido(self, pedido, tienda):
        """
        Confirma un pedido realizado por el cliente en la tienda.
        :param pedido: El objeto Pedido a confirmar.
        :param tienda: El objeto Tienda en el que se realizará el pedido.
        :return: None
        """
        opcion = input("Presione 1 si quiere confirmar su pedido, cualquier otra tecla en caso contrario")
        if opcion == "1":
            self.pedidos.append(pedido)
            print("Su pedido se ha confirmado con exito!")
            tienda.pedidos.append(pedido)
            generar_factura = input("Presione 1 si quiere generar una factura")
            if generar_factura == "1":
                # esto le da la opcion al cliente de generar un txt
                tienda.factura(self, pedido)
        else:
            pass

    def cambiar_info(self, opcion):
        """
        Permite al cliente cambiar su información personal.
        :param opcion: La opción seleccionada por el cliente.
        :return: None
        """
        match opcion:
            case "1":
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                while verNombre(nuevo_nombre) == False:
                    nuevo_nombre = input("Por favor, ingrese un nombre válido: ")
                    self.nombre = nuevo_nombre
                print("¡El nombre se ha actualizado correctamente!")
            case "2":
                nuevo_apellido = input("Ingrese el nuevo apellido: ")
                while verNombre(nuevo_apellido) == False:
                    nuevo_apellido = input("Por favor, ingrese un apellido válido: ")
                self.apellido = nuevo_apellido
                print("¡El apellido se ha actualizado correctamente!")
            case "3":
                nuevo_dni = input("Ingrese el nuevo DNI: ")
                while verDNI(nuevo_dni) == False:
                    nuevo_dni = input("Ingrese un DNI valido: ")
                self.dni = nuevo_dni
                print("¡El DNI se ha actualizado correctamente!")
            case "4":
                nuevo_mail = input("Ingrese el nuevo mail: ")
                while verMail(nuevo_mail) == False:
                    nuevo_mail = input("Ingrese un email valido: ")
                self.mail = nuevo_mail
                print("¡El mail se ha actualizado correctamente!")
            case "5":
                nueva_calle = input("Ingrese la nueva calle: ")
                while verNombre(nueva_calle) == False:
                    nueva_calle = input("Ingrese una calle valída: ")
                self.calle = nueva_calle
                print("¡La calle se ha actualizado correctamente!")

            case "6":
                nueva_altura = input("Ingrese la nueva altura: ")
                while verAltura(nueva_altura) == False:
                    nueva_altura = input("Ingrese una altura valída: ")
                self.altura = nueva_altura
                print("¡La altura se ha actualizado correctamente!")

            case "7":
                nuevo_telefono = input("Ingrese el nuevo teléfono: ")
                while verTelefono(nuevo_telefono) == False:
                    nuevo_telefono = input("Ingrese un teléfono valido: ")
                self.telefono = nuevo_telefono
                print("¡El teléfono se ha actualizado correctamente!")

    def cambiar_contrasena(self):
        """
        Permite al cliente cambiar su contraseña.
        :return: None
        """
        contrasena_actual = input("Ingrese su contraseña actual: ")
        if contrasena_actual != self.password:
            print("Contraseña incorrecta. No se puede cambiar la contraseña.")
            return

        nueva_contrasena = input("Ingrese su nueva contraseña: ")
        confirmar_contrasena = input("Confirme su nueva contraseña: ")

        if nueva_contrasena != confirmar_contrasena:
            print("Las contraseñas no coinciden. No se puede cambiar la contraseña.")
            return

        self.password = nueva_contrasena
        print("¡La contraseña se ha cambiado exitosamente!")
