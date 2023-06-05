import pickle
from Tienda import *

try:
    with open('tienda.pickle', 'rb') as arch:
        Blue_Velvet_Cupcakes = pickle.load(arch)
except FileNotFoundError:
    Blue_Velvet_Cupcakes = Tienda("Mi tienda", "Iguazu 123")

Blue_Velvet_Cupcakes.iniciar()
Blue_Velvet_Cupcakes.guardarDatos()
