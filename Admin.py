from Persona import *
import matplotlib.pyplot as plt
from Validadores import *
from Pedidos import *
class Admin(Persona):
    def __init__(self, nombre, apellido,dni, mail, calle, altura, telefono, nombre_usuario, password):
        super().__init__(nombre, apellido, dni, mail, calle, altura, telefono)
        self.nombre_usuario = nombre_usuario
        self.password = password
    def __str__(self):
        return f"Admin: {self.nombre} {self.apellido}\nUsername: {self.nombre_usuario}"

    def crear_admin(self):
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

    def ver_estadisticas(self, tienda):
        print('1. Sabores más pedidos')
        print('2. Usuario que más gastó')
        opcion = input('Selccione una opción: ')

        while verificar_rango(opcion, 4) == False:
            opcion = int(input('Selccione una opción válida: '))
        if opcion == "1":
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
            plt.title(label="Grafico pedidos por sabor", fontsize=20, color="blue")
            plt.xlabel("Sabor")
            plt.ylabel('Cantidad de pedidos')
            plt.bar(sabores_pedidos, cantidad, color="green", width=0.5)
            plt.show()

    def ver_estadisticas(self, tienda):
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