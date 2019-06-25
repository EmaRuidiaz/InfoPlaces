import sys
sys.path.append('../connection')
sys.path.append('../model')
sys.path.append('../view')
from model import RegisteredUser, User, ShopOwner, Shop, Schedule
from SignIn2 import IniciarSesionView
from User import UserProfileView
from UserEdit import UserEditView
from CreateAccount import CreateAccountView
from db_connection import DBconn
from RegisterStore import RegisterStoreView
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
		ventana1.pushButton_Sign_In.clicked.connect(lambda: self.sign(ventana1.passwd, ventana1.user, ventana1.type,Ventana_Principal, "registrado"))
		ventana1.pushButton_Anonymous_access.clicked.connect(lambda: self.sign(ventana1.passwd, ventana1.user, ventana1.type,Ventana_Principal, "invitado"))
		ventana1.pushButton_Create_Account.clicked.connect(lambda: self.crearCuenta(Ventana_Principal))

	def cargarUsuario(self, ventana1, Ventana_Principal):
		self.reguser.firstname = ventana1.firstname
		self.reguser.lastname = ventana1.lastname
		self.reguser.username = ventana1.username
		self.reguser.birthdate = ventana1.birthdate
		self.reguser.email = ventana1.email
		self.reguser.password = ventana1.password
		self.reguser.type = ventana1.type
		self.reguser.image = ventana1.image
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
		
		if ventana1.terms == 1 and (ventana1.fechacontrol < 2019) and self.reguser.firstname and self.reguser.lastname and self.reguser.username and self.reguser.email and self.reguser.password and (len(self.reguser.password) > 8) and (self.reguser.password == self.confirmuser):
			
			if not self.reguser.CheckReg():
				if self.reguser.Register():
					self.reguser.RegisterPhoto()
					QMessageBox.about(Ventana_Principal, "Registro Exitoso", "Usuario Registrado Satisfactoriamente!")
					self.menuPrincipal(Ventana_Principal)
				else:
					pass
			else:
				QMessageBox.about(Ventana_Principal, "Error", "Puede que hayas ingresado mal los datos. O puede que el username y el correo ya esté en uso.")
				print("Email o Username en uso")
		else:
			QMessageBox.about(Ventana_Principal, "Error", "Puede que hayas ingresado mal los datos. O puede que el username y el correo ya esté en uso.")
		print(" checkReg")

	def Home(self, Ventana_Principal,user, tipo):
		#if estado == "nuevo":
		ventana1 = HomeView(Ventana_Principal, tipo, user)
		try:
			ventana1.pushButton_Create_Store.clicked.connect(lambda: self.crearStore(Ventana_Principal, user))
		except:
			pass
		ventana1.pushButton_Log_Out.clicked.connect(lambda: self.menuPrincipal(Ventana_Principal))
		ventana1.perfil.clicked.connect(lambda: self.user(Ventana_Principal, user))

	def sign(self, passwd="", user="", typeu="", Ventana_Principal="", usuario=""):
		print("Hola sign")
		if usuario == "registrado":
			print("Hola registrado")
			if typeu == 1:
				print("Hola tipo 1")
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
					self.reguser.firstname = self.validacion[0][2]
					self.reguser.lastname = self.validacion[0][3]
					self.reguser.username = self.validacion[0][0]
					self.reguser.birthdate = self.validacion[0][6]
					self.reguser.email = self.validacion[0][4]
					self.reguser.password = self.validacion[0][5]
					self.reguser.type = self.validacion[0][1]
					self.reguser.phone_number = self.validacion[0][7]
					self.reguser.image = self.validacion[0][8]
					self.Home(Ventana_Principal,self.reguser,1)
				else:
					QMessageBox.about(Ventana_Principal, "Datos Incorrectos", "Por favor, intente nuevamente. Si no está registrado, puede hacerlo gratuitamente.")
			elif typeu == 2:
				self.owner = ShopOwner()
				print(user)
				print(passwd)
				print("Tipo de usuario", typeu)
				self.owner.username = user
				self.owner.email = user
				self.owner.password = passwd
				self.owner.type = typeu
				self.validacion = self.owner.SignIn()

				print("Esto tiene validacion", self.validacion)

				#self.reguser.username, self.reguser.password)
				if (self.validacion):
					import sys
					import imagen_rc
					self.owner.firstname = self.validacion[0][2]
					self.owner.lastname = self.validacion[0][3]
					self.owner.username = self.validacion[0][0]
					self.owner.birthdate = self.validacion[0][6]
					self.owner.email = self.validacion[0][4]
					self.owner.password = self.validacion[0][5]
					self.owner.type = self.validacion[0][1]
					self.owner.phone_number = self.validacion[0][7]
					self.owner.image = self.validacion[0][8]
					self.Home(Ventana_Principal,self.owner,2)
				else:
					QMessageBox.about(Ventana_Principal, "Datos Incorrectos", "Por favor, intente nuevamente. Si no está registrado, puede hacerlo gratuitamente.")
		elif usuario == "invitado":
			self.user = User()
			ventana1 = HomeView(Ventana_Principal,1)

	

	def crearStore(self, Ventana_Principal, user):
		self.shop = Shop()
		self.schedule = Schedule()
		ventana1 = RegisterStoreView(Ventana_Principal, user)
		ventana1.pushButton_Create_Store.connect(lambda: ventana1.actualizar())
		ventana1.pushButton_Create_Store.connect(lambda: self.AddStore(self.shop, user, ventana1, self.schedule))

	def AddStore(self, shop, user, ventana1, schedule):
		shop.name = ventana1.name
		shop.address = ventana1.address
		shop.number = ventana1.number
		shop.description = ventana1.description

		#if shop.name and shop.address and shop.number and shop.description:


	def editarUser(self, Ventana_Principal, user, userresguardo):
		import imagen_rc
		self.userresguardo = user
		ventana1 = UserEditView(Ventana_Principal, user)
		ventana1.pushButton_GuardarCambios.clicked.connect(lambda: ventana1.actualizar())
		ventana1.pushButton_GuardarCambios.clicked.connect(lambda: self.UpdateUserEdit(user,self.userresguardo,ventana1, Ventana_Principal))
		#ventana1.pushButton_GuardarCambios.clicked.connect(lambda: self.Home(Ventana_Principal, user, user.type))
		ventana1.pushButton_GuardarCambios.clicked.connect(lambda: self.user(Ventana_Principal, user))
		

	def UpdateUserEdit(self, user, userresguardo, ventana1, Ventana_Principal):
		print("User: ", user.username)
		print("UserResguardo: ", userresguardo.username)
		self.usernameresguardo = user.username
		self.emailresguardo = user.email

		user.firstname = ventana1.firstname
		user.lastname = ventana1.lastname
		user.username = ventana1.username
		user.password = ventana1.password
		user.phone_number = ventana1.phone
		user.image = ventana1.fileName
		print("User: ", user.username)
		print("UserResguardo: ", userresguardo.username)
		if user.firstname and user.lastname and user.password:
			self.var = user.CheckReg()
			print("Var: ", self.var)
			if len(self.var) == 0 or self.var[0][0] == self.usernameresguardo:
				user.UpdateInfo(self.usernameresguardo)
				user.UpdatePhoto(self.usernameresguardo)
				QMessageBox.about(Ventana_Principal, "Update Succefull", "Se ha actualizado correctamente sus datos.")
			else:
				QMessageBox.about(Ventana_Principal, "Error", "El username, el email ya está en uso")
				print("User antes de asignar: ", user.username)
				print("UserResguardo: ", userresguardo.username)
				user = userresguardo
				user.username = self.usernameresguardo
				user.email = self.emailresguardo
				print("User: ", user.username)
				print("UserResguardo: ", userresguardo.username)
				self.editarUser(Ventana_Principal, user, userresguardo)
		else:
			QMessageBox.about(Ventana_Principal, "Error", "Datos Incompletos")
			user = userresguardo
			self.editarUser(Ventana_Principal, user, userresguardo)

	def user(self, Ventana_Principal, user=""):
		import imagen_rc
		ventana1 = UserProfileView(Ventana_Principal, user)
		ventana1.pushButton_back.clicked.connect(lambda: self.Home(Ventana_Principal, user, user.type))
		ventana1.pushButton_editUser.clicked.connect(lambda: self.editarUser(Ventana_Principal, user, user))

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