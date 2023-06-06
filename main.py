from Tienda import *

# Intenta cargar la tienda existente desde un archivo pickle
# Si el archivo no se encuentra, crea una nueva tienda con valores predeterminados
try:
    with open('tienda.pickle', 'rb') as arch:
        Blue_Velvet_Cupcakes = pickle.load(arch)
except FileNotFoundError:
    Blue_Velvet_Cupcakes = Tienda("Mi tienda", "Iguazu 123")

# Inicializa la tienda y realiza las operaciones necesarias
Blue_Velvet_Cupcakes.iniciar()

# Guarda los datos actualizados de la tienda en el archivo pickle
Blue_Velvet_Cupcakes.guardarDatos()
