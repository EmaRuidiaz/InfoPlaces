import sys
sys.path.append('../connection')
sys.path.append('../view')
from SignIn_ui import IniciarSesionView
import db_connection
from PyQt5 import QtCore, QtGui, QtWidgets
#import fondo_rc

import os

class ControllerUsuario:
	def imp(self):
		print("Controlador de usuario")


class Controller():

	def __init__(self):
		pass
		
	def Iniciar(self):
		import sys
		
		app = QtWidgets.QApplication(sys.argv)
		Ventana_Principal = QtWidgets.QMainWindow()
		ventana1=IniciarSesionView(Ventana_Principal)
		self.objeto = ventana1.passwd
		ventana1.adelante2()
		ventana1.pushButton_2.clicked.connect(lambda: ventana1.adelante2())
		ventana1.pushButton_2.clicked.connect(lambda: self.mostrar(ventana1.passwd))
		sys.exit(app.exec_())

	def mostrar(self, x):
		print(x," mensaje")

	def guardar(self, objeto):
		objeto="sadsad"
		print(objeto)
		return objeto

def clear(): #También la podemos llamar cls (depende a lo que estemos acostumbrados)
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")

if __name__ == "__main__":
	cs = Controller()
	cs.Iniciar()