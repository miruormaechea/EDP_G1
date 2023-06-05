from Cliente import *
from Producto import *
from Admin import *
import pickle
class Tienda:

    def __init__(self, nombre, direccion, usuarios: dict = None):
        self.nombre = nombre
        self.direccion = direccion
        self.usuarios = usuarios
        self.productos = Producto()
        self.pedidos = []

        if usuarios is None:
            self.usuarios = dict()
            admin = Admin("Admin", "Maestro", "admin", "pass")  # el usuario del admin es el mismo siempre por default
            self.usuarios["admin"] = admin
            print(f"Se creo el usuario Admin con los siguientes datos"
                  f"\n Usuario: {admin.nombre_usuario} \nContrasena: {admin.password} ")

    def __str__(self):
        return f"Tienda: {self}"

    lista_pedidos = []

    def iniciar(self):

        inicio = False
        opcion = 0

        while inicio != True:
            opcion = "a"
            while not verificar_rango(opcion, 4):
                opcion = input(
                    "Seleccione una opcion:\n1.Iniciar sesion\n2.Crear cuenta\n3.Salir\n")

            match int(opcion):
                case 1:
                    usuario_login = input("Ingrese su Usuario: ")
                    usuario_seleccionado = self.usuarios.get(usuario_login)
                    password_login = input("Ingrese su contrasena: ")
                    if usuario_seleccionado is None:
                        print("El Usuario no existe")
                    elif usuario_seleccionado.password != password_login:
                        print("Contrasena incorrecta")
                    else:
                        print("Login exitoso!")
                        self.menu_cliente(self)

                case 2:
                    cliente_nuevo = Cliente.crear_cliente()
                    if self.usuarios.get(cliente_nuevo.nombre_usuario) is None:
                        self.usuarios[cliente_nuevo.nombre_usuario] = cliente_nuevo
                    else:
                        print("Ya existe ese Usuario")
                case 3:
                    print("Gracias por usar nuestro programa!")
                    break

    def factura(self, usuario_seleccionado, pedido):
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        archivo_factura = f"C:/Users/ormae/OneDrive/Documents/factura_{usuario_seleccionado.nombre}_{timestamp}.txt"
        with open(archivo_factura, "w") as archivo:
            # escribe la info en el archivo
            archivo.write(str(pedido) + "Fecha:" + timestamp)

    def guardarDatos(self):
        with open('tienda.pickle', 'wb') as arch:
            pickle.dump(self, arch)


    def menu_cliente(self, usuario_seleccionado):
        while True:
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
                    self.productos.ver_productos()
                case "2":
                    nuevo_pedido = Pedido(nombre_usuario=usuario_seleccionado, productos=self.productos)
                    nuevo_pedido.hacer_pedido()
                    usuario_seleccionado.confirmar_pedido(nuevo_pedido, self)


                case "3":
                    for i, pedido in enumerate(usuario_seleccionado.pedidos):
                        print(i + 1, pedido)
                    n_pedido = input("Si desea repetir un pedido, ingrese el numero del pedido que desea repetir\n "
                          "Cualquier otra tecla caso contrario")
                    if verificar_rango(n_pedido, len(usuario_seleccionado.pedidos)):
                        usuario_seleccionado.repetir_pedido(int(n_pedido),self)

                    input("Presione enter para continuar")


                case "4":
                    usuario_seleccionado.cambiar_contrasena()
                case "5":
                    break