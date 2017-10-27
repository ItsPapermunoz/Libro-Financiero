import time
import IEM as iem
import pickle as pkl

# Classes
class Paquete:
    """Clase que define a el paquete de venta"""
    def __init__(self, nombre, destino, precio):
        self.nombre = nombre
        self.destino = destino
        self.precio = precio

# Functions

def cargar_paquetes():
    try:
        paquetes = pkl.load(open("Paquetes.data", "rb"))
    except FileNotFoundError:
        paquetes = []
        pkl.dump(paquetes,open("Paquetes.data", "wb"))
    finally:
        return paquetes


def cargar_libro():
    try:
        libro = pkl.load(open("libro.data", "rb"))
    except FileNotFoundError:
        libro = []
        pkl.dump(libro,open("libro.data", "wb"))
    finally:
        return libro


def nuevo_paquete():
    nuevo_nombre = input("Como se llama el paquete? ")
    nuevo_destino = input("Cual es el destino del paquete? ")
    try:
        nuevo_precio = int(input("Cual es el precio del paquete? "))
    except ValueError:
        print("El precio necesita ser un numero, intenta nuevamente...")
        nuevo_precio = int(input("Precio: "))
    pack = Paquete(nuevo_nombre, nuevo_destino, nuevo_precio)
    paquetes.append(pack)
    pkl.dump(paquetes, open("Paquetes.data", "wb"))


def leer_paquetes():
    for pack in paquetes:
        print("Nombre: {}\nDestino: {} \nPrecio: {}".format(pack.nombre, pack.destino, pack.precio))


pause = iem.pause
clear = iem.cls

paquetes = cargar_paquetes()
libro = cargar_libro()

leer_paquetes()
