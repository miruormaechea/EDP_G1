import os  # esta libreria es la que usamos para limpiar la pantalla
import csv  # esta libreria es para las hojas de calculo
from Funciones import *  # este import nos trae la parte del codigo con todos los validadores
from datetime import datetime  # la usamos para las fechas
from time import sleep  # la usamos como "cooldown" de pantalla
import pickle
import re




class Persona():
    def __init__(self, nombre, apellido, nombre_usuario, password):
        self.nombre = nombre
        self.apellido = apellido
        self.nombre_usuario = nombre_usuario
        self.password = password

    def __str__(self):
        return f"Persona: {self.nombre} {self.apellido} Username: {self.nombre_usuario}"



class Cliente(Persona):
    def __init__(self, nombre, apellido, dni, mail, calle, altura, telefono, nombre_usuario, password):
        super().__init__(nombre, apellido, nombre_usuario, password)
        self.dni = dni
        self.mail = mail
        self.calle = calle
        self.altura = altura
        self.telefono = telefono
        self.nombre_usuario = nombre_usuario
        self.password = password
        self.pedidos = []

    @staticmethod
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

    def cambiar_contrasena(self):
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

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nDNI: {self.dni}\nEmail: {self.mail}\nDirección: {self.calle} {self.altura}\nTeléfono: {self.telefono}"

    def factura(self,pedido):
        timestamp = re.sub(r'[^a-zA-Z0-9]', '_', str(datetime.now()))
        archivo_factura = f"C:/Users/ormae/OneDrive/Documents/factura_{self.nombre}_{timestamp}.txt"
        with open(archivo_factura, "w") as archivo:
            # Write data to the file
            archivo.write(str(pedido))

    #esto le da la opcion al cliente de generar un txt
    def menu(self, tienda):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Bienvenido a la tienda de cupcakes online!")
            print("1. Ver productos")
            print("2. Hacer pedido")
            print("3. Ver pedidos")
            print("4. Cambiar contraseña")
            print("5. Cerrar Sesion")
            opcion = "a"
            while not verificar_rango(opcion, 5):
                opcion = input("Elija una opcion: ")
            match opcion:
                case "1":
                    tienda.productos.ver_productos()
                case "2":
                    nuevo_pedido = Pedido(nombre_usuario=self, productos= tienda.productos)
                    nuevo_pedido.hacer_pedido()
                    opcion = input("Presione 1 si quiere confirmar su pedido, cualquier otra tecla en caso contrario")
                    if opcion == "1":
                        self.pedidos.append(nuevo_pedido)
                        print("Su pedido se ha confirmado con exito!")
                        Tienda.lista_pedidos.append(nuevo_pedido)
                        generar_factura = input("Presione 1 si quiere generar una factura")
                        if generar_factura == "1":
                          self.factura(nuevo_pedido)
                    else:
                        pass

                case "3":
                    for i,pedido in enumerate(self.pedidos):
                        print(i+1,pedido)
                        input("Presione enter para continuar")



                case "4":
                    self.cambiar_contrasena()
                case "5":
                    break

class Invitado(Cliente): #ya esta creada la clase, falta la implementacion
    def __init__(self, nombre, apellido, dni, mail, calle, altura, telefono, nombre_usuario):
        super().__init__(nombre, apellido, dni, mail, calle, altura, telefono, nombre_usuario, None)
        self.login_count = 0

    def menu(self, tienda):
        self.login_count += 1  # Increment the login count
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Bienvenido a la tienda de cupcakes online!")
            print("1. Ver productos")
            print("2. Salir")
            opcion = "a"
            while not verificar_rango(opcion, 2):
                opcion = input("Elija una opción: ")
            match opcion:
                case "1":
                    tienda.productos.ver_productos()
                case "2":
                    break


class Admin(Persona):
    def __init__(self, nombre, apellido, username, password):
        super().__init__(nombre, apellido, username, password)

    def __str__(self):
        return f"Admin: {self.nombre} {self.apellido}\nUsername: {self.nombre_usuario}"


    def menu(self, tienda):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Bienvenido administrador!")
            print("1. Ver productos actuales")
            print("2. Ver estadisticas")
            print("3. Editar productos")
            print("4. Cerrar Sesion")
            opcion = "a"
            while not verificar_rango(opcion, 4):
                opcion = input("Elija una opcion: ")
            match opcion:
                case "1":
                    tienda.productos.ver_productos()
                case "2":
                    pass
                case "3":
                    tienda.productos.modificar_producto()
                case "4":
                    break



class Producto():
    def __init__(self):
        # aca los guardo como diccionario
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
        return f"Producto\nSabor: {self.sabor}\nRelleno: {self.relleno}\nCobertura: {self.cobertura}\nSprinkle: {self.sprinkle}"

    def ver_productos(self, opcion=None, modificar = False):
        os.system('cls' if os.name == 'nt' else 'clear')
        if opcion == None:
            opcion = input("Seleccione una opcion: \n 1.Sabores \n 2.Rellenos \n 3.Coberturas \n 4.Sprinkles\n")
            while not verificar_rango(opcion, 4):
                opcion = input(
                    "Seleccione una opcion valida: \n 1.Sabores \n 2.Rellenos \n 3.Coberturas \n 4.Sprinkles\n")

        producto = self
        def mostrar(productos, tipo):
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

    def modificar_producto(self):
        diccionario_a_modificar = self.ver_productos(modificar=True)
        key_a_modificar = "a" #pasamos este parametro para entrar directamente al while
        while not verificar_rango(key_a_modificar, len(diccionario_a_modificar)+1):
            key_a_modificar = input("Que tipo quiere modificar?")
        try:
            opcion_seleccionada = list(diccionario_a_modificar)[int(key_a_modificar)-1]
        except IndexError:
            opcion_seleccionada = input("Que le gustaria agregar?")
        precio = input("Que precio le gustaria?")
        while not es_int(precio):
            print("Ingrese un numero por favor")
            precio = input("Que precio le gustaria?")
        diccionario_a_modificar[opcion_seleccionada] = int(precio)


class Pedido():
    def __init__(self, nombre_usuario, productos:Producto):
        self.nombre_usuario = nombre_usuario
        self.productos = productos
        self.total = 0
        self.carrito = dict()
        self.fecha = datetime.now()

    def __str__(self):
        return f"Pedido de {self.nombre_usuario} \nTotal: ${self.total} \nDetalles del pedido: Cupcake/s Sabor: {self.carrito['sabor'][0]} - Relleno: {self.carrito['relleno'][0]} - Cobertura: {self.carrito['cobertura'][0]} - Sprinkle: {self.carrito['sprinkle'][0]} "

    def hacer_pedido(self):
        def seleccionar(tipo:str, categoria):
            dict_tipo = self.productos.ver_productos(categoria)
            n = input(
                f"Ingrese el número de {tipo} que quiera:  ")
            while verificar_rango(n, len(dict_tipo)) == False:
                n = input(
                    "Ingrese un número valido de sabor que quiera:  ")
            return list(dict_tipo)[int(n) - 1]

        os.system('cls' if os.name == 'nt' else 'clear')
        total = 0
        while True:
            sabor_seleccionado = seleccionar("sabor",1)
            relleno_seleccionado = seleccionar("relleno",2)
            cobertura_seleccionada = seleccionar("cobertura",3)
            sprinkle_seleccionada = seleccionar("sprinkle",4)

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

class Tienda:

    def __init__(self,nombre, direccion, usuarios:dict = None):
        self.nombre = nombre
        self.direccion = direccion
        self.usuarios = usuarios
        self.productos = Producto()
        if usuarios is None:
            self.usuarios = dict()
            admin = Admin("Admin", "Maestro", "admin", "pass") #el usuario del admin es el mismo siempre por default
            self.usuarios["admin"] = admin
            print(f"Se creo el usuario Admin con los siguientes datos , {admin} ")


    def __str__(self):
        return f"Tienda: {self}"

    lista_pedidos = []

    def iniciar(self):

        inicio = False
        opcion = 0

        while inicio != True:
            opcion = "a"
            while not verificar_rango(opcion,4):
                opcion = input("Seleccione una opcion:\n1.Iniciar sesion\n2.Crear cuenta\n3.Salir\n")

            match int(opcion):
                case 1:
                    usuario_login = input("Ingrese su Usuario: ")
                    password_login = input("Ingrese su contrasena: ")
                    usuario_seleccionado = self.usuarios.get(usuario_login)
                    if usuario_seleccionado is None:
                        print("El Usuario no existe")
                    elif usuario_seleccionado.password != password_login:
                        print("Contrasena incorrecta")
                    else:
                        print("Login exitoso!")
                        usuario_seleccionado.menu(self)

                case 2:
                    cliente_nuevo = Cliente.crear_cliente()
                    if self.usuarios.get(cliente_nuevo.nombre_usuario) is None:
                        self.usuarios[cliente_nuevo.nombre_usuario] = cliente_nuevo
                    else:
                        print("Ya existe ese Usuario")

                case 3:
                    print("Gracias por usar nuestro programa!")
                    break

    def guardarDatos(self):
        with open('tienda.pickle', 'wb') as arch:
            pickle.dump(self,arch)


try:
    with open('tienda.pickle', 'rb') as arch:
        Blue_Velvet_Cupcakes = pickle.load(arch)
except FileNotFoundError:
    Blue_Velvet_Cupcakes = Tienda("Mi tienda", "Iguazu 123")

Blue_Velvet_Cupcakes.iniciar()
Blue_Velvet_Cupcakes.guardarDatos()