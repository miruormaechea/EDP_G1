import os
import csv
from Verificadores import *


class Cliente:
    def __init__(self, dni, nombre, apellido, calle, altura, email, telefono):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.calle = calle
        self.altura = altura
        self.email = email
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} {self.apellido}, {self.email}"


class Producto:
    # esto por ahora no tiene sentido. Ergo, podria estar mergeado con cupcake (pues solo vendemos cupcakes)
    # pero la dejo porque nos deja usar herencia con cupcakes y ademas tal vez en un futuro vendemos tortas o galletitas
    def __init__(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    def __str__(self):
        return f"{self.nombre}: {self.descripcion} - ${self.precio}"


class Cupcake(Producto):
    def __init__(self, nombre, descripcion, precio, sabor, relleno, cobertura, sprinkle):
        super().__init__(nombre, descripcion, precio)
        self.sabor = sabor
        self.relleno = relleno
        self.cobertura = cobertura
        self.sprinkle = sprinkle

    def __str__(self):
        return f"{super().__str__()} - Sabor: {self.sabor}"


class Pedido:
    def __init__(self, cliente, productos, total):
        self.cliente = cliente
        self.productos = productos
        self.total = total
        self.escribir_archivo(cliente)

    def __str__(self):
        return f"Pedido de {self.cliente} - Total: ${self.total} \nDetalles del pedido: {self.productos[4]} Cupcake/s Sabor: {self.productos[0]} " \
               f"- Relleno: {self.productos[1]} - Cobertura: {self.productos[2]} - Sprinkle: {self.productos[3]}"

    def escribir_archivo(self, usuario):
        with open('pedidos.csv', mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([usuario, self.productos[0], self.productos[1], self.productos[2], self.productos[3],
                             self.total]
                            )


class Tienda:
    def __init__(self, usuarios):
        self.usuarios = usuarios
        self.sabor = [
            ("Chocolate", 100),
            ("Vainilla", 200),
            ("Frutilla", 400),
            ("Zanahoria", 5000)
        ]
        self.relleno = [
            ("Sin relleno", 0),
            ("Dulce de leche", 400),
            ("Crema Pastelera", 300),
            ("Batata", 400),
            ("Membrillo", 300)
        ]
        self.cobertura = [
            ("Sin cobertura", 0),
            ("Chocolate", 100),
            ("Crema", 30)
        ]
        self.sprinkle = [
            ("Sin sprinkles", 0),
            ("Chocolate", 400),
            ("Multicolor", 200)
        ]
        self.pedidos = []

    def menu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Bienvenido a la tienda de cupcakes online!")
        print("1. Ver productos")
        print("2. Hacer pedido")
        print("3. Ver pedidos")
        print("4. Salir")

    def ver_productos(self, opcion=None):
        os.system('cls' if os.name == 'nt' else 'clear')
        if opcion == None:
            opcion = input("Seleccione una opcion: \n 1.Sabores \n 2.Rellenos \n 3.Coberturas \n 4.Sprinkles\n")
            while not verificar_rango(opcion, 4):
                opcion = input(
                    "Seleccione una opcion valida: \n 1.Sabores \n 2.Rellenos \n 3.Coberturas \n 4.Sprinkles\n")
        match int(opcion):
            case 1:
                print("Sabores disponibles:")
                for i, sabor in enumerate(self.sabor):
                    print(f"{i + 1}. {sabor[0]} - ${sabor[1]}")
            case 2:
                print("Rellenos disponibles:")
                for i, relleno in enumerate(self.relleno):
                    print(f"{i + 1}. {relleno[0]} - ${relleno[1]}")
            case 3:
                print("Coberturas disponibles:")
                for i, cobertura in enumerate(self.cobertura):
                    print(f"{i + 1}. {cobertura[0]} - ${cobertura[1]}")
            case 4:
                print("Sprinkles disponibles:")
                for i, sprinkle in enumerate(self.sprinkle):
                    print(f"{i + 1}. {sprinkle[0]} - ${sprinkle[1]}")

    def hacer_pedido(self, usuario):
        os.system('cls' if os.name == 'nt' else 'clear')
        carrito = []
        total = 0
        while True:
            self.ver_productos(1)
            n_sabor = input(
                "Ingrese el número de sabor que quiera:  ")
            while verificar_rango(n_sabor, 4) == False:
                n_sabor = input(
                    "Ingrese un número valido de sabor que quiera:  ")

            self.ver_productos(2)
            n_relleno = input(
                "Ingrese el número de relleno que quiera:  ")
            while not verificar_rango(n_relleno, 5):
                n_relleno = input(
                    "Ingrese un número valido de relleno que quiera:  ")

            self.ver_productos(3)
            n_cobertura = input(
                "Ingrese el número de cobertura que quiera:  ")
            while verificar_rango(n_cobertura, 3) == False:
                n_cobertura = input(
                    "Ingrese un número valido de cobertura que quiera:  ")
            self.ver_productos(4)
            n_sprinkle = input(
                "Ingrese el número de sprinkle que quiera:  ")
            while verificar_rango(n_sprinkle, 3) == False:
                n_sprinkle = input(
                    "Ingrese un número valido de sprinkle que quiera:  ")

            cantidad = input("¿Cuantos cupcakes quiere?: ")
            validado = False
            while validado == False:
                while not es_int(cantidad):
                    cantidad = input("Ingrese una cantidad valida de cupcakes: ")
                if int(cantidad) > 100:
                    print("El numero maximo de cupcakes por pedido es 100")
                    cantidad = "not int"
                else:
                    validado = True

            total += self.sabor[int(n_sabor) - 1][1] * int(cantidad)
            carrito.append(self.sabor[int(n_sabor) - 1][0])
            total += self.relleno[int(n_relleno) - 1][1] * int(cantidad)
            carrito.append(self.relleno[int(n_relleno) - 1][0])
            total += self.cobertura[int(n_cobertura) - 1][1] * int(cantidad)
            carrito.append(self.cobertura[int(n_cobertura) - 1][0])
            total += self.sprinkle[int(n_sprinkle) - 1][1] * int(cantidad)
            carrito.append(self.sprinkle[int(n_sprinkle) - 1][0])
            carrito.append(cantidad)
            break
        pedido = Pedido(usuario, carrito, total)
        self.pedidos.append(pedido)
        print(f"Su pedido ha sido registrado con éxito. Total a pagar: ${total}")
        input("Presione Enter para volver al menú principal")


    def ver_pedidos(self, usuario_ver_pedidos):
        os.system('cls' if os.name == 'nt' else 'clear')
        with open('pedidos.csv', mode='r') as csv_file:
            reader = csv.reader(csv_file)
            i = 0
            for row in (reader):
                print(usuario_ver_pedidos)
                if row[0] == usuario_ver_pedidos:
                    i += 1
                    print(
                        f'{i} Fecha: {row[0]} - Total: ${row[7]}- {row[2]} Cupcake/s Sabor: {row[3]} - Relleno: {row[4]} - Cobertura: {row[5]} - Sprinkle: {row[6]}\n ')
        input("Presione Enter para volver al menú principal")


    def iniciar(self):
        inicio = False
        usuario = None
        opcion = 0
        users_file = "C:/Users/ormae/OneDrive/Documents/usuarios.txt"
        while inicio != True:
            opcion = input("Seleccione una opcion:\n1.Iniciar sesion\n2.Crear cuenta\n")

            if opcion == "1":
                usuario = input("Ingrese su Usuario: ")
                password = input("Ingrese su contrasena: ")
                with open(users_file, "r") as f:
                    for line in f:
                        user, pw = line.strip().split(":")
                        if user == usuario and pw == password:
                            print("Login exitoso!")
                            inicio = True
                            break
                    else:
                        print("Usuario o Contrasena incorrectos.")

            elif opcion == "2":
                dni = input("Ingrese su DNI: ")
                while verDNI(dni) == False:
                    dni = input("Ingrese un DNI valido: ")
                nombre = input("Ingrese su nombre: ")

                while verNombre(nombre) == False:
                    nombre = input("Por favor, ingrese un nombre válido: ")
                apellido = input("Ingrese su apellido: ")
                while verNombre(apellido) == False:
                    apellido = input("Por favor, ingrese un apellido válido: ")
                calle = input("Ingrese la calle en donde vive: ")
                while verNombre(calle) == False:
                    calle = input("Ingrese una calle valída")
                altura = input("Ingrese la altura de su vivienda: ")
                while verAltura(altura) == False:
                    altura = input("Ingrese una altura valída")
                email = input("Ingrese su email: ")
                while verMail(email) == False:
                    email = input("Ingrese un email valido: ")
                telefono = input("Ingrese su teléfono: ")
                while verTelefono(telefono) == False:
                    telefono = input("Ingrese un teléfono valido: ")
                usuario = input("Ingrese un nombre de usuario: ")
                password = input("Ingrese una contraseña: ")
                with open('users.csv', mode='a', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(
                        [usuario, dni, nombre, apellido, calle, altura, email, telefono])
                with open(users_file, "r+") as f:
                    for line in f:
                        user, pw = line.strip().split(":")
                        if user == usuario:
                            print("El usuario ya existe.")
                            break
                    else:
                        f.write(f"\n{usuario}:{password}")
                        print("Usuario creado exitosamente.")

        while True and inicio == True:
            self.menu()
            opcion = input("Seleccione una opción: ")
            if opcion == "1":  # opcion ver productos
                self.ver_productos()
                input("Presione Enter para volver al menu principal.")
            elif opcion == "2":  # opcion hacer pedido
                self.hacer_pedido(usuario)
            elif opcion == "3":  # opcion ver pedidos
                self.ver_pedidos(usuario)
            elif opcion == "4":  # opcion salir
                print("Gracias por visitar la tienda de cupcakes online!")
                break

            else:
                print("Opción inválida. Por favor ingrese un número del 1 al 4.")
                input("Presione Enter para continuar")


Blue_Velvet_Cupcakes = Tienda([])
Blue_Velvet_Cupcakes.iniciar()
