import os
import csv
from Validadores import *
from datetime import datetime
from time import sleep


class Cliente():
    def __init__(self, nombre, apellido, dni, mail, calle, altura, telefono, nombre_usuario, password):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.mail = mail
        self.calle = calle
        self.altura = altura
        self.telefono = telefono
        self.nombre_usuario = nombre_usuario
        self.password = password


def crear_cliente():
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


class Pedido():
    def __init__(self, nombre_usuario, productos, total):
        self.nombre_usuario = nombre_usuario
        self.productos = productos
        self.total = total
        self.escribir_archivo()

    def __str__(self):
        return f"Pedido de {self.nombre_usuario} - Total: ${self.total} \nDetalles del pedido: {self.productos[4]} Cupcake/s Sabor: {self.productos[0]} - Relleno: {self.productos[1]} - Cobertura: {self.productos[2]} - Sprinkle: {self.productos[3]}"

    def escribir_archivo(self):
        with open('pedidos.csv', mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(
                [datetime.now(), self.nombre_usuario, self.productos[4], self.productos[0], self.productos[1],
                 self.productos[2], self.productos[3],
                 self.total])


class Tienda():
    lista_pedidos = []

    def __init__(self):

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
        self.pedido = []

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
                cont = 0
                print("Sabores disponibles:")
                for sabor,precio in self.sabor.items():
                    cont+=1
                    print(f"{cont} {sabor} - ${precio}")
            case 2:
                cont = 0
                print("Rellenos disponibles:")
                for relleno,precio in self.relleno.items():
                    cont += 1
                    print(f"{cont} {relleno} - ${precio}")
            case 3:
                cont = 0
                print("Coberturas disponibles:")
                for cobertura,precio in self.cobertura.items():
                    cont += 1
                    print(f"{cont} {cobertura} - ${precio}")
            case 4:
                print("Sprinkles disponibles:")
                cont = 0
                for sprinkle,precio in self.sprinkle.items():
                    cont+=1
                    print(f"{cont} {sprinkle} - ${precio}")

    def hacer_pedido(self, usuario_pedido, pedido_anterior=None):
        os.system('cls' if os.name == 'nt' else 'clear')
        carrito = []
        total = 0
        if pedido_anterior != None:

            cantidad = input("¿Cuantos cupcakes quiere?: ")
            validado = False
            while validado == False:
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

            total += self.sabor[pedido_anterior[0]] * int(cantidad)
            carrito.append(pedido_anterior[0])
            total += self.relleno[pedido_anterior[1]] * int(cantidad)
            carrito.append(pedido_anterior[1])
            total += self.cobertura[pedido_anterior[2]] * int(cantidad)
            carrito.append(pedido_anterior[2])
            total += self.sprinkle[pedido_anterior[3]] * int(cantidad)
            carrito.append(pedido_anterior[3])
            carrito.append(cantidad)



        elif pedido_anterior == None:
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
                    n_cobertura = (input(
                        "Ingrese un número valido de cobertura que quiera:  "))

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
                    elif int(cantidad) < 1:
                        print("El numero minimo de cupcakes por pedido es 1")
                        cantidad = "not int"
                    else:
                        validado = True

                total += self.sabor[list(self.sabor)[int(n_sabor)-1]] * int(cantidad)
                carrito.append(list(self.sabor)[int(n_sabor)-1])
                total += self.relleno[list(self.relleno)[int(n_relleno)-1]] * int(cantidad)
                carrito.append(list(self.relleno)[int(n_relleno)-1])
                total += self.cobertura[list(self.cobertura)[int(n_cobertura)-1]] * int(cantidad)
                carrito.append(list(self.cobertura)[int(n_cobertura)-1])
                total += self.sprinkle[list(self.sprinkle)[int(n_sprinkle)-1]] * int(cantidad)
                carrito.append(list(self.sprinkle)[int(n_sprinkle)-1])
                carrito.append(cantidad)
                break

        print(f"Su pedido ha sido registrado con éxito. Total a pagar: ${total}")
        confirmacion = input("Ingrese 1 para confirmar su pedido, cualquier otra tecla para cancelar: ")
        if confirmacion != "1":
            print("Su pedido ha sido cancelado.")
            input("Presione Enter para volver al menú principal")
        elif confirmacion == "1":
            pedido = Pedido(usuario_pedido, carrito, total)
            Tienda.lista_pedidos.append(pedido)
            print(f"Su pedido ha sido confirmado")
            input("Presione Enter para volver al menú principal")

    def ver_pedidos(self, usuario):

        os.system('cls' if os.name == 'nt' else 'clear')
        with open('pedidos.csv', mode='r') as csv_file:
            existe = False
            reader = csv.reader(csv_file)
            pedidos_usuario = []
            i = 0
            for row in (reader):
                if row[1] == usuario:
                    existe = True
                    i += 1
                    print(
                        f'{i} Fecha: {row[0]} - Total: ${row[7]}- {row[2]} Cupcake/s Sabor: {row[3]} - Relleno: {row[4]} -'
                        f' Cobertura: {row[5]} - Sprinkle: {row[6]}\n ')
                    pedidos_usuario.append(row)
            if existe == False:
                print(f'Disculpa {usuario} no realizaste ningun pedido todavia')
            repetir = input(
                "Presione 1 si desea volver a pedir uno de sus pedidos, cualquier otra letra en caso contrario:")
            if repetir != "1":
                input("Presione Enter para volver al menú principal")
            elif repetir == "1":
                pedido = input("Ingrese el numero de pedido que quiere repetir: ")
                while not es_int(pedido):
                    pedido = input("Ingrese un numero valido de pedido: ")
                existe = False
                for i, row in enumerate(pedidos_usuario):
                    if i == int(pedido) - 1:
                        existe = True
                        datos_pedido = [row[3], row[4], row[5], row[6]]
                        # Estoy pasando los datos en orden, Sabor, Relleno, Cobertura, Sprinkle
                        self.hacer_pedido(usuario, datos_pedido)
                if existe == False:
                    print("No ingreso un numero valido de pedido")
                    sleep(2)

    def iniciar(self):
        inicio = False
        opcion = 0
        users_file = "C:/Users/ormae/OneDrive/Documents/usuarios.txt"
        while inicio != True:
            opcion = input("Seleccione una opcion:\n1.Iniciar sesion\n2.Crear cuenta\n")

            if opcion == "1":
                usuario_login = input("Ingrese su Usuario: ")
                password_login = input("Ingrese su contrasena: ")
                cont_login = 0
                with open(users_file, 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        if ':' in line:
                            user, pw = line.strip().split(":")
                            if user == usuario_login and pw == password_login:
                                print("Login exitoso!")
                                cont_login = 1
                                inicio = True
                                break
                    if cont_login != 1:
                        print("Usuario o Contrasena incorrectos.")



            elif opcion == "2":
                cliente_nuevo = crear_cliente()

                with open(users_file, "r+") as f:
                    for line in f:
                        if ':' in line:
                            user, pw = line.strip().split(":")
                            if user == cliente_nuevo.nombre_usuario:
                                print("El usuario ya existe.")
                                break
                            else:
                                with open('users.csv', mode='a', newline='') as csv_file:
                                    writer = csv.writer(csv_file)
                                    writer.writerow(
                                        [cliente_nuevo.nombre_usuario, cliente_nuevo.dni, cliente_nuevo.nombre,
                                         cliente_nuevo.apellido, cliente_nuevo.calle, cliente_nuevo.altura,
                                         cliente_nuevo.mail, cliente_nuevo.telefono])

                                f.write(f"{cliente_nuevo.nombre_usuario}:{cliente_nuevo.password}\n")
                                Tienda.lista_clientes.append(cliente_nuevo)
                                print("Usuario creado exitosamente.")

        while True and inicio == True:
            self.menu()
            opcion = input("Seleccione una opción: ")
            if opcion == "1":  # opcion ver productos
                self.ver_productos()
                input("Presione Enter para volver al menu principal.")
            elif opcion == "2":  # opcion hacer pedido
                self.hacer_pedido(usuario_login)
            elif opcion == "3":  # opcion ver pedidos
                self.ver_pedidos(usuario_login)
            elif opcion == "4":  # opcion salir
                print("Gracias por visitar la tienda de cupcakes online!")
                break
            else:
                print("Opción inválida. Por favor ingrese un número del 1 al 4.")
                input("Presione Enter para continuar")


Blue_Velvet_Cupcakes = Tienda()
Blue_Velvet_Cupcakes.iniciar()
