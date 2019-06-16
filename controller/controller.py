import sys
sys.path.append('../connection')
sys.path.append('../model')
sys.path.append('../view')
from model import RegisteredUser
from SignIn_ui import IniciarSesionView
from db_connection import DBconn
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
		#self.objeto = ventana1.passwd
		#ventana1.adelante2()
		ventana1.pushButton_2.clicked.connect(lambda: ventana1.actualizar())
		ventana1.pushButton.clicked.connect(lambda: ventana1.actualizar())
		#ventana1.pushButton_2.clicked.connect(lambda: self.mostrar(ventana1.passwd))
		ventana1.pushButton_2.clicked.connect(lambda: self.sign(ventana1.passwd, ventana1.user, ventana1.type))
		
		ventana1.pushButton.clicked.connect(lambda: self.crearCuenta(ventana1.passwd, ventana1.user, ventana1.type))

		sys.exit(app.exec_())

	def crearCuenta(self, passwd, user, typeu):
		print(typeu)
		if typeu == 1:
			print("creando cuenta")
		else:
			print("No se puede crear una cuenta Owner")
			pass
		self.reguser = RegisteredUser()
		self.reguser.username = user
		self.reguser.password = passwd
		self.reguser.type = typeu
		try:
			self.validacion = self.reguser.Register()
			if not (self.validacion):
				print("usuario libre")
		except:
			pass

	def sign(self, passwd, user, typeu):
		self.reguser = RegisteredUser()
		print(user)
		print(passwd)
		print("Tipo de usuario", typeu)
		self.reguser.username = user
		self.reguser.password = passwd
		self.reguser.type = typeu
		self.validacion = self.reguser.SignIn()
		print("Esto tiene validacion", self.validacion)#self.reguser.username, self.reguser.password)
		if (self.validacion):
			print("Ir a pantalla principal")
		else:
			print("Datos Incorrectos")
		

	def validar(self):
		self.query = "Select first_name from usuario where patente = %s and dni = %s"
		self.values = (self.patente, self.dni)
		return self.db.ejecutar(self.query,self.values)

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