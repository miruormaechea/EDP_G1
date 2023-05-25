import os  # esta libreria es la que usamos para limpiar la pantalla
import csv  # esta libreria es para las hojas de calculo
from Funciones import *  # este import nos trae la parte del codigo con todos los validadores
from datetime import datetime  # la usamos para las fechas
from time import sleep  # la usamos como "cooldown" de pantalla
import pickle




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

    def menu(self, tienda):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Bienvenido a la tienda de cupcakes online!")
        print("1. Ver productos")
        print("2. Hacer pedido")
        print("3. Ver pedidos")
        print("4. Cambiar contraseña")
        print("5. Cerrar Sesion")


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
        diccionario_a_modificar[opcion_seleccionada] =  precio


class Pedido():
    # Tiene un constructor que inicializa los atributos de un pedido
    # Tiene un método llamado "escribir_archivo", que escribe la información del pedido en un archivo CSV.
    # Tiene un método llamado "str" que devuelve una cadena formateada que representa los detalles del pedido
    def __init__(self, nombre_usuario, productos, total):
        self.nombre_usuario = nombre_usuario
        self.productos = productos
        self.total = total
        self.escribir_archivo()

    def __str__(self):
        return f"Pedido de {self.nombre_usuario} - Total: ${self.total} \nDetalles del pedido: {self.productos[4]} Cupcake/s Sabor: {self.productos[0]} - Relleno: {self.productos[1]} - Cobertura: {self.productos[2]} - Sprinkle: {self.productos[3]}"

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

                total += Producto.sabor[list(Producto.sabor)[int(n_sabor) - 1]] * int(cantidad)
                carrito.append(list(Producto.sabor)[int(n_sabor) - 1])
                total += Producto.relleno[list(Producto.relleno)[int(n_relleno) - 1]] * int(cantidad)
                carrito.append(list(Producto.relleno)[int(n_relleno) - 1])
                total += Producto.cobertura[list(Producto.cobertura)[int(n_cobertura) - 1]] * int(cantidad)
                carrito.append(list(Producto.cobertura)[int(n_cobertura) - 1])
                total += Producto.sprinkle[list(Producto.sprinkle)[int(n_sprinkle) - 1]] * int(cantidad)
                carrito.append(list(Producto.sprinkle)[int(n_sprinkle) - 1])
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

    def escribir_archivo(self):
        header = ["Fecha", "Hora", "Usuario", "Sabor", "Relleno", "Cobertura", "Sprinkle", "Cantidad de Cupcakes",
                  "Total"]

        if not os.path.isfile(pedidos_file) or os.path.getsize(pedidos_file) == 0:
            with open(pedidos_file, "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(header)

        with open(pedidos_file, mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            now = datetime.now()
            if csv_file.tell() == 0:  # Si el archivo esta vacio, entonces se escriben los headers
                writer.writerow(header)
            writer.writerow(
                [now.strftime("%Y-%m-%d"), now.strftime("%H:%M"), self.nombre_usuario,
                 self.productos[0], self.productos[1], self.productos[2], self.productos[3], self.productos[4],
                 self.total])

    def ver_pedidos(self, usuario):
        header = ["Fecha", "Hora", "Usuario", "Sabor", "Relleno", "Cobertura", "Sprinkle",
                  "Cantidad de Cupcakes", "Total"]


        try:
            with open(pedidos_file, mode='r') as csv_file:
                existe = False
                reader = csv.DictReader(csv_file, fieldnames=header)
                pedidos_usuario = []
                i = 0

                for row in reader:
                    if row.get("Usuario") == usuario:
                        existe = True
                        i += 1
                        print(
                            f'{i} Fecha: {row.get("Fecha")} - Total: ${row.get("Total")} - '
                            f'Cantidad de cupcakes: {row.get("Cantidad de Cupcakes")} - Sabor: {row.get("Sabor")} '
                            f'- Relleno: {row.get("Relleno")}  - Cobertura: {row.get("Cobertura")} - Sprinkle: {row.get("Sprinkle")}\n ')
                        pedidos_usuario.append(row)

                if existe == False:
                    print(f'Disculpa {usuario} no realizaste ningun pedido todavia')
                    sleep(7)
                else:
                    pedido = input("Ingrese el numero de pedido que quiere repetir, en caso de que no quiera repetir " \
                                   "presione cualquier otro numero: ")
                    while not es_int(pedido):
                        pedido = input("Ingrese un numero: ")
                    for i, row in enumerate(pedidos_usuario):
                        if i == int(pedido) - 1:
                            existe = True
                            datos_pedido = [row.get("Sabor"), row.get("Relleno"), row.get("Cobertura"),
                                            row.get("Sprinkle")]
                            # aca usamos el get que recomendo Ian
                            self.hacer_pedido(usuario, datos_pedido)
                    if existe == False:
                        print("Volviendo al menu principal")
                        sleep(10)

        except FileNotFoundError:
            print(f'Error: el archivo {pedidos_file} no se encuentra')


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
            opcion = "4"
            while not verificar_rango(opcion,3):
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