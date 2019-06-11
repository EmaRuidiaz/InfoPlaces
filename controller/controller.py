import sys
sys.path.append('../connection')
from interfaz_ui import IniciarSesion
import db_connection

import os


class Controller():

	def __init__(self):
		print("Holaaaaaaa")
		ventana = IniciarSesion()
		


	def iniciar_busqueda(self):
		print("Inicio Busqueda")

def clear(): #También la podemos llamar cls (depende a lo que estemos acostumbrados)
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")


cs = Controller()