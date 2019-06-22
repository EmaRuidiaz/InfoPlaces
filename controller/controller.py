import sys
sys.path.append('../connection')
sys.path.append('../model')
sys.path.append('../view')
from model import RegisteredUser
from SignIn2 import IniciarSesionView
from CreateAccount import CreateAccountView
from db_connection import DBconn
from Home import HomeView
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
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
		import imagen_rc
		app = QtWidgets.QApplication(sys.argv)
		Ventana_Principal = QtWidgets.QMainWindow()
		self.menuPrincipal(Ventana_Principal)

		sys.exit(app.exec_())

### falta la ventana de register, una vez hecha. el registro se podra hacer llamando a este metodo ###
	def crearCuenta(self, Ventana_Principal):
		ventana1=CreateAccountView(Ventana_Principal)
		self.reguser = RegisteredUser()
		ventana1.pushButton_Create_Account.clicked.connect(lambda: ventana1.actualizar())
		ventana1.pushButton_Create_Account.clicked.connect(lambda: self.cargarUsuario(ventana1,Ventana_Principal))
		ventana1.pushButton_cancel.clicked.connect(lambda: self.menuPrincipal(Ventana_Principal))

	def menuPrincipal(self, Ventana_Principal):
		ventana1=IniciarSesionView(Ventana_Principal)
		ventana1.pushButton_Sign_In.clicked.connect(lambda: ventana1.actualizar())
		ventana1.pushButton_Sign_In.clicked.connect(lambda: self.sign(ventana1.passwd, ventana1.user, ventana1.type,Ventana_Principal))
		ventana1.pushButton_Create_Account.clicked.connect(lambda: self.crearCuenta(Ventana_Principal))

	def cargarUsuario(self, ventana1, Ventana_Principal):
		self.reguser.firstname = ventana1.firstname
		self.reguser.lastname = ventana1.lastname
		self.reguser.username = ventana1.username
		self.reguser.birthdate = ventana1.birthdate
		self.reguser.email = ventana1.email
		self.reguser.password = ventana1.password
		self.reguser.type = ventana1.type
		self.confirmuser = ventana1.confirmuser
		try:
			self.reguser.phone_number = int(ventana1.phone)
		except:
			if ventana1.phone:
				ventana1.terms = 0
				self.reguser.phone_number = None
				print("Numero de telefono está mal")
			else:
				pass
		
		if ventana1.terms == 1 and self.reguser.firstname and self.reguser.lastname and self.reguser.username and self.reguser.email and self.reguser.password and (self.reguser.password == self.confirmuser):
			
			if not self.reguser.CheckReg():
				print("Holaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
				if self.reguser.Register():
					print("Registrado")
					QMessageBox.about(Ventana_Principal, "Registro Exitoso", "Usuario Registrado Satisfactoriamente!")
					self.menuPrincipal(Ventana_Principal)
				else:
					pass
			else:
				QMessageBox.about(Ventana_Principal, "Error", "Puede que hayas ingresado mal los datos. O puede que el username y el correo ya esté en uso.")
				print("Email o Username en uso")
		else:
			QMessageBox.about(Ventana_Principal, "Error", "Puede que hayas ingresado mal los datos. O puede que el username y el correo ya esté en uso.")
			print("No completooo nada")
		print(" checkReg")

	def sign(self, passwd, user, typeu, Ventana_Principal):
		self.reguser = RegisteredUser()
		print(user)
		print(passwd)
		print("Tipo de usuario", typeu)
		self.reguser.username = user
		self.reguser.email = user
		self.reguser.password = passwd
		self.reguser.type = typeu
		self.validacion = self.reguser.SignIn()

		print("Esto tiene validacion", self.validacion)

		#self.reguser.username, self.reguser.password)
		if (self.validacion):
			import sys
			import imagen_rc
			self.reguser.firstname = self.validacion[0][3]
			self.reguser.lastname = self.validacion[0][4]
			self.reguser.username = self.validacion[0][1]
			self.reguser.birthdate = self.validacion[0][7]
			self.reguser.email = self.validacion[0][5]
			self.reguser.password = self.validacion[0][6]
			self.reguser.type = self.validacion[0][2]
			self.reguser.phone_number = self.validacion[0][8]
			ventana1 = HomeView(Ventana_Principal)
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